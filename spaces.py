import cv2 as cv
import matplotlib.pyplot as  plt


img = cv.imread('Photos/d.jpg')
cv.imshow("d", img)

plt.imshow(img)
plt.show()

# gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# cv.imshow('as', gray)

# hsv = cv.cvtColor(img , cv.COLOR_BGR2HSV)
# cv.imshow('dshu', hsv)

# lab = cv.cvtColor(img, cv.COLOR_BGR2LAB)
# cv.imshow('as', lab)

rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)
cv.imshow('Rgb', rgb)

plt.imshow(rgb)
plt.show()

#hsv to 

cv.waitKey(0)