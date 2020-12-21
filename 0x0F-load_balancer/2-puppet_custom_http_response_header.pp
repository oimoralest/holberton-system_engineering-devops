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
file_line { 'add_header':
  ensure => present,
  path   => '/etc/nginx/sites-available/default',
  after  => 'server_name _;',
  line   => 'add_header X-Served-By $hostname;',
}
service {'nginx':
  ensure  => running,
  require => Package['nginx'],
}
