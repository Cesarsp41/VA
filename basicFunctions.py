import numpy as np
import matplotlib
import cv2 as cv


img = cv.imread('Images/yo1.jpg')
cv.imshow("Yo",img)


#------------------------- Funciones basicas de OpenCV ------------------------#

#-------GRAYSCALE-------#
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("Gray",gray)
#-----------------------#


#-------BLUR-------#
blur = cv.GaussianBlur(img, (9,9), cv.BORDER_DEFAULT)
cv.imshow("Blur",blur)
#-----------------------#


#-------EDGE CASCADE-------#
canny = cv.Canny(img, 125, 175)
cv.imshow("Canny",canny)
#Para obtener bordes menos definidos, aplicar un blur a la imagen
#--------------------------#


#---------RESIZE---------#
resized = cv.resize(img, (500,500))
cv.imshow("Resized",resized)
#------------------------#



cv.waitKey(0)