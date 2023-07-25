import fnmatch2 as fnmatch
import os
 
rootPath = '/'
# replace .mp3 with file extension you want to find
pattern = '*.mp3'
 
for root, dirs, files in os.walk(rootPath):
    for filename in fnmatch.filter(files, pattern):
        print( os.path.join(root, filename))
