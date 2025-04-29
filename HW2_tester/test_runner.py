#!/usr/bin/env python3
import sys
import os
import json
import subprocess
import difflib

def load_manifest(path):
    with open(path, 'r', encoding='utf-8') as f:
        return json.load(f)

def collect_tests(manifest):
    tests = []
    for section, cases in manifest.items():
        if isinstance(cases, list):
            for case in cases:
                tests.append(case)
    return tests

def run_test(exe_path, input_path, expected_path):
    with open(input_path, 'rb') as f:
        input_bytes = f.read()
    try:
        proc = subprocess.run(
            [exe_path],
            input=input_bytes,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )
    except Exception as e:
        return False, f"Error running '{exe_path}' on '{input_path}': {e}"
    actual = proc.stdout.decode('utf-8', errors='replace')
    with open(expected_path, 'rb') as f:
        expected = f.read().decode('utf-8', errors='replace')
    if actual == expected:
        return True, None
    diff = difflib.unified_diff(
        expected.splitlines(keepends=True),
        actual.splitlines(keepends=True),
        fromfile='expected',
        tofile='actual'
    )
    return False, ''.join(diff)

def main():
    if len(sys.argv) != 3:
        print("Usage: python3 test_runner.py <path_to_executable> <manifest.json>")
        sys.exit(1)

    exe_path = sys.argv[1]
    manifest_path = sys.argv[2]

    if not os.path.isfile(exe_path):
        print(f"Executable not found: {exe_path}")
        sys.exit(1)
    if not os.path.isfile(manifest_path):
        print(f"Manifest not found: {manifest_path}")
        sys.exit(1)

    manifest = load_manifest(manifest_path)
    tests = collect_tests(manifest)
    failures = 0

    for case in tests:
        inp = case.get("input")
        out = case.get("output")
        if not inp or not out:
            print(f"❌ Invalid manifest entry (missing input/output): {case}")
            failures += 1
            continue
        if not os.path.isfile(inp):
            print(f"❌ Missing input file: {inp}")
            failures += 1
            continue
        if not os.path.isfile(out):
            print(f"❌ Missing output file: {out}")
            failures += 1
            continue

        ok, info = run_test(exe_path, inp, out)
        if ok:
            print(f"✅ PASS: {inp}")
        else:
            print(f"❌ FAIL: {inp}")
            print(info, end='')
            failures += 1

    if failures:
        print(f"\n🚨 {failures} test(s) failed.")
        sys.exit(1)
    else:
        print("\n🎉 All tests passed.")
        sys.exit(0)

if __name__ == "__main__":
    main()