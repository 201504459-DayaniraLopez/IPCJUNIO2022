#Creamos el objeto Carrito

class NodoCarrito:
    def __init__(self,numero):
        self.Numero = numero
        self.Siguiente = None


#Creamos el Objeto Cliente
class NodoCliente:
    def __init__(self,id,nombre,carrito):
        self.Id = id
        self.Nombre = nombre
        self.Carrito = carrito
        self.Siguiente = None

class NodoCaja:
    def __init__(self,nombre,carrito):
        self.Nombre = nombre
        self.Carrito = carrito
        self.Siguiente = None

#Creamos las Colas a utilizar

class PilaCarrito:
    def __init__(self):
        self.Inicio = None
        self.Final = None

    def Agregar(self,dato):
        #Preguntamos si la Cola esta vacia
        if self.Inicio is None:
            #si esta vacia agregamos el dato
            self.Inicio=self.Final = dato

        else:
            #si no esta vacia se recorre la cola hasta llegar al espacio vacio
            aux = dato
            aux.Siguiente = self.Inicio
            self.Inicio = dato


    def DesApilar(self):
        aux = self.Inicio
        if aux is not None:
            carrito = self.Inicio.Numero
            self.Inicio = aux.Siguiente
            return carrito

        elif aux == None:
            return 0

    def imprimir(self):
        cadena=""
        aux = self.Inicio
        if aux is not None:
            while aux is not None:
                if aux.Siguiente is not None:
                    cadena = cadena + "["+str(aux.Numero)+"],"
                else:
                    cadena = cadena+"["+str(aux.Numero)+"]"
                aux = aux.Siguiente
            return (cadena)
        else:
            return None

class ListaCliente:
    def __init__(self):
        self.Inicio = None
        self.Final = None

    def Agregar(self, cliente):
        # Preguntamos si la Cola esta vacia
        if self.Inicio is None:
            # si esta vacia agregamos el cliente
            self.Inicio = self.Final = cliente
            return ("Cliente Agregado Correctamente")
        else:
            # si no esta vacia se recorre la cola hasta llegar al espacio vacio
            aux = self.Final
            while aux.Siguiente is not None:
                aux = aux.Siguiente
            aux.Siguiente = cliente
            self.Final = cliente
            return ("Cliente Agregado Correctamente")

    def imprimir(self, opc):
        aux = self.Inicio
        cadena = ""
        while aux is not None:
                if opc == 1:
                    if aux is not None:
                        if aux.Siguiente != None:
                            print("\033[;32m"+"-----------------------------")
                            print("Id: " + str(aux.Id))
                            print("Nombre: "+aux.Nombre)
                            print("Carrito: "+str(aux.Carrito))
                        else :
                            print("\033[;32m"+"-----------------------------")
                            print("Id: " + str(aux.Id))
                            print("Nombre: " + aux.Nombre)
                            print("Carrito: " + str(aux.Carrito))
                            return("-----------------------------")
                    else:
                            return None
                elif opc ==2:
                    if aux is not None:
                        if aux.Siguiente != None:
                            cadena = cadena +aux.Nombre+"-"+str(aux.Carrito)+" , "
                        else:
                            cadena = cadena + aux.Nombre + "-" + str(aux.Carrito)
                        return (cadena)
                    else:
                            return None
                aux = aux.Siguiente

    def Buscar(self,id):
        aux = self.Inicio
        while aux is not None:
            if id == aux.Id:
                nombre = aux.Nombre
                carrito = aux.Carrito
                print(self.eliminar(id))
                return nombre,carrito

            aux = aux.Siguiente

    def eliminar(self, id):
        aux = self.Inicio
        if self.Inicio is None:
            return("La lista de clientes Esta Vacia")

        if self.Inicio.Id == id:
            self.Inicio = self.Inicio.Siguiente
            return("El cliente Elegido esta en Cola")

        while aux.Siguiente is not None:
            if aux.Siguiente.Id == id:
                break
            aux = aux.Siguiente
        if aux.Siguiente is None:
            return("El cliente no fue Econtrado")
        else:
           aux.Siguiente= aux.Siguiente.Siguiente
           return ("El cliente Elegido esta en Cola")


class ColaCaja:
        def __init__(self):
            self.Inicio = None
            self.Final = None

        def Agregar(self,cajacl):
            if self.Inicio is None:
                self.Inicio = self.Final = cajacl
                return ("Cliente en Caja")
            else:
                aux = self.Final
                while aux.Siguiente != None:
                    aux = aux.Siguiente
                aux.Siguiente = cajacl
                self.Final = cajacl
                return ("Cliente en Caja")

        def DesEncolar(self):
            aux = self.Inicio
            if aux is not None:
                carrito = self.Inicio.Carrito
                self.Inicio = aux.Siguiente
                print("\033[;40m"+"Cliente a sido Atendido, carrito "+str(carrito)+" en Pila")
                return carrito
            elif aux == None:
                print("\033[;31m"+"No hay Cliente en Caja")

        def imprimir(self):
            cadena = ""
            aux = self.Inicio
            if aux is not None:
                while aux is not None:
                    if aux.Siguiente is not None:
                        cadena = cadena + "[Carrito: " + str(aux.Carrito) + ", Nombre: "+str(aux.Nombre)+"]"
                    else:
                        cadena = cadena + "[Carrito: " + str(aux.Carrito) + ", Nombre: "+str(aux.Nombre)+"]"
                    aux = aux.Siguiente
                return (cadena)
            else:
                return None

