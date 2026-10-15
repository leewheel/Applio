@echo off

if /i "%cd%"=="C:\Windows\System32" (
    color 0C
    echo Applio does not require administrator permissions and should be run as a regular user.
    echo.
    pause
    exit /b 1
)

setlocal
for %%F in ("%~dp0.") do set "folder_name=%%~nF"

title %folder_name%

if not exist env (
    echo Please run 'run-install.bat' first to set up the environment.
    pause
    exit /b 1
)

set HTTP_PROXY=
set HTTPS_PROXY=
set http_proxy=
set https_proxy=
set NO_PROXY=*
set no_proxy=*
set ALL_PROXY=
set all_proxy=
env\python.exe app.py --open
echo.
pause
