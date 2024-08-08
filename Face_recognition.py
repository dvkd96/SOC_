import numpy as np
import cv2 as cv

haar_cascade = cv.CascadeClassifier('haar.xml')

people = ['dhoni', 'virat']
# features = np.load('features.npy', allow_pickle=True)
# labels = np.load('labels.npy')

face_recognizer = cv.face.LBPHFaceRecognizer_create()
face_recognizer.read('face_trained.yml')

img = cv.imread(r'D:\Pictures\face\virat\1.jpg')

# re = cv.resize(img, (500,500), interpolation=cv.INTER_CUBIC)
# cv.imshow('REs', re)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# cv.imshow('Pehvjh', gray)

faces_rect = haar_cascade.detectMultiScale(gray, 1.1, 4)

for (x,y,w,z) in faces_rect:
    faces_roi = gray[y:y+z,x:x+w]

    label, confidence = face_recognizer.predict(faces_roi)
    print(f'Label = {people[label]} with a confidence of {confidence}')

    cv.putText(img, str(people[label]), (20,20), cv.FONT_HERSHEY_COMPLEX, 1.0, (0,255,0), thickness=2)
    cv.rectangle(img, (x,y), (x+w,y+z), (0,255,0), thickness=2)

cv.imshow('erjhg', img)

cv.waitKey(0)

