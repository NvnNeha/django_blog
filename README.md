This is my first website with django, here you can create account and write blog, also you can update, delete your post, you can comment to the post if you are busy or not have time to read post so you can click read later button and see in stored posts all read later blog.


How to deploy your django app on ec2

#first update and install basic packages
sudo apt update
sudo apt install python3-venv python3-dev python3-pip libpq-dev nginx    # check pip3 --version #libpq-dev is important

git clone https://your git repo
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
User=sammy
Group=www-data
WorkingDirectory=/home/ubuntu/django_blog
ExecStart=/home/ubantu/django_blog/env/bin/gunicorn \
          --access-logfile - \
          --workers 3 \
          --bind unix:/run/gunicorn.sock \
          nvnblog.wsgi:application

[Install]
WantedBy=multi-user.target


sudo systemctl start gunicorn.socket
sudo systemctl enable gunicorn.socket   # create a soft link between symlink /etc/systemd/system/sockets.target.wants/gunicorn.socket → /etc/systemd/system/gunicorn.socket.

# deactivate virtualenv

# set up nginx
cd /etc/nginx/site-available 
and check any file is exist or not if exist delete it sudo rm -rf default

sudo nano /etc/nginx/site-available/blog






























######## sudo systemctl status nginx.service ###### for this i remove default file from /etc/nginx/sites-enabled  and sites-available ######
######## sudo systemctl status gunicorn  #######





