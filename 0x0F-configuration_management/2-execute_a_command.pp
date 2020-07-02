# Using Puppet, create a manifest that kills a process named killmenow
exec { 'puppet command name':
  command => "pkill -f 'killmenow'",
  path    => ['/bin/', '/sbin/', '/usr/bin', '/usr/sbin'],
  returns => ['',' '],
}
