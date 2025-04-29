# HW Tester Archive

This repository is a multi-homework grading toolkit for C programming assignments. It currently includes **two** separate testing harnesses:

1. **HW1 Tester** (`hw1/` folder)
2. **HW2 Tester** (`hw2/` folder)

Each tester is designed to be **plug & play** for beginners: unzip a student’s homework ZIP, compile their code (if needed), and automatically run I/O tests.

---

## Repository Layout

```
hw-tester/             # Repo root
├── hw1/               # HW1 tester (manual harness)
│   ├── Q1_files/          # Q1 input+output test cases for HW1
│   └── Q2_files/          # Q2 input+output test cases for HW1

└── hw2/               # HW2 tester (automated script)
    ├── simulate_env.sh    # Script to unzip, compile, and run HW2 tests
    ├── test_runner.py     # Python I/O test harness
    ├── tests_all.json     # JSON manifest of HW2 test files
    ├── hw2_q1/            # Q1 input+output test cases for HW2
    ├── hw2_q2/            # Q2 input+output test cases for HW2
    └── hw2_q3/            # Q3 input+output test cases for HW2
```

> **Note:** HW1 harness is manual: you invoke the Python test runner directly. HW2 includes a helper script (`simulate_env.sh`) that automates unzip, compile, and test steps.

---

## Prerequisites

- **Bash** (for HW2 script, Linux/macOS)
- **GCC** (e.g. `gcc`)
- **Python 3** (to run `test_runner.py`)

## Using the HW1 Tester

> **Note:** The HW1 testing harness is maintained separately in its own repository.
> You must first clone it into this folder:
> 
> ```bash
> git clone https://github.com/DarkLordF1/CprogHW1.git hw1
> ```

Once you have the `hw1/` directory in place, follow the steps below:

## Using the HW1 Tester

1. **Enter the HW1 folder**:
   ```bash
   cd hw1
   ```
2. **Compile** the student’s code or use your reference binary (e.g. `hw1_q1` and `hw1_q2` executables).
3. **Run** the Python harness:
   ```bash
   python3 test_runner.py ./<binary> tests_all.json
   ```
   - `<binary>` should be the compiled executable that reads stdin and writes stdout.
   - For example: `python3 test_runner.py ./Q1_files/hw1_q1 tests_all.json`.

You’ll see a pass/fail summary for each test file.

## Using the HW2 Tester

1. **Enter the HW2 folder**:
   ```bash
   cd ../hw2
   ```
2. **Make the helper script executable** (once per machine):
   ```bash
   chmod +x simulate_env.sh
   ```
3. **Run**:
   ```bash
   ./simulate_env.sh HW2_123456789.zip [path/to/hw2.c]
   ```
   - The ZIP **must** be named `HW2_<StudentID>.zip`.
   - Ensure the ZIP file includes `hw2.c` before running the script; no additional argument is necessary.

The script will unzip, compile, run all tests, and display results.

Here you will find the tests for the rest of the homework accordingly.

## Contributing

- Found a bug? Open an issue.
- Improvements or new homeworks? Submit a pull request.

Happy grading! 🎉

