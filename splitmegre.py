import cv2 as cv
import numpy as np

img = cv.imread('Photos/d.jpg')
cv.imshow('d', img)

blank = np.zeros(img.shape[:2], dtype='uint8')

b,g,r = cv.split(img)

blue = cv.merge([b,blank,blank])
cv.imshow('bl',blue)



cv.imshow('b',b )
cv.imshow('g',g)
cv.imshow('r',r)

print(img.shape)
print(b.shape)
print(g.shape)
print(r.shape)

merged= cv.merge([b,g,r])
cv.imshow('merge', merged)





cv.waitKey(0)