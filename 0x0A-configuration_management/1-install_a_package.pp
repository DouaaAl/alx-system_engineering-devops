# Ensure Python and pip are installed
class { 'python':
  pip    => true,
  ensure => installed,
}

# Install Flask version 2.1.0
python::pip { 'Flask':
  ensure => '2.1.0',
}
