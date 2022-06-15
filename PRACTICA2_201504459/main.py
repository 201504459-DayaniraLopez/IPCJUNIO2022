import tkinter
from tkinter import *
from tkinter import Menu, filedialog
from functools import partial
from tkinter import messagebox as MessageBox
import xml.etree.ElementTree as ET
import GestorEmpleado


fuente = 'Lucida Sans Typewriter'
imgurl = 'img/fondo.png'
enviar = GestorEmpleado.GestrorEmpleado()
class Ventana():
    def __init__(self):
        self.window = Tk()
        self.window.title("GestorXML Administrar")
        self.window.geometry('500x300')
        #SE CREARA UNA BARRA DE MENU
        menu = Menu(self.window)
        self.SubMenu1 = Menu(menu, tearoff=0, font=(fuente, 10))
        self.SubMenu1.add_command(label='Cargar Archivo', command=self.Cargar)
        self.SubMenu1.add_command(label='Getión de empleado',command= partial(Ventana.Ventana_Empleado,self))
        self.SubMenu1.add_command(label='Getión de discos')
        self.SubMenu1.add_command(label='Reportes')
        menu.add_cascade(label='Inicio', menu=self.SubMenu1)
        self.window.config(menu=menu)
        # ubicacion de de fondo

        self.fondo = PhotoImage(file=imgurl)
        self.fondolabel = Label(self.window, image=self.fondo, borderwidth=5)
        self.fondolabel.place(x=0, y=0)

        self.Tamano = 20
        Titulo = Label(self.window, text="GESTOR DE EMPLEADO", fg='Blue', bg = None, font=(fuente, self.Tamano))
        Titulo.place(x=100, y=50)
        self.window.mainloop()

    def Cargar(self):
        self.ruta=StringVar()
        self.empleados = None
        self.discos = None
        self.ruta.set(filedialog.askopenfilename(initialdir="/", title="Selecione Archivo",filetypes=(("xml files", "*.xml"), ("todos los archivos", "*.*"))))


    def Ventana_Empleado(self):
        self.idEmpelado = StringVar()
        self.nombre = StringVar()
        self.salario = StringVar()
        self.puesto = StringVar()
        self.windowE= Toplevel()
        self.windowE.title("EMPLEADOS")
        self.windowE.geometry('600x300')
        self.windowE['bg'] = '#9DB7E1'

        Titulo = Label(self.windowE, text="GESTOR DE EMPLEADO", fg='White', bg='#9DB7E1', font=(fuente, self.Tamano))
        Titulo.place(x=150, y=5)

        self.Texto = Text(self.windowE)
        self.Texto.config(width=35, height=13, font=("Consolas", 8), selectbackground="blue")
        self.Texto.place(x=350, y=60)

        IdEmpleado = Label(self.windowE, text="ID Empleado", bg='#9DB7E1',font=(fuente, 11))
        IdEmpleado.place(x=35, y=50)

        txtID = tkinter.Entry(self.windowE, textvariable=self.idEmpelado)
        txtID.place(x=150, y=50)

        Buscar = Button(self.windowE, text="Buscar Empleado", font=(fuente, 10), bg='#AFC9D3', command=self.Buscar)
        Buscar.place(x=100, y=100)

        Nombre = Label(self.windowE, text="Nombre", bg='#9DB7E1', font=(fuente, 11))
        Nombre.place(x=35, y=150)

        txtNombre = tkinter.Entry(self.windowE, textvariable=self.nombre)
        txtNombre.place(x=150, y=150)

        Puesto = Label(self.windowE, text="Puesto", bg='#9DB7E1', font=(fuente, 11))
        Puesto.place(x=35, y=180)

        txtPuesto = tkinter.Entry(self.windowE, textvariable=self.puesto)
        txtPuesto.place(x=150, y=180)

        Salario = Label(self.windowE, text="Salario", bg='#9DB7E1', font=(fuente, 11))
        Salario.place(x=35, y=210)

        txtSalario = tkinter.Entry(self.windowE, textvariable=self.salario)
        txtSalario.place(x=150, y=210)

        Modificar = Button(self.windowE, text="Modificar Empleado", font=(fuente, 10), bg='#AFC9D3', command=self.ModificarE)
        Modificar.place(x=10, y=250)

        Eliminar = Button(self.windowE, text="Eliminar Empleado", font=(fuente, 10), bg='#AFC9D3',command=self.Eliminar)
        Eliminar.place(x=180, y=250)

        Vtodo = Button(self.windowE, text="Ver Todo", font=(fuente, 10), bg='#AFC9D3', command=self.Vertodo)
        Vtodo.place(x=350, y=250)
        GNuevo = Button(self.windowE, text="Generar Archivo", font=(fuente, 10), bg='#AFC9D3', command=self.GenerarNuevo)
        GNuevo.place(x=450, y=250)


    def Vertodo(self):
        self.Texto.delete('0.0',"end")
        texto = enviar.imprimir(self.ruta.get())
        self.Texto.insert('0.0', texto)

    def Buscar(self):
        datos = enviar.buscar(self.idEmpelado.get(),self.ruta.get())
        self.nombre.set(datos[0])
        self.puesto.set(datos[1])
        self.salario.set(datos[2])


    def ModificarE(self):
        enviar.modificar(self.idEmpelado.get(),self.ruta.get(),self.nombre.get(),self.puesto.get(),self.salario.get())


    def Eliminar(self):
        enviar.Eliminar(self.idEmpelado.get(),self.ruta.get())

    def GenerarNuevo(self):
        enviar.GenerarNuevo(self.ruta.get())





def main():
    Ventana()
    return 0
if __name__ == '__main__':
    main()


