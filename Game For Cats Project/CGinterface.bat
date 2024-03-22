@echo off
title Cat Adventure Game

:START
cls
echo Welcome to Cat Adventure Game!
echo.
echo 1. Chase the Dot
echo 2. Catch the Mouse
echo 3. Explore the Garden
echo 4. Exit
echo.

set /p choice="Enter your choice: "

if "%choice%"=="1" goto CHASE_DOT
if "%choice%"=="2" goto CATCH_MOUSE
if "%choice%"=="3" goto EXPLORE_GARDEN
if "%choice%"=="4" goto EXIT

echo Invalid choice. Please try again.
pause
goto START

:CHASE_DOT
cls
echo You're chasing the dot!
echo Watch it move and try to catch it!
echo.
pause
goto START

:CATCH_MOUSE
cls
echo You're hunting for mice!
echo Sneak up quietly and pounce when you see one!
echo.
pause
goto START

:EXPLORE_GARDEN
cls
echo You're exploring the garden!
echo Sniff around and see what you can find!
echo.
pause
goto START

:EXIT
cls
echo Thanks for playing Cat Adventure Game!
echo Meow!
echo.
pause
exit
