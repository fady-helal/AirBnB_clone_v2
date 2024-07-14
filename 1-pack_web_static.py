#!/usr/bin/python3
# generates a .tgz archive from the contents of the web_static folder
from datetime import datetime
from fabric import Connection
from fabric.api import *
def do_pack():
  time = datetime.now()
  archive = 'web_static_' + time.strftime("%Y%m%d%H%M%S") + '.' + 'tgz'
  local('mkdir -p versions')
  my_arc = local('tar -czvf versions/{} web_static'.format(archive))
  if my_arc is not None:
    return archive
  else:
    return None