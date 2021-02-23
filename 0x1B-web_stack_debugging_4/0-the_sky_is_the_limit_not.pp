# This manifest fix the read limit for nginx
exec {'sed':
  command => 'sed -i "s/ULIMIT=\"-n 15\"/ULIMIT=\"-n 4000\"/" /etc/default/nginx',
  path    => '/bin/'
}
service {'nginx':
  ensure  => true,
  restart => 'service nginx restart'
}
