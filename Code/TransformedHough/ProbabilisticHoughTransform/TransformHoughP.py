import cv2
import numpy as np
 
# Cargamos la imagen
img = cv2.imread('carril.png')
cv2.imshow("original", img)

# Convertimos a escala de grises
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
cv2.imshow("grises", gray)
cv2.imwrite("grises.jpg", gray) 

# Aplicar suavizado Gaussiano
gauss = cv2.GaussianBlur(gray, (5,5), 0)
 
cv2.imshow("suavizado", gauss)
cv2.imwrite("suavizado.jpg", gauss) 

# Detectamos los bordes con Canny
edges = cv2.Canny(gauss,50,150,apertureSize = 3)
cv2.imshow("canny", edges)
cv2.imwrite("canny.jpg", gauss)

lines = cv2.HoughLinesP(edges,1,np.pi/180,100,minLineLength=100, maxLineGap=10)
for line in lines:
    x1, y1, x2, y2 = line[0]
    cv2.line(img,(x1,y1),(x2,y2),(0,255,0),1,cv2.LINE_AA)

cv2.imwrite('carrilProcesado.jpg',img)
cv2.imshow("Hough", img)

cv2.waitKey() 