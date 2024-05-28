# Navegar a la raíz del proyecto


# Crear el entorno virtual
python -m venv env

# Activar el entorno virtual (Windows)
.\env\Scripts\activate

# Activar el entorno virtual (Linux/MacOS)
source env/bin/activate

# Instalar dependencias
pip install -r requirements.txt

# Ejecutar la aplicación FastAPI
uvicorn app.main:app --reload