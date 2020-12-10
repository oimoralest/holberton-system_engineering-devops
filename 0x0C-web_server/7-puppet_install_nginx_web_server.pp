# This manifest configures a web server with nginx
include stdlib

package {'nginx':
  ensure => 'installed',
}
file {'create index.html':
  path    => '/var/www/html/index.html',
  content => 'Holberton School',
}
file_line {'append permanent redirection':
  ensure => present,
  path   => '/etc/nginx/sites-available/default',
  after  => 'server_name _;',
  line   => '       rewrite ^/redirect_me/$ https://www.youtube.com/watch?v=QH2-TGUlwu4 permanent;',
}
service {'nginx':
  ensure  => running,
  require => Package['nginx'],
}
