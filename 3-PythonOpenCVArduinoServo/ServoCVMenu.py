# Importar librerías necesarias
from cvzone.SerialModule import SerialObject
import cv2

# Crear la clase de comunicación serial con Arduino
arduino = SerialObject("COM5")

# Registar en variables las rutas de las imágenes a utilizar
imgServo90 = cv2.imread("Resources/servo90Grados.jpg")
imgServo180 = cv2.imread("Resources/servo180Grados.jpg")

# Iterar el algoritmo del programa
while True:
    # PASO 1: Mostrar menú de opciones
    print("***** Menú de opciones *******")
    print("Para mover 90° el servo, ingrese 1")
    print("Para mover 180° el servo, ingrese 2")
    print("Para salir ingrese 0")
    print("******************************")

    # PASO 2: Pedir que el usuario ingrese una opción
    opcion = int(input("Ingrese una opción: "))

    # PASO 3: Decidir que operación realizar según la opción elegida
    if opcion == 1:
        # Enviar el valor 1 a Arduino
        arduino.sendData([90])
        # Mostrar la imagen de led encendido
        cv2.imshow("Image", imgServo90)
        # Esperar 1 s
        cv2.waitKey(1000)
    elif opcion == 2:
        # Enviar el valor 0 a Arduino
        arduino.sendData([180])
        # Mostrar la imagen de led apagado
        cv2.imshow("Image", imgServo180)
        cv2.waitKey(1000)
    elif opcion == 0:
        break;
    else:
        print("¡Ingresó una opción incorrecta! Vuelva a intentarlo")