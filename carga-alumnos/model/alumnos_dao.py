from model.conexion_db import ConexionDB
from tkinter import messagebox

##----------------- CREAR TABLA DB ---------------##

def crear_tabla():
    conexion = ConexionDB()
    
    sql = '''
    CREATE TABLE alumnos(
        id_alumnos INTEGER,
        nombre VARCHAR(100),
        domicilio VARCHAR(100),
        dni VARCHAR(100),
        edad VARCHAR(10),
        PRIMARY KEY(id_alumnos AUTOINCREMENT)    
    )'''
    try :
        conexion.cursor.execute(sql)
        conexion.cerrar()
        titulo = 'Crear Registro'
        mensaje = 'Se creo la tabla en la base de datos'
        messagebox.showinfo(titulo, mensaje)
        
    except:  # noqa: E722
        titulo = 'Crear Registro'
        mensaje = 'La tabla ya está creada'
        messagebox.showwarning(titulo, mensaje)

##-------------------- BORRAR TABLA DB -----------------##  
  
def borrar_tabla():
    conexion = ConexionDB()
    
    sql = 'DROP TABLE alumnos'
    
    try:
        conexion.cursor.execute(sql)
        conexion.cerrar()
        titulo = 'Borrar Registro'
        mensaje = 'Se creo la tabla en la base de datos se borró con éxito'
        messagebox.showinfo(titulo, mensaje)
    
    except:  # noqa: E722
        titulo = 'Crear Registro'
        mensaje = 'No hay tabla para borrar'
        messagebox.showerror(titulo, mensaje)
        
class Alumno: 
    def __init__(self, nombre, domicilio, dni, edad):
        self.id_alumnos = None
        self.nombre = nombre
        self.domicilio = domicilio
        self.dni = dni
        self.edad = edad
        
    def __str__(self):
        return f'Alumnos[{self.nombre}, {self.domicilio}, {self.dni}, {self.edad}]'
    
##----------------------- CONEXIÓN BASE DE DATOS ALUMNOS -------------------##

def guardar(alumno):
    conexion = ConexionDB()
    
    sql = f"""INSERT INTO alumnos (nombre, domicilio, dni, edad)
    VALUES('{alumno.nombre}', '{alumno.domicilio}', '{alumno.dni}', '{alumno.edad}')"""
    
    try:
        conexion.cursor.execute(sql)
        conexion.cerrar()
    
    except:  # noqa: E722
        titulo = 'Conexion al Registro'
        mensaje = 'La tabla de alumnos no está creada en la Base de Datos'
        messagebox.showerror(titulo, mensaje)
        
def listar():
    conexion = ConexionDB()
    
    lista_alumnos = []
    sql = 'SELECT * FROM alumnos'
    
    try: 
        conexion.cursor.execute(sql)
        lista_alumnos = conexion.cursor.fetchall()
        conexion.cerrar()
        
    except:  # noqa: E722
        titulo = 'Conexion al Registro'
        mensaje = 'Crea la tabla en la Base de Datos'
        messagebox.showwarning(titulo, mensaje) 
        
    return lista_alumnos

##------------------ EDITAR BASE DE DATOS -----------------## 

def editar(alumno, id_alumnos):
        conexion = ConexionDB()
        
        sql = f"""UPDATE alumnos
        SET nombre = '{alumno.nombre}', domicilio = '{alumno.domicilio}',
        dni = '{alumno.dni}', edad = '{alumno.edad}'
        WHERE id_alumnos = '{id_alumnos}'
        """
        
        try: 
            conexion.cursor.execute(sql)
            conexion.cerrar()
            
        except:  # noqa: E722
            titulo = 'Edición de datos'
            mensaje = 'No se a podido editar este registro'
            messagebox.showerror(titulo, mensaje)

##------------------ ELIMINAR BASE DE DATOS -----------------## 
        
def eliminar(id_alumnos):
    conexion = ConexionDB()
    sql = f'DELETE FROM alumnos WHERE id_alumnos = {id_alumnos}'
    
    try:
        conexion.cursor.execute(sql)
        conexion.cerrar()
    
    except:  # noqa: E722
        titulo = 'Eliminar Datos'
        mensaje = 'No se pudo eliminar el registro'
        messagebox.showerror(titulo, mensaje)
            