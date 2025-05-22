from Models.ConexionDB import ConexionDB
from tkinter import messagebox

class Usuario():
    def __init__(self, nombre_usuario, password):
        self.nombre_usuario = nombre_usuario
        self.password = password
        self.rol = ""
        
    def iniciarsesion(self, nombre_usuario, password):
        miconexion = ConexionDB()
        miconexion.crearconexion()
        conm = miconexion.getconecction()
        cursor = conm.cursor()
        cursor.execute("select * from usuario")
        lista_usuario = cursor.fetchall ()
        for usuario in lista_usuario:
            if  (usuario [1] == nombre_usuario and usuario [2] == password):
                self.rol = usuario [3]
                if (self.rol == "admin"):
                    messagebox.showinfo ( "informacion", "acceso correcto Administrador ")
                    #crear obj y abrir menu del administrador
                else:    
                    messagebox.showinfo ( "informacion", "acceso correcto Digitador ")  
                
                miconexion.cerrarconexion()
                return 
        messagebox.showwarning ("advertencia", "el nombre de usuario o contraseña no exste, verifique e intente nuevamente")
        
        
        