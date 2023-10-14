@echo off

set /p projectname=Enter project name: 
set "basepath=%USERPROFILE%\Documents\GitHub"
set "projectpath=!basepath!\!projectname!"

if not exist "!projectpath!" (
    mkdir "!projectpath!"
)

code "!projectpath!"

endlocal
