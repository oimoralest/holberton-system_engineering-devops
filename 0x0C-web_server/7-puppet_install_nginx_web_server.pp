# This manifest configures a web server with nginx
include stdlib
package { 'apache2.2-common':
  ensure => absent,
}
package {'nginx':
  ensure   => 'installed',
  provider => 'apt',
}
exec {'enable firewall for nginx':
  command => "ufw allow 'Nginx HTTP'",
  path    => '/usr/bin:/bin:/usr/sbin:/etc',
}
file {'create index.html':
  path    => '/var/www/html/index.html',
  content => 'Holberton School',
}
file_line {'append permanent redirection':
  path  => '/etc/nginx/sites-available/default',
  after => 'server_name -;',
  line  => '        rewrite ^/redirect_me/$ https://www.youtube.com/watch?v=QH2-TGUlwu4 permanent;',
}
exec {'start nginx':
  command => 'service nginx restart',
  path    => '/usr/bin:/bin:/usr/sbin:/etc',
}
