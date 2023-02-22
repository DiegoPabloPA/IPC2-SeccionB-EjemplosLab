import xml.etree.ElementTree as ET
from MatrizMuestra import MatrizMuestras
from Muestra import Muestra
from ClassCeldas import Celda
class Lector:
    def Lectura(direccion):
        ListaEspecimenes=[]
        ListaMatrices=[]
        doc=ET.parse(direccion).getroot()
        organismos=doc.iter('organismo')
        listaMuestras=doc.iter('muestra')
        for elements in organismos:
            ListaEspecimenes.append(Muestra(elements.findtext('codigo'),elements.findtext('nombre'),'red'))
        
        
        for muestra in listaMuestras:
            temporal=MatrizMuestras()
            temporal.DefinirTamano(int(muestra.findtext('filas')),int(muestra.findtext('columnas')))
            celdasvivas=muestra.iter('celdaViva')
            for viva in celdasvivas:
                temporal.AgregarInformacion(int(viva.findtext('fila')),int(viva.findtext('columna')),Celda(viva.findtext('codigoOrganismo'),'red'))
            diccionario={
                "filas":muestra.findtext('filas'),
                "columnas":muestra.findtext('columnas'),
                "codigo":muestra.findtext('codigo'),
                "descripcion":muestra.findtext('descripcion'),
                "matriz":temporal
            }
                
            ListaMatrices.append(diccionario)

        return {"ListaEspecimenes":ListaEspecimenes,"ListaMatrices":ListaMatrices}