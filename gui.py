# gui.py
import sys
import subprocess
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QLabel, QInputDialog, QMessageBox

class FaceApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Sistema de Reconocimiento Facial")
        self.setGeometry(100, 100, 300, 200)

        layout = QVBoxLayout()

        self.label = QLabel("Seleccione una opción:")
        layout.addWidget(self.label)

        self.reg_button = QPushButton("Registro")
        self.reg_button.clicked.connect(self.registrar_rostro)
        layout.addWidget(self.reg_button)

        self.acc_button = QPushButton("Acceso")
        self.acc_button.clicked.connect(self.verificar_acceso)
        layout.addWidget(self.acc_button)

        self.setLayout(layout)

    def registrar_rostro(self):
        name, ok = QInputDialog.getText(self, "Registro", "Ingrese el nombre del usuario:")
        if ok and name.strip():
            try:
                subprocess.run(["python", "encoding.py", name], check=True)
            except subprocess.CalledProcessError:
                QMessageBox.critical(self, "Error", "No se pudo ejecutar encoding.py")
        else:
            QMessageBox.warning(self, "Advertencia", "Nombre inválido.")

    def verificar_acceso(self):
        try:
            subprocess.run(["python", "face_id.py"], check=True)
        except subprocess.CalledProcessError:
            QMessageBox.critical(self, "Error", "No se pudo ejecutar face_id.py")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = FaceApp()
    window.show()
    sys.exit(app.exec_())