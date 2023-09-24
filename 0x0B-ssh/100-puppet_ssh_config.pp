# puppet script that sets up ssh config file to allow connectivity without password
include stdlib

file_line { 'Turn off passwd auth':
  path => '/etc/ssh/sshd_config',  # Path to the SSH server configuration file
  line => 'PasswordAuthentication no',
}

file_line { 'Declare identity file':
  path => '/etc/ssh/ssh_config',  # Path to the SSH client configuration file
  line => 'IdentityFile ~/.ssh/school',
}
