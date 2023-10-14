@echo off
echo Which folder do you want to open?
echo 1 - private projects
echo 2 - GitHub

set /p choice=Please enter the number of the folder and press Enter: 

if "%choice%"=="1" (
    call private.bat
) else if "%choice%"=="2" (
    call github.bat
) else (
    echo Invalid selection.
)

rem 
exit
