#!/bin/sh
cd /app
echo "\033[33mInstalling requirements...\033[0m"
pip install -r requirements.txt

if [[ $? -ne 0 ]]; then
    echo "\033[31mFailed to install requirements\033[0m"
    exit 1
fi
echo "\033[32mVigilant bot is starting...\033[0m"
/usr/local/bin/python main.py
