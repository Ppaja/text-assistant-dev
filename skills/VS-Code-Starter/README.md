# VS Code Project Launcher

## Overview
The VS Code Project Launcher is a set of batch files designed to streamline the process of opening and managing your projects in Visual Studio Code (VS Code). It provides options for opening both local and GitHub projects, making it easier to switch between different coding tasks. It is easily expandable if you need more than these 2 parent folders (one for github projects and one for local private projects).

## Before Use (installation)
1. download the project
2. move the folder to a place of your choice
3. create a shortcut for start.bat and move it to the desktop or where you have quick access to it. If you like you can change the shortcut settings by giving it the example logo (logo.ico)
4. Make sure all batch files (`start.bat`, `private.bat`, `github.bat`) are in the same directory.
5. (optional) change the paths inside github.bat or private.bat to fit the desired destination folder. By default, the Github superfolder is documents/github and for private projects documents/programming\private
6. (optional) If you store all of your projects in one folder, you can simply use one bat file (private.bat) instead of start.bat

## How to Use
1. Run `start.bat` with your shortcut to display the menu.
2. Choose an option:
    - Press `1` for local projects.
    - Press `2` for GitHub projects.
3. For local projects:
    - Enter the name of the project you want to open and press Enter.
    - VS Code will open in the selected project directory. If the project doesn't exist, a new one will be created and then opened.
4. For GitHub projects:
    - same as for local projects, but with a different folder.

## Requirements
Ensure you have the following software installed:
- [Visual Studio Code](https://code.visualstudio.com/)


## Contributions
Contributions to this project are welcome. Feel free to submit issues, fork the repository, or create pull requests to enhance the functionality.


## Author
- [Ppaja](https://github.com/Ppaja)

