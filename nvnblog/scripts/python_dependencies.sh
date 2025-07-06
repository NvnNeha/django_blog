#!/usr/bin/env bash
set -e

PROJECT_MAIN_DIR_NAME="nvnblog"

# # Validate variables
# if [ -z "$PROJECT_MAIN_DIR_NAME" ]; then
#     echo "Error: PROJECT_MAIN_DIR_NAME is not set. Please set it to your project directory name." >&2
#     exit 1
# fi

# # Change ownership to ubuntu user
# sudo chown -R ubuntu:ubuntu "/home/ubuntu/$PROJECT_MAIN_DIR_NAME"

# create directory for virtual environment
sudo mkdir projectenv
cd projectenv

# Create virtual environment
echo "Creating virtual environment..."
python3 -m venv env

# Activate virtual environment
echo "Activating virtual environment..."
source "/home/ubuntu/projectenv/env/bin/activate"

# Install dependencies
echo "Installing Python dependencies..."
pip3 install -r "/home/ubuntu/blog_aws/$PROJECT_MAIN_DIR_NAME/requirements.txt"

echo "Dependencies installed successfully."
