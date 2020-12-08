# Change the /etc/ssh/ssh_config to connect to a server without typing a
# password

exec {'ssh_config':
  command => 'echo "PasswordAuthentication no\nIdentityFile ~/.ssh/holberton\n" >> /etc/ssh/ssh_config',
  path    => '/usr/bin:/usr/sbin:/bin',
}
