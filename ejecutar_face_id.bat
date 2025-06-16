@echo off
REM =========================================
REM Activar entorno y ejecutar tu script principal
REM Autor: - Juan Rojas
REM =========================================

echo 🔐 Activando entorno virtual...
call .venv\Scripts\activate.bat

echo 🚀 face_id.py
REM Reemplazá "main.py" con el nombre real de tu archivo si es distinto
python main.py

echo ✅ Ejecución finalizada.
pause
