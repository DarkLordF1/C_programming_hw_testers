#!/usr/bin/env bash
set -euo pipefail

# Usage: ./grade_submission.sh HW2_<StudentID>.zip

if [ $# -ne 1 ]; then
  echo "Usage: $0 HW2_<StudentID>.zip"
  exit 1
fi

ZIPFILE="$1"

# 1. Validate the ZIP name matches HW2_<digits>.zip
if [[ ! "$ZIPFILE" =~ ^HW2_[0-9]+\.zip$ ]]; then
  echo "✗ ERROR: ZIP file must be named like 'HW2_123456789.zip'"
  exit 2
fi

WORKDIR=".submission"
rm -rf "$WORKDIR"
mkdir "$WORKDIR"

# 2. Unzip into a temporary folder
echo "→ Unzipping $ZIPFILE → $WORKDIR/"
unzip -q "$ZIPFILE" -d "$WORKDIR"

# 3. Check that hw2.c is present
if [ ! -f "$WORKDIR/hw2.c" ]; then
  echo "✗ ERROR: hw2.c not found inside the archive"
  exit 3
fi

# 4. Compile it
echo "→ Compiling hw2.c"
gcc -std=c99 -Wall -Werror -o "$WORKDIR/hw2" "$WORKDIR/hw2.c"

# 5. Run the test harness
echo "→ Running tests"
python3 test_runner.py "$WORKDIR/hw2" tests_all.json

# 6. Clean up
rm -rf "$WORKDIR"

echo "✓ Done."
