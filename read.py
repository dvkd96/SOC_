import cv2 as cv
 
#img = cv.imread('Photos/b.png')
#cv.imshow('B', img)

capture = cv.VideoCapture('Videos/v.MP4')

while True:
    isTrue, frame = capture.read()
    cv.imshow('V', frame)

    if cv.waitKey(20) & 0xFF==ord('d'):
      break

capture.release()
cv.destroyAllWindows()

