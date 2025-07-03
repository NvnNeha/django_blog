This is my first website with django, here you can create account and write blog, also you can update, delete your post, you can comment to the post if you are busy or not have time to read post so you can click read later button and see in stored posts all read later blog.


How to deploy your django app on ec2

#first update and install basic packages
sudo apt update
sudo apt install python3-venv python3-dev python3-pip libpq-dev nginx    # check pip3 --version #libpq-dev is important

git clone https://yourgitrepolink
cd your project folder

#create and activate virtualenv either python3 or virtualenv
pip3 install -r requirements.txt

# check python manage.py runserver 0.0.0.0:8000
# make sure you have run python manage.py makemigrations, migrate, collectstatic

# now install in virtualenv gunicorn, it is a wsgi server that server your website
pip install gunicorn
sudo nano /etc/systemd/system/gunicorn.socket 

# add content in it 
[Unit]
Description=gunicorn socket

[Socket]
ListenStream=/run/gunicorn.sock

[Install]
WantedBy=sockets.target


sudo nano /etc/systemd/system/gunicorn.service
# add content in it
[Unit]
Description=gunicorn daemon
Requires=gunicorn.socket
After=network.target

[Service]
User=ubuntu
Group=www-data
WorkingDirectory=/home/ubuntu/django_blog                   ### your manage.py path
ExecStart=/home/ubuntu/django_blog/env/bin/gunicorn \       ### here your active virtualenv path
          --access-logfile - \
          --workers 3 \
          --bind unix:/run/gunicorn.sock \
          nvnblog.wsgi:application                         ### here setting.py or wsgi server path

[Install]
WantedBy=multi-user.target


sudo systemctl start gunicorn.socket
sudo systemctl enable gunicorn.socket   # create a soft link between symlink /etc/systemd/system/sockets.target.wants/gunicorn.socket → /etc/systemd/system/gunicorn.socket.

## checking gunicorn socket file
sudo systemctl status gunicorn.socket
##your should recieve

● gunicorn.socket - gunicorn socket
     Loaded: loaded (/etc/systemd/system/gunicorn.socket; enabled; vendor preset: enabled)
     Active: active (listening) since Mon 2022-04-18 17:53:25 UTC; 5s ago
   Triggers: ● gunicorn.service
     Listen: /run/gunicorn.sock (Stream)
     CGroup: /system.slice/gunicorn.socket

Apr 18 17:53:25 django systemd[1]: Listening on gunicorn socket.
### check gunicorn service file as well
## before that run systemctl daemon-reload, systemctl restart gunicorn.service
sudo ststemctl status gunicorn.service

## Next, check for the existence of the gunicorn.sock file within the /run directory:
file /run/gunicorn.sock
Output
/run/gunicorn.sock: socket



# deactivate virtualenv

# set up nginx
cd /etc/nginx/site-available 
and create one file 

sudo nano /etc/nginx/site-available/blog

server {
    listen 80;
    server_name server_domain_or_IP;
    location = /favicon.ico { access_log off; log_not_found off; }
    location /static/ {
        root /home/sammy/myprojectdir; ### your manage.py path
    }
    location / {
        include proxy_params;
        proxy_pass http://unix:/run/gunicorn.sock;
    }
}

### now to create symbolic link to sites-enabled dir
sudo ln -s /etc/nginx/sites-available/blog /etc/nginx/sites-enabled/

## check nginx configuration
sudo nginx -t


### restart your nginx and gunicorn






