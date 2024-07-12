# File: 100-puppet_ssh_config.pp

file { '/etc/ssh/ssh_config':
  ensure  => present,
  content => template('ssh_config.erb'),
}

# Template file: ssh_config.erb
# This template ensures that Puppet correctly manages the ssh_config file
# by adding or modifying the necessary configurations.

Host *
  IdentityFile ~/.ssh/school
  PasswordAuthentication no

