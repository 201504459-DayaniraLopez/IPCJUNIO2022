
import Colas as cola
class Interfaz():

   def __init__(self):
      pilas= cola.PilaCarrito()
      lcliente = cola.ListaCliente()
      lcaja = cola.ColaCaja()
      n= 1
      id =0
      opc =0
      while opc!=5:
         print("\033[;36m" + "┌-------------------------------┐")
         print("|       Tienda la Barata        |")
         print("|_______________________________|")
         print("|1. Ingresar Datos              |")
         print("|2. Nuevo Cliente               |")
         print("|3. Ver Cliente                 |")
         print("|4. Caja registradora           |")
         print("|5. Visualizar Datos            |")
         print("|6. Salir                       |")
         print("└-------------------------------┘")
         op = int(input("\033[1;35m" + "Ingrear la opcion Elegida: "))
         if op>0 and op ==1:
            numero= int(input("Ingrese el Numero de Carritos:" ))
            if numero >0:
               while n <= numero:
                  pilas.Agregar(cola.NodoCarrito(n))
                  n = n + 1
            else:
               print("\033[;31m" + "Ingrese un Numero Mayor a 0")
         elif op>0 and op ==2:
            id = id+1
            if pilas.imprimir() is not None:
               print("Carritos Disponibles: "+pilas.imprimir())
               nombre= input("\033[1;35m" +"Ingresar Nombre del Cliente: ")
               carrito =int(pilas.DesApilar())
               lcliente.Agregar(cola.NodoCliente(id, nombre, carrito))
            else:
               print("\033[;31m" + "No hay carritos Disponibles")
         elif op>0 and op ==3:
            opc = 0
            print("\033[;36m" + "┌---------------------------┐")
            print("|1. Pagar                   |")
            print("|2. Regresar                |")
            print("└---------------------------┘")
            opc = int(input("\033[1;35m" +"Ingrese la Opcion Elegiga: "))
            if opc > 0 and opc <3:
               if opc == 1:
                  print("Lista de Clientes")
                  if lcliente.imprimir(opc) is not None:
                        idcliente = int(input("\033[1;35m"+"Ingrese el id del cliente que Pagara: "))
                        datosl = lcliente.Buscar(idcliente)
                        if datosl != None:
                           lcaja.Agregar(cola.NodoCaja(str(datosl[0]),datosl[1]))
                        else:
                           print("\033[1;31m" +"Cliente elegido no Existe")
                  else:
                     print("\033[;31m" + "No hay Clientes")

               elif opc == 2:
                  break
            else:
               print("\033[;31m" + "Ingrese una opcion Disponible")

         elif op > 0 and op == 4:
            print("Cola en Caja")

            print(lcaja.imprimir())
            opx=0
            while opx !=2:
               print("\033[;36m" + "┌---------------------------┐")
               print("|1. Avanzar                 |")
               print("|2. Regresar                |")
               print("└---------------------------┘")
               opx = int(input("Elija una Opcion: "))
               if opx > 0 and opx < 3:
                  if opx == 1 and lcaja.imprimir() is not None:
                     carrito = lcaja.DesEncolar()
                     pilas.Agregar(cola.NodoCarrito(carrito))
                  elif lcaja.imprimir() is None:
                     print("\033[;31m" + "No hay Clientes en Caja")
                     break
               else:
                  print("\033[;31m" + "Ingrese una opcion Disponible")

         elif op > 0 and op == 5:
            if pilas.imprimir() is not None:
                print("\033[;40m" +"Pila Carritos: "+pilas.imprimir())
            else:
               print("\033[;40m" + "Pila Carritos: No Hay Carritos en Cola")
            if lcliente.imprimir(2) is not None:
                print("Lista de Clientes: "+lcliente.imprimir(2))
            else:
               print("\033[;40m" + "Lista de Clientes: No hay Clientes en La lista")
            if lcaja.imprimir() is not None:
               print(+"\033[;32m"+"Cola Caja: "+ lcaja.imprimir())
            else:
               print("\033[;40m" + "Cola Caja: No hay Clientes en la Cola")

         elif op > 0 and op == 6:
            exit()
         else:
            print("\033[;31m" + "La opcion Elegida No es correcta ")
def main():
   Interfaz()

if __name__ == '__main__':
   main()
