# Using Puppet, create a file in /tmp
file { '/tmp/codeschool':
  path    => '/tmp/codeschool',
  mode    => '0744',
  owner   => 'www-data',
  group   => 'www-data',
  content => 'I love Puppet'
}
