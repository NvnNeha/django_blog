📝 Django Blog Deployment on EC2
This is my first Django-based blog website!

🌐 Features
User registration and login

Create, update, and delete blog posts

Add comments to posts

Save posts for later reading using "Read Later" button

🚀 Deploy Django App on EC2
Follow the steps below to deploy your Django app on an Ubuntu EC2 instance.

1️⃣ Install System Dependencies
sudo apt update
sudo apt install python3-venv python3-dev python3-pip libpq-dev nginx
✅ libpq-dev is important for PostgreSQL support
✅ Make sure pip3 --version works

2️⃣ Clone Your Django Repository
git clone https://yourgitrepolink
cd your-project-folder

3️⃣ Set Up Virtual Environment
mkdir projectenv
cd projectenv
python3 -m venv env
source env/bin/activate
pip3 install -r requirements.txt

Run your project to confirm it works:
python manage.py makemigrations
python manage.py migrate
python manage.py collectstatic
python manage.py runserver 0.0.0.0:8000


4️⃣ Install & Configure Gunicorn
Install Gunicorn inside the virtual environment:
pip install gunicorn

Create the Gunicorn socket file:
sudo nano /etc/systemd/system/gunicorn.socket
Add:
[Unit]
Description=gunicorn socket

[Socket]
ListenStream=/run/gunicorn.sock

[Install]
WantedBy=sockets.target

Create the Gunicorn service file:
sudo nano /etc/systemd/system/gunicorn.service

[Unit]
Description=gunicorn daemon
Requires=gunicorn.socket
After=network.target

[Service]
User=ubuntu
Group=www-data
WorkingDirectory=/home/ubuntu/django_blog        # path to your project
ExecStart=/home/ubuntu/django_blog/env/bin/gunicorn \ 
          --access-logfile - \
          --workers 3 \
          --bind unix:/run/gunicorn.sock \
          nvnblog.wsgi:application                # your wsgi path

[Install]
WantedBy=multi-user.target

5️⃣ Enable and Start Gunicorn

sudo systemctl start gunicorn.socket
sudo systemctl enable gunicorn.socket

sudo systemctl start gunicorn.service
sudo systemctl enable gunicorn.service

sudo systemctl daemon-reload

sudo systemctl restart gunicorn.service
sudo systemctl restart gunicorn.socket

sudo chmod -a -G www-data ubuntu



6️⃣ Configure NGINX
Create an NGINX configuration file:

sudo nano /etc/nginx/sites-available/blog
Add:
server {
    listen 80;
    server_name your_domain_or_IP;
    location = /favicon.ico { access_log off; log_not_found off; }
    location /static/ {
        root /home/ubuntu/django_blog;  # static path
    }
    location / {
        include proxy_params;
        proxy_pass http://unix:/run/gunicorn.sock;
    }
}


sudo ln -s /etc/nginx/sites-available/blog /etc/nginx/sites-enabled/

sudo nginx -t
sudo systemctl restart nginx


✅ Done!
Now your Django blog is live on your EC2 instance via Gunicorn and NGINX!

📌 Notes
Always deactivate your virtual environment after finishing:
deactivate
Make sure your security group allows port 80 (HTTP).
































