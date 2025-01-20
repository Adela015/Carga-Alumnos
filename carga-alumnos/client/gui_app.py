import tkinter as tk

##-------------- BARRA DEL MENÚ ---------------##
def barra_menu(root):
    barra_menu = tk.Menu(root)
    root.config(menu = barra_menu, width = 300, height = 300)
    
    menu_inicio = tk.Menu(barra_menu, tearoff = 0)
    barra_menu.add_cascade(label = 'Inicio', menu = menu_inicio)
    
    menu_inicio.add_command(label = 'Crear Registro en DB')
    menu_inicio.add_command(label = 'Eliminar Registro en DB')
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
        self.campos_carga_alumnos()

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

        self.entry_nombre = tk.Entry(self)
        self.entry_nombre.config(width = 50, state = 'disabled', font = ('Arial', 12, 'bold'))
        self.entry_nombre.grid(row = 0, column = 1, padx = 10, pady = 10, columnspan = 2)

        self.entry_domicilio = tk.Entry(self)
        self.entry_domicilio.config(width = 50, state = 'disabled', font = ('Arial', 12, 'bold'))
        self.entry_domicilio.grid(row = 1, column = 1, padx = 10, pady = 1, columnspan = 20)
        
        self.entry_dni = tk.Entry(self)
        self.entry_dni.config(width = 50, state = 'disabled', font = ('Arial', 12, 'bold'))
        self.entry_dni.grid(row = 2, column = 1, padx = 10, pady = 10, columnspan = 2)
        
        self.entry_edad = tk.Entry(self)
        self.entry_edad.config(width = 50, state = 'disabled', font = ('Arial', 12, 'bold'))
        self.entry_edad.grid(row = 3, column = 1, padx = 10, pady = 10, columnspan = 2)
        
##------------- BOTONES --------------##

        self.boton_nuevo = tk.Button(self, text = "Nuevo")
        self.boton_nuevo.config(width = 20, font = ('Arial', 12,'bold'), fg = 'white', bd = 0, bg = '#FF69B4', cursor = 'hand2', activebackground = '#FFB6C1', activeforeground = "white", relief = 'flat')
        self.boton_nuevo.grid(row = 4, column = 0, padx = 10, pady = 10)
        
        self.boton_guardar = tk.Button(self, text = "Guardar")
        self.boton_guardar.config(width = 20, font = ('Arial', 12,'bold'), fg = 'white', bd = 0, bg = '#FF1493', cursor = 'hand2', activebackground = '#FF69B4', activeforeground = "white", relief = 'flat')
        self.boton_guardar.grid(row = 4, column = 1, padx = 10, pady = 10)
        
        self.boton_cancelar = tk.Button(self, text = "Cancelar")
        self.boton_cancelar.config(width = 20, font = ('Arial', 12,'bold'), fg = 'white', bd = 0, bg = '#C71585', cursor = 'hand2', activebackground = '#FF1493', activeforeground = "white", relief = 'flat')
        self.boton_cancelar.grid(row = 4, column = 2, padx = 10, pady = 10)
        