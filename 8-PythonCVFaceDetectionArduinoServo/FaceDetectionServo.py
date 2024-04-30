import cv2
import mediapipe as mp
import serial

com = serial.Serial('COM6', 9600, write_timeout=10)

detector = mp.solutions.face_detection
dibujo = mp.solutions.drawing_utils

cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

with detector.FaceDetection(min_detection_confidence=0,75) as rostros:
    while True:
        ret, frame = cap.read()
        frame = cv2.flip(frame, 1)
        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        resultado = rostros.process(rgb)

        if resultado.detections is not None:
            for rostro in resultado.detections:
                dibujo.draw_detection(frame, rostro, dibujo.DrawingSpec(color=(0, 255, 0),))
