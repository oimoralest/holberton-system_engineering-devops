# This manifest configures a web server with nginx

exec { 'Nginx header':
  command   => 'sudo apt-get update;
  sudo apt-get -y install nginx;
  sudo sed -i "/server_name _;/ a\ \ \ \ \ \ \ \ add_header X-Served-By $HOSTNAME;" /etc/nginx/sites-available/default;
  sudo service nginx restart',
  provider => 'shell',
}
