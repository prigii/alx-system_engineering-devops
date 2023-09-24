# Kills a process name killmenow

exec { 'pkill killmenow':
  path     => '/usr/bin/killmenow',
  command  => 'pkill killmenow',
  provider => shell,
  returns  => [0, 1],
}