#!/bin/sh
cd /app
echo -e "\033[33mInstalling requirements...\033[0m"
pip install -r requirements.txt
echo -e "\033[32mVigilant bot is starting...\033[0m"
/usr/local/bin/python main.py
