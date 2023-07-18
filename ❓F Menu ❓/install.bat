@echo off
title Installing
color 04

echo Installing the shit you need my homie 

REM Install pip if not already installed
python -m ensurepip --default-pip

REM Install the required modules
python -m pip install scapy colorama termcolor selenium requests

echo.
echo installed successfully my g
Python menu.py
pause
