import cv2
import numpy
photo=cv2.imread('photo3.jpg')
photo1=cv2.imread('photo4.jpg')
photo.shape
cv2.imshow('hi',photo)
cv2.waitKey()
cv2.destroyAllWindows()
cv2.imshow('hi',photo1)
cv2.waitKey()
cv2.destroyAllWindows()
photo1.shape
image=photo[0:250,0:366]
image1=photo1[0:250,0:366]
result=numpy.concatenate([image1,image])
cv2.imshow('hi',result)
cv2.waitKey()
cv2.destroyAllWindows()
