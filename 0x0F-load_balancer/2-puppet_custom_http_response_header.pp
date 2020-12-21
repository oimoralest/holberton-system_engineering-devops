# This manifest configures a web server with nginx

package { 'nginx':
  ensure => installed,
}

file { 'index.html':
  content => 'Holberton School',
  path    => '/var/www/html/index.html'
}
file_line { 'append instruction':
  ensure => present,
  path   => '/etc/nginx/sites-available/default',
  after  => 'server_name _;',
  line   => 'rewrite ^/redirect_me https://www.youtube.com/watch?v=QH2-TGUlwu4 permanent;',
}
exec { 'append http header':
  command => 'sed -i "/server_name _;/ a\ \ \ \ \ \ \ \ add_header X-Served-By $HOSTNAME;" /etc/nginx/sites-available/defaul',
  path    => '/usr/bin:/usr/sbin:/bin',
}
service {'nginx':
  ensure  => running,
  require => Package['nginx'],
}
