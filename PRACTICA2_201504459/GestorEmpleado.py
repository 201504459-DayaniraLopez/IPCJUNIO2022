import xml.etree.ElementTree as ET
class GestrorEmpleado:

    def imprimir(self,ruta):
        archivo_xml = ET.parse(ruta)
        raiz = archivo_xml.getroot()
        i=0
        cadena = ""
        for padre in raiz:
            while i <= len(padre)-1:
                cadena = cadena + "\nID: " + str(padre[i].get('id')) + "\nNombre: "+ str(padre[i][0].text)+"\nPuesto: " + str(padre[i][1].text)+"\nSalario: " + str(padre[i][2].text)
                i=i+1
            i = 0
        return cadena



