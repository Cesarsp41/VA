import cv2 as cv
import numpy as np

#Existen dos maneras de dibujar en una imagen:
# 1-Dibujar directamente en la imagen
# 2-Crear una imagen en blanco


#--------------------------------------------------------------------------------------------------
#                                 Crear una imagen en blanco (negro)

#La linea de abajo crea: Un array de ceros, tipo entero. Tamaño: 500 x 500 de 3 canales
blank = np.zeros((500,500,3), dtype='uint8')
cv.imshow('Zeros',blank)

#--------------------------------------------------------------------------------------------------


#--------------------------------------------------------------------------------------------------
#                                 Como se pinta la imagen?

#1- Asignando valores RGB al array de 0's (Se pinta todo el cuadro)
blank[:] = 255,255,255
cv.imshow('Color plano',blank)

#2- Dibujando figuras
#2.1 Rectangulo
#             matriz        Comienzo       Final            Color(BGR)        Grosor, se puede rellenar cv.FILLED
cv.rectangle (  blank,      (0,0),      (250,250),          (0,0,255),          thickness=2)
cv.imshow('Rectangulo dibujado',blank)


#2.2 Circulo
#           matriz             Centro       Radio          Color BGR           Grosor   
cv.circle (  blank,          (250,250),      100,          (0,0,255),          thickness=2)
cv.imshow('Circulo dibujado',blank)


#2.3 Linea
#           matriz           Comienzo               Final             ColorBGR          Grosor         
cv.line (   blank,           (10,10),            (320,490),          (255,0,0),         thickness=2)
cv.imshow('Linea dibujada',blank)


#2.4 Texto
#cv.putText()

#--------------------------------------------------------------------------------------------------


cv.waitKey(0)

