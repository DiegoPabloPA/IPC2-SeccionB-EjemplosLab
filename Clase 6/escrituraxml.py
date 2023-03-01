from xml.etree.ElementTree import Element, SubElement
import xml.etree.cElementTree as ET
class Escritor:
    def Escritura(Informacion):
        cabecera=Element('datosMarte')
        Organismos=SubElement(cabecera,'listaOrganismos')
        for muestras in Informacion['ListaEspecimenes']:
            muestra=SubElement(Organismos,'organismo')
            codigo=SubElement(muestra,'codigo')
            codigo.text=str(muestras.codigo)
            nombre=SubElement(muestra,'nombre')
            nombre.text=str(muestras.nombre)
        listadoMuestras=SubElement(cabecera,'listadoMuestras')

        for matriz in Informacion['ListaMatrices']:
            etiquetamuestra=SubElement(listadoMuestras,'muestra')
            codigo=SubElement(etiquetamuestra,'codigo')
            codigo.text=matriz["codigo"]
            descripcion=SubElement(etiquetamuestra,'descripcion')
            descripcion.text=matriz["descripcion"]
            filas=SubElement(etiquetamuestra,'filas')
            filas.text=matriz["filas"]
            columnas=SubElement(etiquetamuestra,'columnas')
            columnas.text=matriz["columnas"]
            listadoCeldasVivas=SubElement(etiquetamuestra,'listadoCeldasVivas')
            matriz['matriz'].RecorrerMatrizyEscribir(listadoCeldasVivas)
        arbol=ET.ElementTree(cabecera)
        arbol.write("salida.xml",encoding='utf-8', xml_declaration=True)
        