import cv2 as cv

img = cv.imread('Photos/d.jpg')
cv.imshow('d', img)

average = cv.blur(img, (7,7))
cv.imshow('asd', average )

gauss = cv.GaussianBlur(img, (7,7), 0)
cv.imshow('ssd', gauss)

median = cv.medianBlur(img, 3)
cv.imshow('asda', median)

bilateral = cv.bilateralFilter(img, 5, 15, 15)
cv.imshow('dfjsd', bilateral)



cv.waitKey(0)