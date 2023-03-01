from Nodo import Nodo
from ClassCeldas import Celda
from Graficar import Graphviz
from xml.etree.ElementTree import Element, SubElement, tostring

class MatrizMuestras:
    def __init__(self):
        self.Matriz=Nodo(1,1,Celda("",""))

    def DefinirTamano(self,Fila,Columna):
        for i in range(Fila):
            for j in range(Columna):
                if i==0 and j==0:
                    self.Matriz=self.Matriz
                else:
                    temporal=Nodo(i+1,j+1,Celda("",""))
                    temporal.anterior=self.Matriz
                    self.Matriz.siguiente=temporal
                    self.Matriz=self.Matriz.siguiente
        temporal=Nodo(Fila,Columna,Celda("",""))
        temporal.anterior=self.Matriz
        self.Matriz.siguiente=temporal
        self.Matriz=self.Matriz.siguiente

    def AgregarInformacion(self,Fila,Columna,CeldaViva:Celda):
        self.RegresarAlInicio()
        bandera=True
        while True:
            if self.Matriz.fila==Fila and self.Matriz.columna==Columna:
                self.Matriz.Datos=CeldaViva
                bandera=False
                break
            else:
                if self.Matriz.siguiente!=None:
                    self.Matriz=self.Matriz.siguiente
                else:
                    break
            
        if bandera:
            print("La posición Fila:"+str(Fila)+" Columna:"+str(Columna)+"No existe")
        

    def RecorrerMatriz(self):
            self.RegresarAlInicio()
            while True:
                if self.Matriz.siguiente!=None:
                    print("Fila: "+str(self.Matriz.fila)+" Columna: "+str(self.Matriz.columna)+" Muestra: "+str(self.Matriz.Datos.codigoMuestra))
                    
                    self.Matriz=self.Matriz.siguiente
                else:
                    break
    def RecorrerMatrizyEscribir(self,padre):
            
            self.RegresarAlInicio()
            while True:
                
                if self.Matriz.siguiente!=None:
                    if str(self.Matriz.Datos.codigoMuestra)!="":
                        celdaViva=SubElement(padre,'celdaViva')
                        fila=SubElement(celdaViva,'fila')
                        fila.text=str(self.Matriz.fila)
                        columna=SubElement(celdaViva,'columna')
                        columna.text=str(self.Matriz.columna)
                        codigoOrganismo=SubElement(celdaViva,'codigoOrganismo')
                        codigoOrganismo.text=str(self.Matriz.Datos.codigoMuestra)
                    self.Matriz=self.Matriz.siguiente
                else:
                    break
    def GraficarMatriz(self):
            code=""
            bodyTable=""
            fila="1"
            self.RegresarAlInicio()
            while True:

                if self.Matriz.siguiente!=None:
                    if str(self.Matriz.Datos.codigoMuestra)!="":
                        code+=Graphviz.NewColumn(self.Matriz.Datos.color,"")
                    else:
                        code+=Graphviz.NewColumn("#FFFFFF","")

                    self.Matriz=self.Matriz.siguiente
                    if str(self.Matriz.fila)!=str(fila):
                        bodyTable+=Graphviz.NewRow(code)
                        code=""
                        fila=self.Matriz.fila
                else:
                    break
            bodyTable+=Graphviz.NewRow(code)    
            tablecode=Graphviz.NodePerTable("n1",Graphviz.StartTable("1","2","5",bodyTable))
            return tablecode



    def RegresarAlInicio(self):
         while True:
            if self.Matriz.anterior!=None:
                self.Matriz=self.Matriz.anterior
            else:
                break
        


   