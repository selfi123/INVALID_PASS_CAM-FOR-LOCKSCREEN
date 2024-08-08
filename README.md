
# INVALID_PASS_CAM-FOR-LOCKSCREEN

This repository contains a Python script and a batch file designed to capture a photo upon detecting failed login attempts on a Windows system. The captured image is saved in a specified folder, and the Python script runs automatically in response to failed login events.

## Features

- **Detect Failed Logins:** The Python script monitors Windows Security logs for failed login attempts.
- **Capture Photo:** When a failed login attempt is detected, the script captures a photo using a connected webcam.
- **Automatic Execution:** The batch file sets up the script to run automatically on system startup or when a failed login event occurs.

## Components

### Python Script: `detect_failed_logins.py`

This script performs the following actions:

1. **Retrieve Failed Logins:** Reads Windows Security logs to identify failed login attempts.
2. **Capture Photo:** Takes a photo using the webcam and saves it to a designated folder.
3. **Take Action:** Runs an action script and captures a photo whenever a failed login attempt is detected.

#### Requirements

- `pywin32`
- `opencv-python`

Install the required packages using pip:

```sh
pip install pywin32 opencv-python

```


### HOW TO USE:
Task Scheduler Setup

To create a scheduled task in Task Scheduler with the required settings:

    Open Task Scheduler:
        Press Win + R, type taskschd.msc, and press Enter.

    Create a New Task:
        In the right pane, click Create Task.

    General Tab:
        Name: Enter a name for the task (e.g., "FailedLoginMonitor").
        Description: (Optional) Enter a description.
        Security Options:
            Run with highest privileges: Check this box.
            Run whether user is logged on or not: Check this box.
            Configure for: Select your version of Windows.

    Triggers Tab:
        Click New.
        Begin the task: Select On an event.
        Settings:
            Log: Select Security.
            Source: Select Microsoft Windows security auditing.
            Event ID: Enter 4625.
        Click OK.

    Actions Tab:
        Click New.
        Action: Select Start a program.
        Program/script: Enter the path to the batch file (e.g., C:\Path\To\Your\Batch\setup.bat).
        Add arguments (optional): Leave this blank.
        Click OK.

    Conditions Tab:
        Configure any conditions if needed (usually you can leave this as default).

    Settings Tab:
        Ensure Allow task to be run on demand is checked.
        Check other settings as needed (e.g., If the task fails, restart every).

    Save and Exit:
        Click OK to save the task.
        You may be prompted to enter your credentials. Enter the credentials for an account with sufficient permissions.
