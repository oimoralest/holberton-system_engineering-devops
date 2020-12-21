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
file_line { 'append instruction':
  ensure => present,
  path   => '/etc/nginx/sites-available/default',
  after  => 'server_name _;',
  line   => 'error_page 404  /custom_404.html;',
}
file { 'custom_404.html':
  content => "Ceci n'est pas une page"
  path    => '/var/www/html/custom_404.html'
}
file_line { 'add_header':
  ensure => present,
  path   => '/etc/nginx/sites-available/default',
  after  => 'server_name _;',
  line   => 'add_header X-Served-By $HOSTNAME;',
}
service {'nginx':
  ensure  => running,
  require => Package['nginx'],
}
