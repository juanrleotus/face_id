@echo off
REM =========================================
REM Reiniciar entorno virtual y reinstalar face-recognition
REM Autor: - Juan Rojas
REM =========================================

echo.
echo 🔄 Eliminando entorno virtual existente...
rmdir /s /q .venv

echo.
echo 🆕 Creando nuevo entorno virtual (.venv)...
python -m venv .venv

echo.
echo ✅ Activando entorno virtual...
call .venv\Scripts\activate.bat

echo.
echo ⬆️ Actualizando pip, setuptools y wheel...
pip install --upgrade pip setuptools wheel

echo.
echo 📦 Instalando face-recognition...
pip install face-recognition

echo.
echo ✅ Listo. Entorno reinstalado correctamente.
pause
