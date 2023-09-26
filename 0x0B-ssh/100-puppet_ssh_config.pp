# puppet script that sets up ssh config file to allow connectivity without password
# Changes SSH config file
exec { '/etc/ssh/ssh_config':
  path    => '/bin',
  command => 'echo "    IdentityFile ~/.ssh/school    PasswordAuthentication no" >> /etc/ssh/ssh_config',
  provider => 'shell',
}
