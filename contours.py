import cv2 as cv
import numpy as np
 
img = cv.imread('Photos/b.png')
cv.imshow('b', img)

blank = np.zeros(img.shape, dtype='uint8')
cv.imshow('blank', blank)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY )
cv.imshow('asdasd', gray)

# canny = cv.Canny(img, 125, 175)
# cv.imshow('canny', canny)

ret, thresh = cv.threshold(gray,125,255, cv.THRESH_BINARY)
cv.imshow=('sd', thresh)

contours, heirarchies = cv.findContours(thresh, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)
print(f'{len(contours)} contour(s) found!')

cv.drawContours(blank, contours, -1, (0,0,255), 1)
cv.imshow('afdfa', blank)

cv.waitKey(0)