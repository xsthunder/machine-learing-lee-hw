#!/usr/bin/python3
from PIL import Image
FILE_NAME = 'westbrook.jpg'
SAVE_FILE_NAME = 'Q2.jpg'
img = Image.open(FILE_NAME)
(X,Y) = img.size
px = img.load()
for x in range(X):
    for y in range(Y):
        p =  px[x,y]
        (a,b,c) = p
        px[x,y] = (a//2, b//2, c//2);
img.save(SAVE_FILE_NAME)
