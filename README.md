   # Overview
   This is a detailed note while deplying the "Item Catalog" app to AWS EC2 service.
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
