import tkinter as tk
from client.gui_app import Frame, barra_menu

def main():
    root = tk.Tk()
    root.title('Carga Alumnos')
    root.iconbitmap('img/cp-logo.ico')
    root.resizable(1,1)
    barra_menu(root)
    
    app = Frame(root = root)
    
    root.mainloop()
    
if __name__ == '__main__':
    main()