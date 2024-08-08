@echo off

set "script_path=passcam.py"
::set the path for python.exe exeutable((find the location using ((where python)) in cmd))
set "python_exe=C:\Python312\python.exe"

set "task_name=RunPythonScriptOnFailedLogin"

schtasks /create /tn "%task_name%" /tr "\"%python_exe%\" \"%script_path%\"" /sc onevent /ec Security /mo *[System/EventID=4625] /ru "SYSTEM" /rl HIGHEST /f /it /np

schtasks /change /tn "%task_name%" /it /ru "SYSTEM" /rl HIGHEST /f

echo Task Scheduler entry created to run script on Event ID 4625.
pause
