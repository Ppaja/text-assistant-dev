@echo off
setlocal

set /p projectname=Enter project name: 
set "basepath="%USERPROFILE%\Documents\GitHub""
set "projectpath=%basepath%\%projectname%"

if not exist "%projectpath%" (
    mkdir "%projectpath%"
)

code "%projectpath%"

endlocal@echo off
setlocal

set /p projectname=Enter project name: 
set "basepath="%USERPROFILE%\Documents\programming\private""
set "projectpath=%basepath%\%projectname%"

if not exist "%projectpath%" (
    mkdir "%projectpath%"
)

code "%projectpath%"

endlocal
exit