class Autores:
    def __init__(self,nombre,fechanacimiento,nacionalidad):
        self.__nombre=nombre
        self._fechanacimiento=fechanacimiento
        self._nacionalidad=nacionalidad
    
    def getNombre(self):
        return self.__nombre
    
    def getFechaNacimiento(self):
        return self._fechanacimiento
    
    def getNacionalidad(self):
        return self._nacionalidad
    
    def setNacionalidad(self,nacionalidad):
        self._nacionalidad=nacionalidad
    
    def setNombre(self,nombre):
        self.__nombre=nombre

    def setFechaNacimiento(self,fecha):
        self._fechanacimiento=fecha 