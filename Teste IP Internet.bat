
cd C:\Biblioteca

call venv\Scripts\activate
if errorlevel 1 (
    echo Falha ao ativar o ambiente virtual.
    exit /b
)

start "" http://189.35.254.184:8000/
python manage.py runserver 189.35.254.184:8000 --insecure

rem Aguarda o usuário pressionar uma tecla antes de fechar o prompt de comando
pause
