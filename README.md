   # Overview
   This is a detailed note while deplying the "Item Catalog" app to AWS EC2 service.
* 10/26
-----
- set up WinSCP connection; 
- got permission denies while changing files as 'ubuntu' user; 
- solved the problem by `sudo chown -R -v ubuntu /var/www/` in ssh
___
- set up FlaskApp: `cd /var/www` `sudo mkdir *App*` `cd *App*` `sudo mkdir *App*` `cd *App*` `sudo mkdir static templates`
```
|----*App*
|---------*App*
|--------------static
|--------------templates
```
- `sudo nano __init__.py` with
```
from flask import Flask
app = Flask(__name__)
@app.route("/")
def home():
    return "Hello, I am your new App"
if __name__ == "__main__":
    app.run()
```
- `sudo apt-get install python-pip` `sudo pip install virtualenv` `sudo virtualenv venv` -- establish and enter virtual environment
- `sudo pip install Flask` `sudo python __init__.py` -- install Flask under venv and run the test .py under venv; it should bounce back `* Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)`
- `Press CTRL+C` & `deactivate`
- `sudo nano /etc/apache2/sites-available/myApp.conf` with
```
<VirtualHost *:80>
		ServerName mywebsite.com
		ServerAdmin admin@mywebsite.com
		WSGIScriptAlias / /var/www/myApp/myapp.wsgi
		<Directory /var/www/myApp/myApp/>
			Order allow,deny
			Allow from all
		</Directory>
		Alias /static /var/www/myApp/myApp/static
		<Directory /var/www/myApp/myApp/static/>
			Order allow,deny
			Allow from all
		</Directory>
		ErrorLog ${APACHE_LOG_DIR}/error.log
		LogLevel warn
		CustomLog ${APACHE_LOG_DIR}/access.log combined
</VirtualHost>
```
- `sudo a2ensite myApp`
- `cd ..` `sudo nano myapp.wsgi` with
```
#!/usr/bin/python
import sys
import logging
logging.basicConfig(stream=sys.stderr)
sys.path.insert(0,"/var/www/myApp/")

from myApp import app as application
application.secret_key = 'super secret key'
```
- `sudo service apache2 restart`
- test app deployed

* 10/25 
-----
- changed instance type from micro ($8/mon) to nano ($4/mon), ubuntu 16.04, 0.5G/15G.
* 10/22 
-----
- initiated an instance on EC2, ubuntu 16.04, 1G/15G.
- created an elastic IP and associated the instance to the IP.
- ssh to the instance ```ssh -i *key.pem* ubuntu@ip-address```   
- `sudo apt-get update`, `sudo apt-get upgrade`, and `sudo apt-get autoremove` were used to keep linux packages current.
- `sudo nano /etc/ssh/sshd_config`changed ssh timeout to be 2 hrs (30s*240)
- `sudo ufw default deny incoming`, `sudo ufw default allow outgoing`, `sudo ufw allow xxx` and `sudo ufw enable` were used to configure the firewall to only listen to SSH(port 22 and 2222), HTTP(port 80 and 8080), and NTP(port 123)
- `sudo apt-get install apache2/libapache2-mod-wsgi python-dev/python`--install Apache2/Python mod-wsgi/Python
- `sudo a2enmod wsgi` --enable wsgi
- 'Apache2 Ubuntu Default Page' dispalyed on the IP.
