import cv2
import cv2 as cv

img = cv.imread('1.jpg')

cv.imshow('testing img', img)


# To display Image
window_name = 'Grayscale Conversion OpenCV'
cv2.namedWindow(window_name, cv2.WINDOW_NORMAL)
cv2.imshow(window_name, img)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv.waitKey(0)
