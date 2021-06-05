import numpy
import cv2
x=numpy.zeros((600,600,3))
cv2.imshow('hi',x)
cv2.waitKey()
cv2.destroyAllWindows()
for i in range(100,105):
    for j in range(100,500):
        x[i][j]=[255,255,255]
for i in range(300,305):
    for j in range(100,500):
        x[i][j]=[255,255,255]
for i in range(100,300):
    for j in range(100,103):
        x[i][j]=[255,255,255]
for i in range(100,305):
    for j in range(500,505):
        x[i][j]=[255,255,255]
    
for i in range(305,390):
    for j in range(300,330):
            x[i][j]=[255,255,255]
for i in range(390,400):
    for j in range(250,380):
          x[i][j]=[255,255,255]
cv2.imshow('hi',x)
cv2.waitKey()
cv2.destroyAllWindows()
