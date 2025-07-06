#!/usr/bin/env bash

sudo apt update

# Install packages that require to os
sudo apt install python3-pip python3-dev python3-venv nginx libpq-dev -y



GIT_REPO_URL="https://github.com/NvnNeha/blog_aws.git"
#GIT_REPO_URL="https://<your_username>:<your_PAT>@github.com/codewithmuh/django-aws-ec2-autoscaling.git"

# Replace {YOUR_PROJECT_MAIN_DIR_NAME} with your actual project directory name
# Clone repository
git clone "$GIT_REPO_URL" 
PROJECT_MAIN_DIR_NAME="nvnblog"

sudo mkdir projectenv
cd projectenv
# Create virtual environment
echo "Creating virtual environment..."
python3 -m venv env

# Activate virtual environment
echo "Activating virtual environment..."
source "/home/ubuntu/projectenv/env/bin/activate"

# Install dependencies
cd "/home/ubuntu/blog_aws/$PROJECT_MAIN_DIR_NAME"
echo "Installing Python dependencies..."
pip3 install -r "/home/ubuntu/blog_aws/$PROJECT_MAIN_DIR_NAME/requirements.txt"

# Copy gunicorn  service file
sudo cp "/home/ubuntu/blog_aws/$PROJECT_MAIN_DIR_NAME/gunicorn/gunicorn.service" "/etc/systemd/system/"
sudo cp "/home/ubuntu/blog_aws/$PROJECT_MAIN_DIR_NAME/gunicorn/gunicorn.socket" "/etc/systemd/system/"

sudo usermod -a -G www-data ubuntu

# Start and enable Gunicorn service
sudo systemctl start gunicorn.socket
sudo systemctl enable gunicorn.socket

sudo systemctl start gunicorn.service
sudo systemctl enable gunicorn.service

sudo systemctl daemon-reload
sudo systemctl restart gunicorn

sudo touch /etc/nginx/sites-available/content
cat /home/ubuntu/blog_aws/nvnblog/nginx/content | sudo tee /etc/nginx/sites-available/content

sudo ln -s /etc/nginx/sites-available/content /etc/nginx/sites-enabled/
sudo systemctl daemon-reload
sudo systemctl restart gunicorn
sudo systemctl restart nginx

# Make all .sh files executable
# chmod +x scripts/*.sh

# Execute scripts for OS dependencies, Python dependencies, Gunicorn, Nginx, and starting the application
# ./scripts/os_dependencies.sh
# ./scripts/python_dependencies.sh
# ./scripts/gunicorn.sh
# ./scripts/nginx.sh