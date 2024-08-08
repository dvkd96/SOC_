import cv2 as cv
import numpy as np

img = cv.imread('Photos/d.jpg')

re = cv.resize(img, (500,500), interpolation=cv.INTER_CUBIC)
cv.imshow('REs', re)


blank = np.zeros(re.shape[:2], dtype='uint8')

circle = cv.circle(blank.copy(), (re.shape[1]//2 + 45, re.shape[0]//2  + 45), 100, 255, -1 )
# cv.imshow('asmd', circle)

rectangle = cv.rectangle(blank.copy(), (30,30), (370,370), 255, -1)


weird = cv.bitwise_and(circle,rectangle)
cv.imshow('adsf', weird) 

masked= cv.bitwise_and(re, re, mask=weird)
cv.imshow('sad',masked)



    


cv.waitKey(0)