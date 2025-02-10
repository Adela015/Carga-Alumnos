# Carga de alumnos
## Descripción

Este proyecto es un sistema básico de **CRUD** (Crear, Leer, Actualizar, Eliminar) para gestionar la carga de alumnos. Está desarrollado en Python utilizando la biblioteca tkinter para la interfaz gráfica y una base de datos SQLite para almacenar la información de los alumnos.

## Características principales

<img src="img/captura.png" alt="Interfaz principal" width="500">

**Agregar alumnos:** Permite ingresar nuevos alumnos con información como nombre, apellido, edad, curso, etc.

**Listar alumnos:** Muestra todos los alumnos registrados en la base de datos.

**Actualizar alumnos:** Permite modificar la información de un alumno existente.

**Eliminar alumnos:** Elimina un alumno de la base de datos.

**Interfaz gráfica:** Utiliza tkinter para una interfaz amigable y fácil de usar.

## Tecnologías usadas

- **Python**

## Estructura del proyecto

carga-alumnos/
├── build
    └── localpycs 
├── client/
    └── _init.py                    
    └── gui_app.py   
├── database/     
    └── alumnos.db
├── dist/
    └── carga-alumnos            
├── img/                    
│   └── cp-logo.ico 
├── model/
    └── _ init _.py
    ├── alumnos_dao.py
    └── _coexion_db.py  
├── carga-alumnos.spec
├── env/
    └── Include/
    └── Lib/
    └── Scripts/
    └── pyvenv.cfg
|       
└── README.md              

## Uso

**Agregar un alumno:**

- Completa los campos del formulario (nombre, apellido, edad, curso, etc.).

- Haz clic en el botón "Guardar" para agregar el alumno a la base de datos.

**Listar alumnos:**

- Haz clic en el botón "Listar" para ver todos los alumnos registrados en una tabla.

**Actualizar un alumno:**

- Selecciona un alumno de la lista.

- Modifica los campos que desees y haz clic en "Actualizar".

**Eliminar un alumno:**

- Selecciona un alumno de la lista.

- Haz clic en el botón "Eliminar" para borrarlo de la base de datos.

## Como correr el programa

**Desde cmder:**
- cd --ruta del proyecto--
- python -m venv env
- ls
- env\Scripts\activate
- cd carga-alumnos\
- ls
- python carga-alumnos.py

## Instalación de paquetes
**Instalar Paquetes (dentro de env 'ls'):**
- pip show pip
- python -m pip install --upgrade pip
- pip install pylint
- pip install autopep8

## Para la distribución 
- pip install pyinstaller : "Lo corro con" = pyi-makespec carga-alumnos.py --windowed
- Se crea un archivo llamado carga-alumnos
- Buscas dentro del a = Analysis --> datas[] y dentro del corchete pones:
-     datas=[('./img/*.ico', 'img'), ('./database/*.db', 'database')],
- Ejecutas en el cdmer : pyinstaller carga-alumnos.spec