import cv2 as cv

img = cv.imread('Photos/a.png')
cv.imshow('A', img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('gray', gray)

blur = cv.GaussianBlur(img, (3,7), cv.BORDER_ISOLATED)
cv.imshow('Blur', blur)  

edge = cv.Canny(blur, 125, 175)
cv.imshow('canny', edge)

dila = cv.dilate(edge, (3,3), iterations=1)
cv.imshow('dila', dila)

eroded = cv.erode(dila, (4,4) , iterations=1)
cv.imshow("ero", eroded)

resize = cv.resize(img, (750,500), interpolation=cv.INTER_CUBIC)
cv.imshow('REs', resize)

cropped = img[150:250, 300:400]
cv.imshow('crop', cropped)




cv.waitKey(0)