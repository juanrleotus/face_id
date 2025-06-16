import cv2
import face_recognition
import serial
import os

# Configuración del puerto serial
arduino = serial.Serial('COM4', 9600)

#Cargar rostros conocidos
def load_known_faces():
    known_faces = {}
    for person in os.listdir('faces'):
        encodings = []
        for img in os.listdir(f"faces/{person}"):
            image_path = f"faces/{person}/{img}"
            image = face_recognition.load_image_file(image_path)
            enc = face_recognition.face_encodings(image)
            if enc:
                encodings.append(enc[0])
            else:
                print(f"[ADVERTENCIA] No se detectó ningún rostro en: {image_path}")
        if encodings:
            known_faces[person] = encodings
        else:
            print(f"[ERROR] No se cargaron rostros válidos para: {person}")
    return known_faces

def main():
    known_faces = load_known_faces()
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print("❌ No se pudo abrir la cámara.")
        return

    while True:
        ret, frame = cap.read()
        if not ret:
            print("❌ Error al leer frame de la cámara.")
            break
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        #Detección
        face_locations = face_recognition.face_locations(rgb_frame)
        face_encodings = face_recognition.face_encodings(rgb_frame, face_locations)

        for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
            for name, encodings in known_faces.items():
               matches = face_recognition.compare_faces(encodings, face_encoding, tolerance=0.5)
               if True in matches:
                   #Cuando la persona es reconocida o el rostro
                   cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)
                   cv2.putText(frame, name, (left, top - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)

                   arduino.write(b'O') # Envía 'O' para abrir puerta
               else:
                   # No lo reconoce
                   cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)
                   cv2.putText(frame, "DESCONOCIDO", (left, top - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
                   arduino.write(b'A')  # Activa la alarma

        cv2.imshow("Face ID Door", frame)
        if cv2.waitKey(1) == 27:
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
            main()