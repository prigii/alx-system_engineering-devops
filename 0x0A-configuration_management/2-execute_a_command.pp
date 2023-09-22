# Kills a process name killmenow

exec { 'pkill killmenow':
  path     => '/usr/bin/pkill killmenow',
  command  => 'pkill killmenow',
  provider => shell,
  returns  => [0, 1],
}