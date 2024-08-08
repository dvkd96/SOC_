import cv2 as cv
import numpy as np

blank = np.zeros((400,400), dtype = 'uint8')

rec = cv.rectangle(blank.copy(), (30,30), (300,300), 255, -1 )
circle = cv.circle(blank.copy(), (200,200), 175,255,-1)

cv.imshow('re', rec)
cv.imshow('sd', circle)

bitwise_and = cv.bitwise_and(rec, circle)
cv.imshow('asd', bitwise_and)

_or = cv.bitwise_or(rec, circle)
cv.imshow('or', _or)

_xor = cv.bitwise_xor(rec, circle)
cv.imshow('xor', _xor)

_not = cv.bitwise_not(rec, circle)
cv.imshow('not', _not)



cv.waitKey(0)