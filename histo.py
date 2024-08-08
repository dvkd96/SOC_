import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

img = cv.imread('Photos/d.jpg')

re = cv.resize(img, (500,500), interpolation=cv.INTER_CUBIC)
cv.imshow('REs', re)

blank = np.zeros(re.shape[:2], dtype='uint8')

# gray = cv.cvtColor(re, cv.COLOR_BGR2GRAY)
# cv.imshow('sad', gray)

mask = cv.circle(blank, (img.shape[1]//2 ,img.shape[0]//2 ), 100, 255, -1)

masked = cv.bitwise_and(re,re, mask=mask)
cv.imshow('mask', masked)

# hist = cv.calcHist([re], [0],mask, [256], [0,256]  )

# plt.figure()
# plt.title('Grayhist' )
# plt.xlabel('bjfd')
# plt.ylabel('sd')
# plt.plot(hist)
# plt.xlim([0,256])
# plt.show()

colors = ('b', 'g', 'r')
plt.figure()
plt.title('Grayhist' )
plt.xlabel('bjfd')
plt.ylabel('sd')
for i,col in enumerate(colors):
    hist = cv.calcHist([img], [i],mask, [256], [0,256])
    plt.plot(hist, color=col)
    plt.xlim([0,256])

plt.show()


cv.waitKey(0)