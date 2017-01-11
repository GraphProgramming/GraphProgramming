@echo off

if "%1"=="" goto blank
if "%1"=="update" goto update
if "%1"=="install" goto install
if "%1"=="upgradepkg" goto upgradepkg
if "%1"=="upgrade" goto upgrade
if "%1"=="status" goto status

:blank
    echo Usage: gpm.bat COMMAND
    echo(
    echo Availible COMMANDs:
    echo   install PKG     # install a package
    echo   update          # update gpm
    echo   upgrade         # update all installed packages
    echo   upgradepkg PKG  # update only the package provided
    echo   status          # show the status of all packages
goto done

:update
    git pull
goto done

:install
    git clone git@github.com:GraphProgramming/%2.git
    cd %2
    install.bat
goto done

:upgradepkg
    cd %2
    git pull
    cd ..
goto done

:upgrade
    for /D %%i in (*.*) do (Echo "%%i" | FIND /I "images" 1>NUL) || (
        cd %%i
	echo Upgrading: %%i
        git pull
        cd ..
    )
goto done

:status
    echo "Status: GraphProgramming (meta-package)"
    git status
    for /D %%i in (*.*) do (Echo "%%i" | FIND /I "images" 1>NUL) || (
        cd %%i
	echo Status: %%i
        git status
        cd ..
    )
goto done

:done