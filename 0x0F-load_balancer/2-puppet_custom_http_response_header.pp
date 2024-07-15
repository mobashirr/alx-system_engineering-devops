# 2-puppet_custom_http_response_header.pp

# Ensure the Nginx package is installed
package { 'nginx':
  ensure => installed,
}

# Ensure the Nginx service is running and enabled to start at boot
service { 'nginx':
  ensure     => running,
  enable     => true,
  require    => Package['nginx'],
}

# Configure Nginx to add the custom HTTP header
file { '/etc/nginx/sites-available/default':
  ensure  => file,
  content => template('nginx/default.erb'),
  require => Package['nginx'],
  notify  => Service['nginx'],
}

# Template for the Nginx default site configuration
file { '/etc/puppetlabs/code/environments/production/modules/nginx/templates/default.erb':
  ensure  => file,
  content => @("EOF"),
server {
    listen 80 default_server;
    listen [::]:80 default_server;

    server_name _;

    root /var/www/html;

    index index.html index.htm index.nginx-debian.html;

    location / {
        try_files \$uri \$uri/ =404;
        add_header X-Served-By \$hostname;
    }
}
| EOF
}
