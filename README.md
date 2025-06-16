# face_id
reconocimiento facial para activar actuador arduino
Estrutura:
proyecto/
├── encoding.py
├── face_id.py
├── gui.py   ← Contendrá la interfaz completa (login + botones)
└── usuarios.json  ← Base de usuarios (para login)

requiere instalar:
pip install opencv
pip instal numpy
pip install cmake
pip install dlib --no-cache-dir
pip install face-recognition
pip download face-recognition --dest ./wheels
pip install pyqt5
pip install face-recognition
python -m pip install --upgrade pip setuptools wheel
pip install dlib
Instala Visual Studio Build Tools (compilador C++):

Descarga desde Visual Studio Build Tools.

Instala el workload "Desktop development with C++".

Instala Python 3.10 (recomendado por compatibilidad):

Versiones recientes de Python (3.11+) pueden tener problemas con dlib.
Instalá la versión oficial de CMake (correctamente)
Descargá desde: https://cmake.org/download/

Usá el instalador para Windows x64
ANDA RE BIEN EN UBUNTU

Durante la instalación, asegurate de marcar esta opción:

✔️ "Add CMake to the system PATH for all users"


