#!/bin/sh
cd /app
# Installing Requirements
echo "\033[33mTest 1: Installing requirements...\033[0m"
pip install -r requirements.txt

if [ $? -ne 0 ]; then
    echo "\033[31mFailed to install requirements\033[0m"
    exit 1
fi
echo "\033[32mTest 1: Completed\033[0m"

# Creating .env file
echo "TG_BOT_TOKEN='$TG_BOT_TOKEN'" > .env
echo "PORT='$PORT'" >> .env

# Check if script is running properly
echo "\033[33mTest 2: Checking if script is running properly...\033[0m"

if [ $? -ne 0 ]; then
    echo "\033[31mFailed to create .env file\033[0m"
    exit 1
fi

timeout 10 python main.py

if [ $? -ne 124 ]; then
    echo "\033[31mFailed to run script\033[0m"
    exit 1
fi

echo "\033[32mTest 2: Completed\033[0m"