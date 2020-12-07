# This manifest runs pkill command to kill killmenow process

exec {'pkill':
  command => 'pkill -f killmenow',
  path    => '/usr/bin:/usr/sbin:/bin'
}
