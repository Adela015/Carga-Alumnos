import tkinter as tk
from tkinter import ttk
from model.alumnos_dao import crear_tabla, borrar_tabla
from model.alumnos_dao import Alumno, guardar, listar, editar
from tkinter import messagebox

##-------------- BARRA DEL MENÚ ---------------##
def barra_menu(root):
    barra_menu = tk.Menu(root)
    root.config(menu = barra_menu, width = 300, height = 300)
    
    menu_inicio = tk.Menu(barra_menu, tearoff = 0)
    barra_menu.add_cascade(label = 'Inicio', menu = menu_inicio)
    
    menu_inicio.add_command(label = 'Crear Registro en DB', command = crear_tabla)
    menu_inicio.add_command(label = 'Eliminar Registro en DB', command = borrar_tabla)
    menu_inicio.add_command(label = 'Salir', command = root.destroy)

    barra_menu.add_cascade(label = 'Consultas',)
    barra_menu.add_cascade(label = 'Configuración',)
    barra_menu.add_cascade(label = 'Ayuda',)


##-------- CONFIGURACIÓN DE LA APLICACIÓN ---------##
class Frame(tk.Frame):

    def __init__(self, root = None):
        super().__init__(root, width = 680, height = 520)
        self.root = root
        self.pack()
        self.config()

        self.id_alumnos = None
        self.campos_carga_alumnos()
        self.deshabilitar_campos()
        self.tabla_alumnos()

##----------- LABELS DE CADA CAMPO ------------##

    def campos_carga_alumnos(self):

        self.label_nombre = tk.Label(self, text = 'Nombre: ')
        self.label_nombre.config(font = ('Arial', 12, 'bold'))
        self.label_nombre.grid(row = 0, column = 0, padx = 10, pady = 10)
        
        self.label_domicilio = tk.Label(self, text = 'Domicilio: ')
        self.label_domicilio.config(font = ('Arial', 12, 'bold'))
        self.label_domicilio.grid(row = 1, column = 0, padx = 10, pady = 10)
        
        self.label_dni = tk.Label(self, text = 'D.N.I: ')
        self.label_dni.config(font = ('Arial', 12, 'bold'))
        self.label_dni.grid(row = 2, column = 0, padx = 10, pady = 10)
        
        self.label_edad = tk.Label(self, text = 'Edad: ')
        self.label_edad.config(font = ('Arial', 12, 'bold'))
        self.label_edad.grid(row = 3, column = 0, padx = 10, pady = 10)
        
##----------- ENTRYS DE CADA CAMPO ------------##

        self.mi_nombre = tk.StringVar()
        self.entry_nombre = tk.Entry(self, textvariable = self.mi_nombre)
        self.entry_nombre.config(width = 50, font = ('Arial', 12))
        self.entry_nombre.grid(row = 0, column = 1, padx = 10, pady = 10, columnspan = 2)

        self.mi_domicilio = tk.StringVar()
        self.entry_domicilio = tk.Entry(self, textvariable = self.mi_domicilio)
        self.entry_domicilio.config(width = 50, font = ('Arial', 12))
        self.entry_domicilio.grid(row = 1, column = 1, padx = 10, pady = 1, columnspan = 2)
        
        self.mi_dni = tk.StringVar()
        self.entry_dni = tk.Entry(self, textvariable = self.mi_dni)
        self.entry_dni.config(width = 50, font = ('Arial', 12))
        self.entry_dni.grid(row = 2, column = 1, padx = 10, pady = 10, columnspan = 2)
        
        self.mi_edad = tk.StringVar()
        self.entry_edad = tk.Entry(self, textvariable = self.mi_edad)
        self.entry_edad.config(width = 50, font = ('Arial', 12))
        self.entry_edad.grid(row = 3, column = 1, padx = 10, pady = 10, columnspan = 2)
        
##------------- BOTONES INICIO --------------##

        self.boton_nuevo = tk.Button(self, text = "Nuevo", command = self.habilitar_campos)
        self.boton_nuevo.config(width = 20, font = ('Arial', 12,'bold'), fg = 'white', bd = 0, bg = '#FF69B4', cursor = 'hand2', activebackground = '#FFB6C1', activeforeground = "white", relief = 'flat')
        self.boton_nuevo.grid(row = 4, column = 0, padx = 10, pady = 10)
        
        self.boton_guardar = tk.Button(self, text = "Guardar", command = self.guardar_datos)
        self.boton_guardar.config(width = 20, font = ('Arial', 12,'bold'), fg = 'white', bd = 0, bg = '#FF1493', cursor = 'hand2', activebackground = '#FF69B4', activeforeground = "white", relief = 'flat')
        self.boton_guardar.grid(row = 4, column = 1, padx = 10, pady = 10)
        
        self.boton_cancelar = tk.Button(self, text = "Cancelar", command = self.deshabilitar_campos)
        self.boton_cancelar.config(width = 20, font = ('Arial', 12,'bold'), fg = 'white', bd = 0, bg = '#C71585', cursor = 'hand2', activebackground = '#FF1493', activeforeground = "white", relief = 'flat')
        self.boton_cancelar.grid(row = 4, column = 2, padx = 10, pady = 10)
        
