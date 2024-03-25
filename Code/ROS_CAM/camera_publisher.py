#!/usr/bin/env python3
# Con esta linea se le dice a ROS que este es un archivo fuente de Python

import rospy # Rospy nos permite usar ROS con Python
from sensor_msgs.msg import Image # Se importa Image ya que, se mandaran msj en forma de imagenes
import cv2 as cv # Aqui se importa OpenCV
from cv_bridge import CvBridge # cv_bridge es un paquete que convierte imagenes de OpenCV a un msj de imagen de ROS, y viceversa (OpenCV-ROS) 

pubNodeName = 'camera_sender' # Se crea el nombre del nodo publisher
topicName = 'video_topic' # Se crea el nombre del topico sobre el cual transmitiremos los msj de imagen, asegurando que sea el mismo en el subscriber

rospy. init_node(pubNodeName, anonymous=True)	# Inicialización del nodo
pub = rospy.Publisher(topicName,Image,queue_size=60) # Se crea un objeto publisher (Nombre del topico,tipo de msj,tamaño del buffer)
rate = rospy.Rate(30) # Tasa de transmision del msj a 30hz
cap = cv.VideoCapture(0) # Se crea un objeto para capturar video
if not cap.isOpened():
	print("Cannot open camera")
	exit()
#Bucle infinito que captura la imagen y la transmite a travez del topic
while not rospy.is_shutdown():
	ret, frame = cap.read() # Regresa dos valores, el primero es el booleano de exito/fracaso y el segundo es el frame actual
	if not ret: # Si todo esta OK, transmite
		print("Can't receive frame (stream end?). Exiting ...")
		break
	bridge = CvBridge() # Se crea el objeto CvBridge que se usara para convertir imagenes OpenCV a un msj de imagen de ROS
	rospy.loginfo('Video frame captured and published') # Imprime el mensaje
	image_message = bridge.cv2_to_imgmsg(frame) # Convierte de OpenCV a mensaje de imagen ROS
	pub.publish(image_message) # Publica la imagen convertida a traves del topico
	rate.sleep() # Se tiene una cierta espera de tiempo para asegurar que se alcance la velocidad de transmision especificada
