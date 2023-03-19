import cv2
import numpy as np
import imutils

# Define los colores del cubo
colores = {1: "Blanco", 2: "Azul", 3: "Rojo", 4: "Verde", 5: "Naranja", 6: "Amarillo"}

#Rango de color rojo
bajo_rojo = np.array([0,50,50]) 
alto_rojo = np.array([10,255,255])

bajo_verde = np.array([100,50,50])
alto_verde = np.array([140,255,255])

bajo_naranja = np.array([40,50,50])
alto_naranja = np.array([10,255,255])

lower_red = np.array([0,50,50])
upper_red = np.array([10,255,255])

lower_red = np.array([0,50,50])
upper_red = np.array([10,255,255])

lower_red = np.array([0,50,50])
upper_red = np.array([10,255,255])

#Captura de video
captura = cv2.VideoCapture(1)

#Ajustar resolucion de camara
captura.set(3, 1080)
captura.set(4, 720)

#Loop principal
while True:

    #Guardar el frame de captura
    isTrue, frame = captura.read()
    #Voltear el frame horizontalmente
    espejo = cv2.flip(frame,1)

    cv2.imshow("Webcam",espejo)

    #Si se presiona 'q', salir
    if cv2.waitKey(20) & 0xFF==ord('q'):
        break