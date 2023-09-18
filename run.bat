@echo off
rem Set the working directory to the current folder
cd /d %~dp0

rem Define the loading bar characters and length
set "loading_chars=-"
set "loading_length=60"

rem Clear the error flag
set "error_flag="

rem Start the pip installation in the background
start /b pip install -r requirements.txt >NUL 2>&1

rem Enable delayed expansion
setlocal enabledelayedexpansion

rem Initialize loading bar
set "loading_bar="

rem Function to display loading bar
:display_loading_bar
cls
echo Welcome to Reddit Comment Search by GabrielNezovic
echo.&echo The current working directory is:
echo %CD%
echo.&echo Checking on required packages:
if not "!error_flag!"=="" (
    echo.&echo Error: An error occurred during installation.
    goto :end
)

rem Display the loading bar
echo.&echo [!loading_bar!]

rem Check if the pip installation process is still running
tasklist /FI "IMAGENAME eq python.exe" | find /I "python.exe" >NUL
if %ERRORLEVEL% EQU 0 (
    set /a "loading_index+=1"
    if !loading_index! gtr %loading_length% (
        set "loading_index=0"
        set "loading_bar="
    ) else (
        set "loading_bar=!loading_bar!!loading_chars!"
    )
    goto :display_loading_bar
)

rem If the pip installation process has finished, continue with the script
goto :installation_complete

:end
rem Handle error and exit

:installation_complete
rem Continue with the rest of your script
endlocal
echo.&echo Required packages are available.
echo.&echo Starting up...
streamlit run search.py --server.port 1198 --browser.gatherUsageStats false --client.toolbarMode minimal --client.showErrorDetails false --runner.fastReruns true --theme.base dark --logger.level info