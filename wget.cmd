@echo off
setlocal
powershell -NoProfile -ExecutionPolicy Bypass -File "%~dp0wget.ps1" %*
exit /b %ERRORLEVEL%