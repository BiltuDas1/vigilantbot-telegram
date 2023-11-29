#!/bin/sh
cd /app
echo "\033[33mInstalling requirements...\033[0m"
echo "Installing requirements..."
pip install -r requirements.txt
clear
echo "\033[32mVigilant bot is starting...\033[0m"
/usr/local/bin/python main.py
