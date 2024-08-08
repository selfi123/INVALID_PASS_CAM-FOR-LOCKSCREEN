@echo off

set "exe_path=PASSCAM.exe"

set "task_name=RunExecutableOnFailedLogin"

schtasks /create /tn "%task_name%" /tr "\"%exe_path%\"" /sc onevent /ec Security /mo *[System/EventID=4625] /ru "SYSTEM" /rl HIGHEST /f /it /np

schtasks /change /tn "%task_name%" /it /ru "SYSTEM" /rl HIGHEST /f

echo Task Scheduler entry created to run executable on Event ID 4625.
pause
