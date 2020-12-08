# Change the /etc/ssh/ssh_config to connect to a server without typing a
# password
include stdlib
file_line {'Disable password authentication':
  path  => '/etc/ssh/ssh_config',
  line  => '    PasswordAuthentication no',
  match => '^*PasswordAuthentication*',
}
file_line {'add identity file':
  path  => '/etc/ssh/ssh_config',
  line  => '    IdentityFile ~/.ssh/holberton',
  match => '^*IdentityFile ~/.ssh/holberton*',
}
