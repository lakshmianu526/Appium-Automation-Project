# Test Automation for Sauce Labs My Demo App

This repository contains automated UI tests for the Sauce Labs My Demo App using Python, Appium, and pytest on macOS.

## Project Overview
- **Purpose**: Automate UI testing of the Sauce Labs My Demo App.
- **Tools**: Python, Appium, pytest, Git.
- **Environment**: macOS, Android Emulator (`emulator-5554`).

## Setup Instructions

1. **Clone the repository:**
   ```bash
   git clone https://github.com/lakshmianu526/Appium-Automation-Project.git
   ```

2. **Navigate to the project directory:**
   ```bash
   cd Appium-Automation-Project
   ```

3. **Create a virtual environment:**
   ```bash
   python3 -m venv myenv
   ```

4. **Activate the virtual environment:**
   ```bash
   source myenv/bin/activate
   ```

5. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

6. **Start the Appium server:**
   ```bash
   appium
   ```

7. **Run tests:**
   ```bash
   pytest tests/ --alluredir=reports/allure-results
   ```

## File Structure

```
Appium-Automation-Project/
│
├── pages/              # Page Object files (e.g., login_page.py)
├── tests/              # Test files (e.g., test_login.py)
├── utils/              # Utility files (e.g., driver.py)
├── reports/            # Test reports (Allure results)
├── requirements.txt    # Python dependencies
└── MyDemoApp.apk       # The app under test
```

## Running Tests

- To run specific tests:
  ```bash
  pytest tests/test_login.py
  ```

- To generate and view Allure reports:
  ```bash
  allure serve reports/allure-results
  ```
