import cv2
import face_recognition
import sys
import os

def register_face(name):
    cap = cv2.VideoCapture(0)
    face_dir = f"faces/{name}"  # corregido: carpeta 'faces' en plural
    os.makedirs(face_dir, exist_ok=True)

    count = 0
    print("[INFO] Presioná ESPACIO para capturar una imagen. ESC para cancelar.")

    while count < 5:
        ret, frame = cap.read()
        if not ret:
            print("[ERROR] No se pudo acceder a la cámara.")
            break

        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        face_locations = face_recognition.face_locations(rgb_frame)

        if face_locations:
            # Mostrar rostro detectado
            for (top, right, bottom, left) in face_locations:
                cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)

        cv2.putText(frame, f"Capturas: {count}/5", (10, 30),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 255), 2)
        cv2.imshow("Registro de rostro", frame)

        key = cv2.waitKey(1)

        if key == 27:  # ESC
            print("[INFO] Registro cancelado por el usuario.")
            break

        if key == 32 and face_locations:  # ESPACIO
            cv2.imwrite(f"{face_dir}/{count}.jpg", frame)
            print(f"[INFO] Imagen {count + 1} capturada.")
            count += 1

    cap.release()
    cv2.destroyAllWindows()

    if count == 5:
        print(f"[OK] Rostro de '{name}' registrado exitosamente.")
    else:
        print("[WARN] Registro incompleto. Algunas imágenes no fueron tomadas.")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Uso: python encoding.py <nombre>")
    else:
        name = sys.argv[1]
        register_face(name)
