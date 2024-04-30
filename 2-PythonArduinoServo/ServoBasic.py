from cvzone.SerialModule import SerialObject

arduino = SerialObject("COM5")

while True:
    arduino.sendData([180])