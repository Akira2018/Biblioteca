
cd C:\Biblioteca

call venv\Scripts\activate
if errorlevel 1 (
    echo Falha ao ativar o ambiente virtual.
    exit /b
)

start "" http://192.168.0.203:8000/
python manage.py runserver 192.168.0.203:8000

rem Aguarda o usuário pressionar uma tecla antes de fechar o prompt de comando
pause
