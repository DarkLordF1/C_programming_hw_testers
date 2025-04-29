import json
import subprocess

EXECUTABLE = "./hq2"
TEST_CASES_JSON = "test_cases.json"

with open(TEST_CASES_JSON, "r") as f:
    test_cases = json.load(f)

for idx, case in enumerate(test_cases, 1):
    with open(case["input_file"], "r") as f_in:
        input_data = f_in.read()
    with open(case["expected_output_file"], "r") as f_out:
        expected_output = f_out.read()

    process = subprocess.Popen(
        [EXECUTABLE],
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE
    )
    stdout, _ = process.communicate(input=input_data.encode())
    actual_output = stdout.decode()

    print(f"Test Case {idx}: ", end="")
    if actual_output.strip() == expected_output.strip():
        print("✅ Passed")
    else:
        print("❌ Failed")
        print(f"  Input:     {repr(input_data)}")
        print(f"  Expected:  {repr(expected_output)}")
        print(f"  Got:       {repr(actual_output)}")
