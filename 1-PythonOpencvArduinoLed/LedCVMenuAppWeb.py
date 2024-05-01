import streamlit as st
from cvzone.SerialModule import SerialObject
import cv2

# Crear la clase de comunicación serial con Arduino
arduino = SerialObject("COM5")

# Registar en variables las rutas de las imágenes a utilizar
imgLedOn = cv2.imread("Resources\Pin13On.jpg")
imgLedOff = cv2.imread("Resources\Pin13Off.jpg")

# Mostrar el título de la aplicación
st.title("Control de Led con Arduino")

# PASO 1: Mostrar menú de opciones en la interfaz web
st.title("Menú de opciones")
opcion = st.radio("Seleccione una opción:",
                    ["Encender el Led", "Apagar el Led", "Salir"])

# PASO 2: Decidir que operación realizar según la opción elegida
if opcion == "Encender el Led":
    # Enviar el valor 1 a Arduino
    arduino.sendData([1])
    # Mostrar la imagen de led encendido
    st.image(imgLedOn, caption='Led Encendido', use_column_width=True)
elif opcion == "Apagar el Led":
    # Enviar el valor 0 a Arduino
    arduino.sendData([0])
    # Mostrar la imagen de led apagado
    st.image(imgLedOff, caption='Led Apagado', use_column_width=True)
elif opcion == "Salir":
    pass
