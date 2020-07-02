exec { 'apply_new_file_limits_sed':
  path    => ['/usr/bin', '/usr/sbin', '/bin'],
  command => '/bin/sed -i "s/ULIMIT=\"-n 15\"/ULIMIT=\"- Hn\"/" /etc/default/nginx && /etc/init.d/nginx restart',
}
