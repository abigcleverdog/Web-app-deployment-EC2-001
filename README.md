   # Overview
   Quick note to future self: 2020/4/15, AWS hardware retired and one of my instance need to restart. 1. start the instance on AWS; 2. get the new IP, in browser, this should show the Apache start page; PuTTY to the IP and `sudo nano /etc/apache2/sites-available/xyz.conf` with
```
<VirtualHost *:80>
		ServerName <NEW IP>
		
```
   `sudo a2ensite xyz(usually folder name and already enabled)`  `sudo service apache2 restart`
   
   2019-10: add new function 'grade scantron' to the website.
   
   11/08--present: building "our Graduates";
   
   10/22--11/08: a detailed note while deplying the "Item Catalog" app to AWS EC2 service.
   
  
-----
* 2019/10/22 Tue
- After a couple of weeks of reconfiguring and testing, the 'grade scantron' function is now online;
![alt text](https://github.com/abigcleverdog/Web-app-deployment-EC2-001/blob/master/img/20191022_1_Capture.PNG "Project Snapshot")
- Sample input and outputs;
![alt text](https://github.com/abigcleverdog/Web-app-deployment-EC2-001/blob/master/img/20191022_2_Capture.PNG "Project Snapshot")
so far, the flask and grading scripts are running on py3 instead of py2, upgrading was a lot of 'FUN'; installing new packages for image processing, pdf converting etc. was directed to certain path; swapped 4G disk for memory to handle the grading; as a side task, the server is now on a new key as the old one is lost.

next would be 
- upgrade grading script for auto ROI detect/calibration;
- provide feedback while grading, right now grading 100 pages would have ~10min blank waiting time, pretty bad UI experience;

-----
* 12/20 Wed
- Added a JavaScript covering div, need a passcode to view the content;
![alt text](https://github.com/abigcleverdog/Web-app-deployment-EC2-001/blob/master/img/20171220_1_Capture.PNG "Project Snapshot")
next would be 
- add support/donation function;
- add a master editting page for bulk updating;
       
-----
* 11/30 Thu
- Linked database to search; adjust css to confine result box;
![alt text](https://github.com/abigcleverdog/Web-app-deployment-EC2-001/blob/master/img/20171130_1_Capture.PNG "Project Snapshot")
next would be 
- add support/donation function;
- add a master editting page for bulk updating;
    
-----
* 11/29 Wed
- Created a semi-live search bar with dummy dataset; The search engine is powered on javascript, should be enough for small datasets, given the number of students (10/yr * 100yr), runtime should be under 1 second.
![alt text](https://github.com/abigcleverdog/Web-app-deployment-EC2-001/blob/master/img/20171129_1_Capture.PNG "Project Snapshot")
next would be 
- add search function-link up the database
- add support/donation function;
- add a master editting page for bulk updating;
    
-----
* 11/26 Sun
- App status:
1. the homepage display the information of some most graduated students, statistics of our graduates;
1' an alternative homepage layout is designed for mobile device viewport;
2. user can navigate to different classes to find certain student via either the left-hand tabs or the bars on the 'grads vs. year' plot;
3. created a master user for editing some content via the web site;
4. once logged in as the master user, one can upload profile pic for each student;
next would be 
- send out for review;
- add search function;
- add support/donation function;
    
-----
* 11/25 Sat
- just before nuc the server, my self-esteem popped in and asked 'Really? You cannot do better than that?' well, I thought, OK, what I can do? Maybe reinstall python on the server; or maybe I should look up the error log on the server `sudo tail -f /var/log/apache2/error.log`; Now it says clearly 
```
[Sat Nov 25 11:48:24.973853 2017] [wsgi:error] [pid 17586:tid 140622446909184] [client 73.156.145.73:33707]     from passlib.hash import sha256_crypt, referer: http://13.58.39.136/2014/
[Sat Nov 25 11:48:24.973871 2017] [wsgi:error] [pid 17586:tid 140622446909184] [client 73.156.145.73:33707] ImportError: No module named passlib.hash, referer: http://13.58.39.136/2014/
```
Now search 'wsgi No module named passlib.hash'; well there we go `sudo pip install paramiko PyYAML jinja2 httplib2 passlib` it seems working now;
- Nah, I was wrong, it browser was loading cache. The server still says 'No module named passlib.hash'; keep searching; someone suggested this is an environment issue, I need some how run `flask/bin/pip install passlib`; I remember installing Flask under venv; so activated the vene `source venv/bin/activate`; `sudo -H pip install passlib`; get into 'venv/bin' found pip; `(sudo -H) pip install passlib`, server says 'Requirement already satisfied'; `deactivate` out the env; restart apache; it is working now;
- now EC2 is sync with local instance; most pages work; the file uploaing is rejected as 'permission denied' for the uploading folder; seems a linux user permission isssue; need to grant permission to the user for apache (maybe www-data); as I still need the ubuntu user to have full control so that I can use WinSCP to transfer files, I would like to test 1. add a usergroup of 'www-data' and 'ubuntu', 2. grant permission to the usergroup; The internet on my computer is experiencing some issue, it says 'Unidentified network No Internet Access' for a while. has to pause the work.
- it worked: 1. `sudo usermod -a -G myusergroup ubuntu` `sudo usermod -a -G myusergroup www-data` 2. `sudo chgrp -R myusergroup /var/www/` 3. `sudo chmod -R g+w /var/www/` 4. `sudo reboot`; now both apache and ubuntu have control of the www folder. upload tested, WinSCP tested. **seems still one issue: the uploaded file cannot be deleted via WinSCP maybe because it belongs to 'www-data'?? Let's try `sudo chmod -R 775 /var/www/` -- nope, doesn't work; search for linux delete file owned by another user -- well does not seem to be a easy thing to do. It may be easier to just alter the sql from the server site if I need to unlink a pic.
next would be 
- send out for review;
    
-----
* 11/24 Fri
- go through the login_required logic;
- configured postgresql to add column to 'student'; the problem was the peer authentification; solved it by change the `/etc/postgresql/9.5/main/pg_hba.conf` 'local  all  postgres  peer' to 'local  all  postgres  md5' then log on as 'user' + 'password'; 
- tried to sync the app on EC2, there is a "Internal Server Error" whenever I include this `from passlib.hash import sha256_crypt`; no similiar cases found online;

next would be 
- nuc the server and start fresh;
    
-----
* 11/22 Wed
- link updated for login/logout;
- pic upload and update database to display uploaded profile pic
![alt text](https://github.com/abigcleverdog/Web-app-deployment-EC2-001/blob/master/img/20171122_1_Capture.PNG "Project Snapshot")
- align pictures;
![alt text](https://github.com/abigcleverdog/Web-app-deployment-EC2-001/blob/master/img/20171122_2_Capture.PNG "Project Snapshot")

next would be 
- sync with EC2;
    
-----
* 11/21 Tue
- created admin user; tested /login and /logout;
- for future students, it may be a good idea to auto generate their accounts with ('fname[0]'+'lname') / [default password]; I will keep the data structure as is for now though; The idea is that for version 1.0 I just need one master user to input the info, others are consumers, they can send requests via email to update info;

next would be 
- user system; complete the admin user links;
- pic upload; now need to link the uploaded pic with specific student;
        
-----
* 11/20 Mon
- finished video/documentation tutorial on upload pic files (it seems the extension control is not working as I can still upload .pdf files)

next would be 
- user system
- pic upload
     
-----
* 11/19 Sun
- add 'email', 'LinkedIn', 'Facebook" icons with Font-Awesome

next would be 
- user system
- pic upload
   
-----
* 11/17 Fri
- Synced EC2 site with local site

next would be 
- add 'email', 'LinkedIn', 'Facebook" icons to the thumbnails
- user system
- pic upload
   
-----
* 11/16 Thu
- Mirrored app to localhost (should have done this from the very beginning)
- Sort students by lastname
- Added links to the bars; added hover effect in css for UX
- made an alternative homepage layout
![alt text](https://github.com/abigcleverdog/Web-app-deployment-EC2-001/blob/master/img/20171116_1_Capture.PNG "Project Snapshot")

next would be 
- add 'email', 'LinkedIn', 'Facebook" icons to the thumbnails
- user system
- pic upload
   
-----
* 11/15 Wed
- Added d3.js statistics to homepage
- current files backed up
![alt text](https://github.com/abigcleverdog/Web-app-deployment-EC2-001/blob/master/img/20171115_1_Capture.PNG "Project Snapshot")

next would be 
- add 'email', 'LinkedIn', 'Facebook" icons to the thumbnails
- change layout of homepage, the barchart can replace the left list once links are added, it can be placed on top of the student pics; 
- user system
- pic upload

-----
* 11/14 Tue
- Changed homepage imgs to thumbnail carosauls
![alt text](https://github.com/abigcleverdog/Web-app-deployment-EC2-001/blob/master/img/20171114_1_Capture.PNG "Project Snapshot")

next would be 
- add 'email', 'LinkedIn', 'Facebook" icons to the thumbnails
- add statistics to homepage and class of pages
-----
* 11/12 Sun
- added 'Class of' pages
- edited navbar; added a search form
- changed list to tumbnails
![alt text](https://github.com/abigcleverdog/Web-app-deployment-EC2-001/blob/master/img/20171112_1_Capture.PNG "Project Snapshot")

next would be 
- change the thumbnails to thumbnail carosauls
- add 'email', 'LinkedIn', 'Facebook" icons to the thumbnails
- add statistics to homepage and class of pages

-----
* 11/10 Fri
- relaunch a new mini instance on AWS-EC2 for "Our Graduates";
- best practice for set up is to move small steps and confirm frequently;
- configured the server to run Flask; tested accessibility of 'static';
- setup database
- created convert.py to extract data from a .csv file and transfer into the database;
- homepage set with database support:
![alt text](https://github.com/abigcleverdog/Web-app-deployment-EC2-001/blob/master/img/20171110_1_Capture.PNG "Project Snapshot")


-----
* 11/09 Thu
- launch a new mini instance on AWS-EC2 for "Our Graduates";
- set the server and the IP shows a Flask driven page;
- screwed up when using `url_for` to link `static` files; the server respond as 404; could nout figure out why;
-----
* 11/08 Wed
- built the login page. hard coded the `<input pattern="[A-Za-z0-9]+">` in html to prevent sql inj;;
![alt text](https://github.com/abigcleverdog/Web-app-deployment-EC2-001/blob/master/img/20171108_1_Capture.PNG "Project Snapshot")
- worked on the login/logout logics in the header.html
- built the login_required wraper
![alt text](https://github.com/abigcleverdog/Web-app-deployment-EC2-001/blob/master/img/20171108_2_Capture.PNG "Project Snapshot")
- next step will be updating other pages for login_session check.
- I need to put up a new project 'Student tracker' or maybe better named as 'Our Graduates' the Student table should contain firstName, middleName, lastName, classOf, url_linkedin, url_facebook, careerPath, etc.
-----
* 11/06 Mon
- Reset psql as old 'user' table does not contain a 'password' column;
- This was supposed to be doable via `ALTER TABLE user ADD COLUMN password varcahr(250)` However, it kept popping 'Syntax error' or 'Peer Authentification failed'
![alt text](https://github.com/abigcleverdog/Web-app-deployment-EC2-001/blob/master/img/20171106_1_Capture.PNG "Project Snapshot")
![alt text](https://github.com/abigcleverdog/Web-app-deployment-EC2-001/blob/master/img/20171106_2_Capture.PNG "Project Snapshot")
- Eventually I did 'DROP DATABASE' as postgres and reestablished the DB; It is probably not the best thing to to with real applications, I will look into it more when I have time; Just for now if I need to do something similar to a running app, better ways would be 1' add that COLUMN; 2' add a separate table to associate user_name with password; 3' reestablish DB with different name and save the original for back-up;
- Set up the registration page. 
Quite a bit of learning here: 
1. WTForms template and validators with regex, which is a defense against sql injection
![alt text](https://github.com/abigcleverdog/Web-app-deployment-EC2-001/blob/master/img/20171106_3_Capture.PNG "Project Snapshot")
2. Postgresql and MySQL use different syntax, my guess is that the returned query results are different too; as I am following a tutorial using MySQL, I need to review some psql and sqlalchemy (blue in the pic)
3. encrypt password with `sha256_crypt.encrypt(form.password.data)` (red in the pic)
![alt text](https://github.com/abigcleverdog/Web-app-deployment-EC2-001/blob/master/img/20171106_4_Capture.PNG "Project Snapshot")
- next step will be updating other pages for login_session check.
-----
* 11/04 Sat
- back deployed the app to local VM to edit pages before setting up security guard.
- 'add/edit/delete item' pages added.
- links on pages updated.

![alt text](https://github.com/abigcleverdog/Web-app-deployment-EC2-001/blob/master/img/20171104_1.gif "Project GIF")

- next step will be creating users management.
-----
* 11/02 Thu
- modified `__init__.py` routes for index, catlog, and item; the old way was working OK but only pass limited information to the rendered page. for instance, I passed `cat_name` and `length` to the page as I need those variables on the specific page. However, it seems to me now that if I pass the list `cats` and object `cat` and `item` to the page, I will be more efficient as when I need to change the layout and the information displaying, I can just work on the html templates to extract the info passed down instead of going back to the .py file to change the query or variables. This approach also makes my .py codes more consistent and readable.

- next step will be creating pages for displaying, adding, editing, and deleting an item...
- concern about the adding, editing and deleting page will be hostile attack from, well anyone found the link at this stage. I guess I may put them on a test page and disable the link when I am done working with them on a day. These pages may need to be hided until I set up the Oauth and security check.
-----
* 11/01 Wed
- modified `itempop.py` to `dbpop.py` to populate the database
- changed 'index.html' to be database-driven
- added @app.route in `__init__.py` for showing a catalog
- created 'items.html' template to display in a specific catalog
- updated both template with url_for hyperlinks
- tricks learned: `{{ var|length }}` `{% if %}` in .html; 
![alt text](https://github.com/abigcleverdog/Web-app-deployment-EC2-001/blob/master/img/20171101_1_Capture.PNG "Project Snapshot")
![alt text](https://github.com/abigcleverdog/Web-app-deployment-EC2-001/blob/master/img/20171101_2_Capture.PNG "Project Snapshot")
- next step will be creating pages for displaying, adding, editing, and deleting an item...
-----
* 10/31 Tue
- installed Postgresql, SqlAlchemy, psycopg2; `sudo apt-get install postgresql postgresql-contrib` `service postgresql status` `sudo -i -u postgres`(login as postgres, version 9.5.9) ` createuser -s pythonflask`(create pythonflask as superuser) `psql` `ALTER USER pythonflask WITH PASSWORD 'a password'` `\q` `exit` `sudo -u postgres createdb --owner=pythonflask itemcat`; `sudo apt-get install python-sqlalchemy`; `sudo apt-get install python-psycopg2`
![alt text](https://github.com/abigcleverdog/Web-app-deployment-EC2-001/blob/master/img/20171031_Capture.PNG "Project Snapshot")
- used old dbsetup.py to set up database structure (change `engine = create_engine('sqlite:///itemcat.db')` to `engine = create_engine(‘postgresql://catalog:catalog@localhost:5432/itemcat’)`); run it on the server.
![alt text](https://github.com/abigcleverdog/Web-app-deployment-EC2-001/blob/master/img/20171031_2_Capture.PNG "Project Snapshot")
- next step will be populating the database with mock cats and items and users ...
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
- `sudo apt-get install python-pip` `sudo pip install virtualenv` `sudo virtualenv venv` `source venv/bin/activate`-- establish and enter virtual environment ***need to be done in the /app/app folder
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
- `sudo apt-get update`, `sudo apt-get upgrade`, and `sudo apt-get autoremove` were used to keep linux packages current. `sudo timedatectl set-timezone America/New_York` `sudo apt-get install ntp`
- `sudo nano /etc/ssh/sshd_config`changed ssh timeout to be 2 hrs (30s*240) ClientAliveCountMax 240; ClientAliveInterval 30
- `sudo ufw default deny incoming`, `sudo ufw default allow outgoing`, `sudo ufw allow xxx` and `sudo ufw enable` were used to configure the firewall to only listen to SSH(port 22 and 2222), HTTP(port 80 and 8080), and NTP(port 123)
- `sudo apt-get install apache2 libapache2-mod-wsgi python-dev python`--install Apache2/Python mod-wsgi/Python
- `sudo a2enmod wsgi` --enable wsgi
- 'Apache2 Ubuntu Default Page' dispalyed on the IP.
