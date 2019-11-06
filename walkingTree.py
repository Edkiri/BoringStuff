import os

for folderName, subfolders, filesnames in os.walk('delicius'):
  print('The current folder is ' + folderName)

  for subfolder in subfolders:
    print('SUBFOLDER OF ' + folderName + ': ' + subfolder)

  for filename in filesnames:
    print('FILE INSIDE ' + folderName + ': ' + filename)

  print('')