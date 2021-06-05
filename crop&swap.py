import cv2
photo=cv2.imread('photo.png')
photo1=cv2.imread('photo1.png')
nphoto1=cv2.imread('photo.png')
cphoto=photo[20:300,150:350]
cphoto1=photo1[20:200,150:300]
cv2.imshow('hi',photo)
cv2.waitKey()
cv2.destroyAllWindows()
cv2.imshow('hi',photo1)
cv2.waitKey()
cv2.destroyAllWindows()
for i in range(40,301):
    for j in range(150,350):
            photo[i][j]=photo1[i][j]
cv2.imshow('hi',photo)
cv2.waitKey()
cv2.destroyAllWindows()

for i in range(0,250):
    for j in range(150,350):
            photo1[i][j]=nphoto1[i][j]
cv2.imshow('hi',photo1)
cv2.waitKey()
cv2.destroyAllWindows()
