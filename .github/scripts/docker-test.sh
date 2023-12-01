#!/bin/bash
cd /app
# Installing Requirements
echo -e "\033[33mTest 1: Installing requirements...\033[0m"
pip install -r requirements.txt

if [[ $? -ne 0 ]]; then
    echo -e "\033[31mFailed to install requirements\033[0m"
    exit 1
fi
echo -e "\033[32mTest 1: Completed\033[0m"

