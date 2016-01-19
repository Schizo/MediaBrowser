
rootPath = "/Users/chavez/Desktop/Projects/Elementsbrowser/prototyping/python/Categories/"
inputFile = 'Cloth/A002C002_140913_FPS120'

import os
head, tail = os.path.split(inputFile)
print tail

fullPathOnDisc = rootPath + inputFile + "/Thumbnails/" + tail + ".0001.jpg"
print fullPathOnDisc


        #pathlist = ['Cloth/A002C001_140913_FPS120/Thumbnails/A002C001_140913_FPS120.0001.jpg', 


x = ['Fire', 'Alice']
mystring = '/'.join(x[1:])
print mystring


