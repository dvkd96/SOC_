import cv2 as cv

img = cv.imread('Photos/g2.jpg')

re = cv.resize(img, (500,500), interpolation=cv.INTER_BITS)
cv.imshow('REs', re)

gray = cv.cvtColor(re, cv.COLOR_BGR2GRAY)
cv.imshow('daf',gray)

haar_cascade = cv.CascadeClassifier('haar.xml')

faces_rect = haar_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=1)
print(f'no = {len(faces_rect)}')

for (x,y,w,h) in faces_rect:
    cv.rectangle(re, (x,y), (x+w,y+h), (0,255,0), thickness = 2)

cv.imshow('sdf', re )




cv.waitKey(0)