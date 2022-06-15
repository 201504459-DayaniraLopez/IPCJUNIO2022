import xml.etree.ElementTree as ET
class GestrorEmpleado:

    def imprimir(self,ruta):
        archivo_xml = ET.parse(ruta)
        raiz = archivo_xml.getroot()
        i=0
        cadena = ""
        if raiz.tag == "empresa":
            for padre in raiz:
                while i <= len(padre)-1:
                    cadena = cadena + "\nID: " + str(padre[i].get('id')) + "\nNombre: "+ str(padre[i][0].text)+"\nPuesto: " + str(padre[i][1].text)+"\nSalario: " + str(padre[i][2].text)
                    i=i+1
                i = 0
            return cadena
        elif  raiz.tag == "catalog":
            return "No hay informacion"

    def buscar(self,id,ruta):
        archivo_xml = ET.parse(ruta)
        raiz = archivo_xml.getroot()
        i = 0
        if raiz.tag == "empresa":
            for padre in raiz:
                while i <= len(padre) - 1:
                    if id== padre[i].get('id'):
                        nombre = str(padre[i][0].text)
                        puesto = str(padre[i][1].text)
                        salario =str(padre[i][2].text)
                    i = i + 1
                i = 0
            return nombre,puesto,salario
        elif raiz.tag == "catalog":
            return "No hay informacion"


    def modificar(self,id,ruta,nombre,puesto,salario):
        archivo_xml = ET.parse(ruta)
        raiz = archivo_xml.getroot()
        i = 0
        if raiz.tag == "empresa":
            for padre in raiz:
                while i <= len(padre) - 1:
                    if id== padre[i].get('id'):
                       padre[i][0].text=nombre
                       padre[i][1].text = puesto
                       padre[i][2].text = salario
                    i = i + 1
                i = 0


    def Eliminar(self, id, ruta):
        archivo_xml = ET.parse(ruta)
        raiz = archivo_xml.getroot()
        i = 0
        if raiz.tag == "empresa":
            for departamento in raiz:
                for empleado in departamento.findall('empleado'):
                    idE = int(empleado.get('id'))
                    print(idE)
                    if idE== int(id):
                        departamento.remove(empleado)


    def GenerarNuevo(self,ruta):
        archivo_xml = ET.parse(ruta)
        nombre_archivo = ruta
        archivo_xml.write(nombre_archivo, xml_declaration=True, encoding="utf-8")


