from Nodo import Nodo
from ClassCanciones import Cancion


class MatrizCanciones:
    def __init__(self):
        self.Matriz=Nodo(1,1,Cancion("",""))

    def DefinirTamano(self,Fila,Columna):
        for i in range(Fila):
            for j in range(Columna):
                if i==0 and j==0:
                    self.Matriz=self.Matriz
                else:
                    temporal=Nodo(i+1,j+1,Cancion("",""))
                    temporal.anterior=self.Matriz
                    self.Matriz.siguiente=temporal
                    self.Matriz=self.Matriz.siguiente
        temporal=Nodo(Fila,Columna,Cancion("",""))
        temporal.anterior=self.Matriz
        self.Matriz.siguiente=temporal
        self.Matriz=self.Matriz.siguiente
    
    def RecorrerMatriz(self):
        self.RegresarAlInicio()
        while True:
            if self.Matriz.siguiente!=None:
                print("Fila: "+str(self.Matriz.fila)+" Columna: "+str(self.Matriz.columna))
                self.Matriz.Datos.ImprimirListadeAutores()
                self.Matriz=self.Matriz.siguiente
            else:
                break
    def AgregarInformacion(self,Fila,Columna,Cancion:Cancion):
        self.RegresarAlInicio()
        bandera=True
        while True:
            if self.Matriz.fila==Fila and self.Matriz.columna==Columna:
                self.Matriz.Datos=Cancion
                bandera=False
                break
            else:
                if self.Matriz.siguiente!=None:
                    self.Matriz=self.Matriz.siguiente
                else:
                    break
            
        if bandera:
            print("La posición Fila:"+str(Fila)+" Columna:"+str(Columna)+"No existe")
        


    def RegresarAlInicio(self):
         while True:
            if self.Matriz.anterior!=None:
                self.Matriz=self.Matriz.anterior
            else:
                break
        


   