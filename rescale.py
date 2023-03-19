import numpy as np
import matplotlib
import cv2 as cv


#Para reescalar una foto, se puede hacer una funcion
def rescaleFrame (frame, scale = 0.50) :

    #La funcion, shape[] regresa el tamaño de una imagen
    #shape[0] regresa height
    #shape[1] regresa width
    height = int (frame.shape[0] * scale)
    width = int (frame.shape[1] * scale)

    #Se puede guardar las nuevas dimensiones en una tupla
    dimensions = height,width

    return cv.resize(frame,dimensions, interpolation=cv.INTER_AREA)




capture = cv.VideoCapture('Videos/yo3.mp4')
while True:
    isTrue, frame = capture.read()

    frame_resized = rescaleFrame(frame)

    cv.imshow('Video',frame)
    cv.imshow('Video Resized',frame_resized)

    if cv.waitKey(20) & 0xFF==ord('a'):
        break


