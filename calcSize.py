#! python3

# Calcula el tamaño de una carpeta

import os 
totalSize = 0

path = '/home/eduardok/Downloads'

for filename in os.listdir(path):
  totalSize += os.path.getsize(os.path.join(path, filename))
  print(filename)
  print(" ")

print(totalSize)