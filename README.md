   # Overview
   This is a detailed note while deplying the "Item Catalog" app to AWS EC2 service.

-----
* 10/30 Mon
- worked some more on the error issue; updated all bootstrap files (redownload and copy over); rebooted the instance and restart the service; still not working.
- then I went to the serious debugging mode and changed the main.html line by line; seem there is a problem when I swtich from loading bootstrap.min.css or bootstrap.min.js over internet to over local host. checked developer's tool and opened 'IP/static/css/bootstrap.min.css', found it does not match with what I have put on the server. Now it seems my browser is storing old .css and .js for me and skipped my updates...; tried CTRL+F5; it worked...; like I expected, very very dumb mistake; I am happy that I did not give up and figured it out eventually.
- work on a 'CTRL+SHIFT+N' page now.
- built the homepage with index.html with extends and include
- hard coded two list groups for 'catalogs' and 'items' respectively.
![alt text](https://github.com/abigcleverdog/Web-app-deployment-EC2-001/blob/master/img/20171030_Capture.PNG "Project Snapshot")
- next step will be building the database to host cats and items and users ...
-----
* 10/29 Sun
- followed some tutorial trying to set up the web app with local bootstrap.min.css and bootstrap.min.js; the Python-Flask syntax worked, but the .js file gave an error said, "Uncaught reference, Popper is not defined" in the "index.js:21"; searched solution for quite a while, no answer found; switched to all CDN calls, and it worked; copied the CDN server files to local host, still same error; I guess that I am sticking with the CDN for now till I figure something out. By the way, this is quite wierd as nobody seems to run into the same problem, which is usually a good indicator that I have done something super stupid.
- try to reproduce the Item Catalog App homepage layout with Bootstrap. the 'navbar' packages are very easy to use and provide eye-pleasing styles. I will leave the fine tuning of the CSS for later.
![alt text](https://github.com/abigcleverdog/Web-app-deployment-EC2-001/blob/master/img/20171029_Capture.PNG "Project Snapshot")
-----
* 10/28
- watched several tutorial videos now I want to rebuild the Item Catalog App with Bootstrap from scratch. I may spend some time on the Bootstrap page in the next a few days.
-----
* 10/27
- set up app with bootstrap css;
- Notepad++ (ver 7.4) had the issue of cannot edit/save empty file, updated to 7.5;
- all html templates need to be under the templates directory... 
-----
* 10/26
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
-----
* 10/25 
- changed instance type from micro ($8/mon) to nano ($4/mon), ubuntu 16.04, 0.5G/15G.
-----
* 10/22 
- initiated an instance on EC2, ubuntu 16.04, 1G/15G.
- created an elastic IP and associated the instance to the IP.
- ssh to the instance ```ssh -i *key.pem* ubuntu@ip-address```   
- `sudo apt-get update`, `sudo apt-get upgrade`, and `sudo apt-get autoremove` were used to keep linux packages current.
- `sudo nano /etc/ssh/sshd_config`changed ssh timeout to be 2 hrs (30s*240)
- `sudo ufw default deny incoming`, `sudo ufw default allow outgoing`, `sudo ufw allow xxx` and `sudo ufw enable` were used to configure the firewall to only listen to SSH(port 22 and 2222), HTTP(port 80 and 8080), and NTP(port 123)
- `sudo apt-get install apache2/libapache2-mod-wsgi python-dev/python`--install Apache2/Python mod-wsgi/Python
- `sudo a2enmod wsgi` --enable wsgi
- 'Apache2 Ubuntu Default Page' dispalyed on the IP.
