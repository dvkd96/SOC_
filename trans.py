import cv2 as cv
import numpy as np

img = cv.imread('Photos/b.png')

cv.imshow('B', img)

def translate(img, x, y):
    transMat = np.float32([[1,0,x],[0,1,y]])
    dimensions = (img.shape[1], img.shape[0])
    return cv.warpAffine(img, transMat, dimensions)
 

translated = translate(img, 300 ,-100)
cv.imshow('asd', translated)

def rotate(img, angle, rotPoint= None ):
    (height,width) = img.shape[:2]

    if rotPoint is None:
        rotPoint = (width/4, height/4)

        rotMat = cv.getRotationMatrix2D(rotPoint, angle ,1.0)
        dimensions = (width,height)
        return cv.warpAffine(img, rotMat, dimensions )
    
rotated = rotate(img, 45)
cv.imshow('asad', rotated)


flip = cv.flip(img, flipCode=-1)
cv.imshow('dasd', flip)


crop = img[200:400, 500:400]
cv.imshow('asdfv', crop)


        


cv.waitKey(0)