
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

RUN THE setup.bat file to set the settings according to the function of the executable to run on the startup before logging in.

```````  setup.bat ```````


EXECUTABLE FILE IN THE executable folder , to set it as same as previous python file , use the bat file in the folder
