# AE_auto_scripts
 Automation scripts for registration testing

## Installation

Make sure you have **Python** installed on your machine.

After cloning the repository, install the required dependencies by running:

```bash
pip install -r requirements.txt

# Scripts

## `test_registration_happy.py`
- Tests the full successful registration flow with valid input.
- A new unique email address is generated automatically for every run to avoid duplication errors.

## `test_registration_unhappy.py`
- Tests invalid registration scenarios:
  - Blank fields
  - Wrong email format
  - Short password
  - Mismatched confirm password
  - Already registered email

---

# What the scripts cover

- Blank input validation (required field errors)
- Invalid email format validation
- Minimum password length validation
- Password mismatch validation
- Duplicate email validation
- Full successful registration flow
- URL redirection check after successful registration
