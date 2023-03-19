import numpy as np
import matplotlib
import cv2 as cv

#Para leer videos se usa la funcion cv.VideoCapture()
#cv.VideoCapture() toma como argumento un entero, que representa el
#puerto de WEBCAM

#cv.VideoCapture() tambien puede tomar como argumento la ruta del video
capture = cv.VideoCapture('Videos/yo3.mp4')

#Sin embargo, leer videos es distinto de leer imagenes
#En el caso de los videos, se usa un ciclo WHILE y se lee el video frame por frame

while True:
    #read() regresa el frame y un bool para decir si el frame fue leido
    isTrue, frame = capture.read()

    #Muestra el frame leido
    cv.imshow('Video',frame)

    #En este caso cv.waitKey(20) espera 20 milisegundo
    if cv.waitKey(20) & 0xFF==ord('a'):
        break


#Cierra el metodo de captura
capture.release() 

#Cierra las ventanas
cv.destroyAllWindows()
