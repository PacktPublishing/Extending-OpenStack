sudo yum update
sudo yum  install httpd httpd-devel -y
echo "LoadModule file_cache_module modules/mod_file_cache.so" >> /etc/httpd/conf.modules.d/00-cache.conf
echo "CacheFile /var/www/html/index.html /var/www/html/somefile.index" >> /etc/httpd/conf/httpd.conf
echo "MMapFile /var/www/html/index.html /var/www/html/somefile.index >> /etc/httpd/conf/httpd.conf"
systemctl restart httpd
sudo iptables -I INPUT 1 -p tcp -m tcp --dport 80 -j ACCEPT -m comment --comment "PacktPub WebServer HTTP Access - Public"
sudo iptables -I INPUT 2 -p tcp -m tcp --dport 443 -j ACCEPT -m comment --comment "PacktPub WebServer HTTP Access - Public"
sudo iptables -I INPUT 3 -p tcp -m tcp --dport 22  -s 10.1.0.0/16 -j ACCEPT -m comment --comment "PacktPub WebServer HTTP Access - Private"

