# Grade Classifier

This program reads a student's mark out of 100, validates the input, and prints the corresponding letter grade. It helps ensure proper input handling and clear output formatting for beginner Python learners.

## Setup

python -m venv .venv
source .venv/bin/activate      # macOS and Linux 
.venv\Scripts\Activate.ps1     # Windows PowerShell 
.venv\Scripts\activate.bat     # Windows Command Prompt 
pip install -r requirements.txt

## Run

python grade_classifier.py

## Example

Enter a mark out of 100: 85
The letter grade for 85 is: B

## Known limitations

Currently supports only integer input between 0 and 100.
Future improvements could include handling decimal marks and adding automated test cases.
