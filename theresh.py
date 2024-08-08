import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

img = cv.imread('Photos/d.jpg')

re = cv.resize(img, (500,500), interpolation=cv.INTER_CUBIC)
cv.imshow('REs', re)
 
gray = cv.cvtColor(re, cv.COLOR_BGR2GRAY)
cv.imshow('sad', gray)

threshold,thresh = cv.threshold(gray, 150, 255, cv.THRESH_BINARY )
cv.imshow('thrws', thresh)

threshold,thresh_inv = cv.threshold(gray, 150, 255, cv.THRESH_BINARY_INV )
cv.imshow('thrws', thresh_inv)

adapt = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, 11, 3)
cv.imshow('dfaf', adapt)



cv.waitKey(0)