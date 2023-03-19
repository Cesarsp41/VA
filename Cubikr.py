import cv2 as cv
import numpy as np

# Define los colores del cubo
colores = {1: "Blanco", 2: "Azul", 3: "Rojo", 4: "Verde", 5: "Naranja", 6: "Amarillo"}

# Define los ROIs
rois = [(50, 85), (150, 85), (250, 85),
        (50, 185), (150, 185), (250, 185),
        (50, 285), (150, 285), (250, 285)]

# Inicializa la webcam
cap = cv.VideoCapture(1)

while True:
    #Lee un frame de la webcam
    isTrue, frame = cap.read()

    #Convierte ese frame a escala de grises
    gris = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

    #Dibujar los ROIs en el frame
    for x, y in rois:
        #           Matriz   Cmnz       Final        Color      Grosor
        cv.rectangle(frame,  (x,y),  (x+60, y+60), (0,255,0),  thickness=2)
    
    #Muestra el frame 
    espejo = cv.flip(frame, 1)
    cv.imshow("Webcam",espejo)
    
    #Si se presiona 'q', salir
    if cv.waitKey(20) & 0xFF==ord('q'):
        break

    #Si se presiona 's', escanear
    if cv.waitKey(20) & 0xFF==ord('s'):

        #Inicializar el array para guardar los colores
        cube = []
        #Extraer colores de los ROI
        for x, y in rois:
            roi = gris[y:y+60, x:x+60]
            _, thresh = cv.threshold(roi, 100,285, cv.THRESH_BINARY_INV)
            cnts, _ = cv.findContours(thresh, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
            if len(cnts) > 0:

                #Encontrar el contorno del color
                c = max(cnts, key = cv.contourArea)
                #Encontrar el centroide del contorno
                M = cv.moments(c)
                cx = int(M['m10'] / M['m00'])
                cy = int(M['m01'] / M['m00'])
                #Determinar el color del sticker
                color = gris[y+cy, x+cx]
                #Mapear el color al arreglo cube[]
                if color > 200:
                    cube.append(1)
                elif color > 150:
                    cube.append(2)
                elif color > 100:
                    cube.append(3)
                elif color > 50:
                    cube.append(4)
                elif color > 0:
                    cube.append(5)
                else:
                    cube.append(6)

        #Imprimir los colores del array
        print([colores[c] for c in cube])

#Apagar camara y cerrar ventanas
cap.release()
cv.destroyAllWindows()



