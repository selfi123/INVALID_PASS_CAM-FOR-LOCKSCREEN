Creating a Task Scheduler Entry for an Executable
###
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
        Program/script: Enter the path to your executable file (e.g., C:\Path\To\Your\Executable\monitor_failed_logins.exe).
        Add arguments (optional): Leave this blank.
        Start in (optional): Enter the directory where your executable file is located (e.g., C:\Path\To\Your\Executable).
        Click OK.

    Conditions Tab:
        Configure any conditions if needed (usually you can leave this as default).

    Settings Tab:
        Ensure Allow task to be run on demand is checked.
        Check other settings as needed (e.g., If the task fails, restart every).

    Save and Exit:
        Click OK to save the task.
        You may be prompted to enter your credentials. Enter the credentials for an account with sufficient permissions.

Verification

    Check Task Status:
        In Task Scheduler Library, find your task and ensure it is listed.
        Right-click on the task and select Run to see if it executes successfully.

    Check Event Logs:
        Open Event Viewer (press Win + X and select Event Viewer).
        Go to Windows Logs > Security and verify that the event with ID 4625 is being logged.

    Check Task History:
        In Task Scheduler, right-click on the task and select View > Show Active Tasks or History to check for any errors or additional information.

Notes

    Ensure that the path to your executable file is correct and accessible by the Task Scheduler.
    Verify that you have the necessary permissions to create tasks and access security logs.
    Monitor the Task Scheduler and Event Viewer for any issues or additional information regarding task execution


###
