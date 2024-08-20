# Ensure pip3 is installed (only if necessary)
package { 'python3-pip':
  ensure => installed,
}

# Install Flask version 2.1.0 using pip3
exec { 'install-flask':
  command => '/usr/bin/pip3 install Flask==2.1.0',
  path    => ['/usr/bin', '/usr/local/bin'],
  unless  => '/usr/bin/pip3 show Flask | grep -q "Version: 2.1.0"',
  notify  => Exec['verify-flask'],
}

# Optionally verify installation
exec { 'verify-flask':
  command => '/usr/bin/pip3 show Flask',
  path    => ['/usr/bin', '/usr/local/bin'],
  refreshonly => true,
}
