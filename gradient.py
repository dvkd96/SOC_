import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

img = cv.imread('Photos/d.jpg')

re = cv.resize(img, (500,500), interpolation=cv.INTER_CUBIC)
cv.imshow('REs', re)

gray = cv.cvtColor(re, cv.COLOR_BGR2GRAY)
cv.imshow('gray', gray)

lap = cv.Laplacian(gray, cv.CV_64F)
lap= np.uint8(np.absolute(lap))
cv.imshow('kdcf',lap)

sobelx = cv.Sobel(gray, cv.CV_64F, 1 ,0)
sobely = cv.Sobel(gray, cv.CV_64F, 0 ,1)
combine = cv.bitwise_and(sobelx, sobely)

cv.imshow('da', sobelx)
cv.imshow('da', sobely)
cv.imshow('dsf', combine)

canny = cv.Canny(gray, 150, 175)
cv.imshow('dsf', canny)



cv.waitKey(0)