import os

def init():
  base_dir = 'watched'

  if not os.path.isdir(base_dir):
    print('Directory not found') 
    return
