import numpy as np
import matplotlib
import cv2 as cv

#La forma de leer imagenes en OpenCV es a traves del uso de
# cv.imread()
#El metodo cv.imread() toma como argumento la RUTA de una imagen
#El metodo cv.imread() regresa una imagen como una MATRIZ de pixeles
img = cv.imread('Images/Shark.jpg')

#Es posible mostrar una imagen (Matriz de pixeles) usando cv.imshow()
#cv.imshow() muestra la imagen en una nueva VENTANA
#cv.imshow() toma como argumentos: el nombre de la ventana y la matriz
cv.imshow('Imagen Prueba', img)

#cv.imshow() sin embargo, se cerrara al instante, por lo que necesitamos
#esperar a que se presione una tecla
cv.waitKey(0)
