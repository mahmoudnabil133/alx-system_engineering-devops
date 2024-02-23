# kill process

exec { 'pkill':
  path     => 'pkill killmenow',
  provider =>'shell'
}