##-------------- HABILITAR CAMPOS Y BOTONES ------------##
        
    def habilitar_campos(self):
        
        self.mi_nombre.set('')
        self.mi_domicilio.set('')
        self.mi_dni.set('')
        self.mi_edad.set('')
        
        self.entry_nombre.config(state = 'normal')
        self.entry_domicilio.config(state = 'normal')
        self.entry_dni.config(state = 'normal')
        self.entry_edad.config(state = 'normal')
        
        self.boton_guardar.config(state = 'normal')
        self.boton_cancelar.config(state = 'normal')
    
##------------- DESHABILITAR CAMPOS Y BOTONES ------------##
    
    def deshabilitar_campos(self):
        
        self.mi_nombre.set('')
        self.mi_domicilio.set('')
        self.mi_dni.set('')
        self.mi_edad.set('')
        
        self.entry_nombre.config(state = 'disabled')
        self.entry_domicilio.config(state = 'disabled')
        self.entry_dni.config(state = 'disabled')
        self.entry_edad.config(state = 'disabled')
        
        self.boton_guardar.config(state = 'disabled')
        self.boton_cancelar.config(state = 'disabled')
        
##-------------- GUARDAR DATOS EN TABLA --------------##

    def guardar_datos(self):
        alumno = Alumno(
            self.mi_nombre.get(),
            self.mi_domicilio.get(),
            self.mi_dni.get(),
            self.mi_edad.get()
        )
        
        if self.id_alumnos is None:
            guardar(alumno)
            
        else:
            editar(alumno, self.id_alumno)
            
        self.tabla_alumnos()
        
        self.deshabilitar_campos()

##---------------- TABLA ALUMNOS ------------------##
    def tabla_alumnos(self):
        self.lista_alumnos = listar()
        self.lista_alumnos.reverse()
        
        self.tabla = ttk.Treeview(self, columns = ('Nombre Completo', 'Domicilio', 'DNI', 'Edad') )
        self.tabla.grid(row = 5, column = 0, columnspan = 5, sticky = 'nse')

        self.scroll = ttk.Scrollbar(self, orient = 'vertical', command =self.tabla.yview)
        self.scroll.grid(row = 5, column = 5, sticky = 'nse')
        self.tabla.configure(yscrollcommand = self.scroll.set)
        
        self.tabla.heading('#1', text = 'Nombre Completo')
        self.tabla.heading('#2', text = 'Domicilio')
        self.tabla.heading('#3', text = 'DNI')
        self.tabla.heading('#4', text = 'Edad')

        for a in self.lista_alumnos:
            self.tabla.insert('', 0, text = a[0],
                values = (a[1], a[2], a[3], a[4]))
        
##-------------------- BOTONES FINAL ---------------------##

        self.boton_editar = tk.Button(self, text = "Editar", command = self.editar_datos)
        self.boton_editar.config(width = 20, font = ('Arial', 12,'bold'), fg = 'white', bd = 0, bg = '#40E0D0', cursor = 'hand2', activebackground = '#7FFFD4', activeforeground = "white", relief = 'flat')
        self.boton_editar.grid(row = 6, column = 0, padx = 10, pady = 10)
        
        self.boton_eliminar = tk.Button(self, text = "Eliminar")
        self.boton_eliminar.config(width = 20, font = ('Arial', 12,'bold'), fg = 'white', bd = 0, bg = '#C70039', cursor = 'hand2', activebackground = '#FF0000', activeforeground = "white", relief = 'flat')
        self.boton_eliminar.grid(row = 6, column = 1, padx = 10, pady = 10)
            
##------------------ EDITAR DATOS BASE DE DATOS --------------##

    def editar_datos(self):
        try: 
            self.id_alumnos = self.tabla.item(self.tabla.selection())['text']
            
            self.nombre_alumno = self.tabla.item(
                self.tabla.selection())['values'][0]
            
            self.domicilio_alumno = self.tabla.item( 
                self.tabla.selection())['values'][1]
            
            self.dni_alumno = self.tabla.item( 
                self.tabla.selection())['values'][2]
            
            self.edad_alumno = self.tabla.item( 
                self.tabla.selection())['values'][3]
            
            self.habilitar_campos()
            
            self.entry_nombre.insert(0, self.nombre_alumno)
            self.entry_domicilio.insert(0, self.domicilio_alumno)
            self.entry_dni.insert(0, self.dni_alumno)
            self.entry_edad.insert(0, self.edad_alumno)
            
            
        except:  # noqa: E722
            titulo = 'Edición de datos'
            mensaje = 'No ha seleccionado ningún registro'
            messagebox.showerror(titulo, mensaje)