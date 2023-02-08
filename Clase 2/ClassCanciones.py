from ClassAutores import Autores
from datetime import datetime
class Cancion:
    def __init__(self,nombre,duracion):
        self.__nombre=nombre
        self.ListadeAutores=[]
        self.duracion=duracion

    def AgregarAutor(self,nombre,fechNacimiento,nacionalidad):
        nuevoAutor=Autores(nombre,fechNacimiento,nacionalidad)
        self.ListadeAutores.append(nuevoAutor)
    
    def ImprimirListadeAutores(self):
        for item in self.ListadeAutores:
            
            fechaNacimiento=datetime.strptime(item.getFechaNacimiento(),'%d/%m/%Y')
            fechaActual=datetime.now()
            edad=int((fechaActual-fechaNacimiento).days/365)         
            print("""Hola Soy: {nombre} de origen: {nacionalidad} y tengo una edad de {edad} años""".format(nombre=item.getNombre(),nacionalidad=item.getNacionalidad(),edad=str(edad)))
       
    def getNombreCancion(self):
        return self.__nombre
    
    def setNombreCancion(self,nombre):
        self.__nombre=nombre