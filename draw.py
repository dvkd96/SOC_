import cv2 as cv 
import numpy as np

blank = np.zeros((500,500,3), dtype='uint8')
cv.imshow('Blank', blank)

#paint
blank[200:300, 400:500] = 0,0,255
cv.imshow('Green', blank)

cv.rectangle(blank, (0,0),   (50,250), (0,0,255), thickness=-1)
cv.imshow('RECC', blank)

#circle
cv.circle(blank, (250,50), 40, (255,0,255), 3)
cv.imshow('circle', blank)

cv.line(blank, (50,250), (250,300) , (0,255,255))
cv.imshow('line', blank)

cv.putText(blank, 'dnya', (250,225), cv.FONT_HERSHEY_SCRIPT_COMPLEX , 1.0, (0,255,0) , thickness=1 ,)
cv.imshow('text', blank)


# img = cv.imread('Photos/a.png')
#    #  # cv.imshow('A', img)

cv.waitKey(100000)