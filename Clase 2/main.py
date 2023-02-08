from MatrizCanciones import MatrizCanciones
from ClassCanciones import Cancion
if __name__=="__main__":
    playList=MatrizCanciones()
    playList.DefinirTamano(5,5)
    nuevo=Cancion('Kill Bill',2.35)
    nuevo.AgregarAutor('SZA','21/01/1998','Estadounidense')
    nuevo.AgregarAutor('Rob Bisel','19/10/1998','Estadounidense')
    nuevo.AgregarAutor('Carter Lang','14/09/2001','Estadounidense')
    playList.AgregarInformacion(4,4,nuevo)
    playList.RecorrerMatriz()

    

    