import cv2 as cv

image = cv.imread('wonder.jpg')
cv.imshow('wonder women',image)
# cv.waitKey(0)

gray_image = cv.cvtColor(image,cv.COLOR_BGR2GRAY)
cv.imshow("Wonder1",gray_image)
# cv.waitKey(0)

inverted_img = 255-gray_image
cv.imshow("Inverted",inverted_img)
# cv.waitKey(0)

blur_img = cv.GaussianBlur(inverted_img,(21,21),0)

inverted_blur = 255-blur_img
pencil_sketch = cv.divide(gray_image,inverted_blur,scale=256.0)
cv.imshow("Sketch",pencil_sketch)
cv.waitKey(0)
