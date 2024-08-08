import cv2 as cv
import numpy as np

canvas = np.zeros((600, 800,1) , np.uint8)

canvas.fill(255) 

x = 0
y = 0
drawing = False



def draw(event, current_x,current_y, flags , params):
  global x,y,drawing
  
  if event == cv.EVENT_LBUTTONDBLCLK :
    x = current_x
    y = current_y
    
    drawing = True
  elif event == cv.EVENT_MOUSEMOVE:
    if drawing:
      cv.line(canvas, (current_x, current_y), (x,y), 0, thickness=2)

      x,y = current_x,current_y
  elif event == cv.EVENT_LBUTTONUP :
    drawing = False
  

cv.imshow('dfsf', canvas)

cv.setMouseCallback('dfsf', draw)

while True:
  cv.imshow('dfsf', canvas)
  if cv.waitKey(1) & 0xFF == 27 : break

cv.destroyAllWindows()