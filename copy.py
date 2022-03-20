import os
import shutil
path = "/Users/Arunjay/Desktop/"
print("Path before copying file")
print(os.listdir(path))
source = "/Users/Arunjay/Desktop/text.txt"
destination = "/Users/Arunjay/Desktop/textCopy.txt"
dest = shutil.copy(source,destination)
print("Path after copying file")
print(os.listdir(path))

