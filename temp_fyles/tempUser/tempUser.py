from shutil import rmtree
from os import makedirs


def tempUser(username):
  del_dir = f'C:\\Users\\{username}\\AppData\\Local\\Temp'
  rmtree(del_dir, ignore_errors=True)
  if del_dir == False:
    makedirs(del_dir)
