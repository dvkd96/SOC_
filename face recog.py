import os
import cv2 as cv
import numpy as np

people = ['dhoni', 'virat']

DIR  = (r'D:\Pictures\face')


haar_cascade = cv.CascadeClassifier('haar.xml')

features = []
labels = []

def create_train():
    for person in people:
        path = os.path.join(DIR, person)
        label = people.index(person)

        for img in os.listdir(path):
            img_path = os.path.join(path,img)
            
            img_array = cv.imread(img_path)

            if img_array is None:
              continue 
           
            gray = cv.cvtColor(img_array, cv.COLOR_BGR2GRAY)

            faces_rect = haar_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=4)

            for(x,y,w,z) in faces_rect:
                faces_roi = gray[y:y+z, x:x+w]
                features.append(faces_roi)
                labels.append(label)

create_train()
print ('training ==-f=wrf=-')


features= np.array(features, dtype = 'object')
labels = np.array(labels)

# print(f'length fea ={len(features)}')
# print(f'length lab ={len(labels)}')

recog = cv.face.LBPHFaceRecognizer_create()

recog.train(features, labels)

recog.save('face_trained.yml')

np.save('features.npy', features)
np.save('labels.npy', labels)
