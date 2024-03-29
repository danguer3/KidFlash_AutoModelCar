#!/usr/bin/env python3
# Con esta linea se le dice a ROS que este es un archivo fuente de Python

import rospy # Rospy nos permite usar ROS con Python
from sensor_msgs.msg import Image # Se importa Image ya que, se mandaran msj en forma de imagenes
import cv2 as cv # Aqui se importa OpenCV
from cv_bridge import CvBridge # cv_bridge es un paquete que convierte imagenes de OpenCV a un msj de imagen de ROS, y vicevers (OpenCV-ROS) 

subNodeName='camera_receiver' # Se crea el nombre del nodo subscriber
topicName='video_topic'# Se tiene que asegurar que el nombre sea el mismo que se uso en el archivo del publisher

def callbackFunction (message) : # Esta funcion de devolucion que se llama cada que llega un mensaje
	bridge = CvBridge() # Se crea el objeto CvBridge
	rospy.loginfo("received a video message/frame") # Imprime el mensaje
	convertedFrameBackToCV = bridge.imgmsg_to_cv2(message) # Convierte de mensaje de imagen ROS a OpenCV
	cv.imshow("camera",convertedFrameBackToCV) # Muestra la imagen en la pantalla
	cv.waitKey(1) # Se espera un tiempo de un milisegundo

rospy.init_node(subNodeName, anonymous=True) # Inicialización del nodo
# anonymous = True, significa que un número aleatorio será añadido al nombre del nodo subscriber
rospy.Subscriber(topicName,Image, callbackFunction) # Aqui se Suscribe, (nombre del topico, tipo de msj que recive, nombre de la funcion de devolución)
rospy.spin() #Aqui hacemos al código "spin", lo que hace que se ejecute infinitamente, a menos que precionemos Ctrl+c
cv.destroyAllWindows() # Destruye todas las ventanas
