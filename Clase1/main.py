from ClassCanciones import Cancion

if __name__=="__main__":
    playList=Cancion('Kill Bill',2.35)
    playList.AgregarAutor('SZA','21/01/1998','Estadounidense')
    playList.AgregarAutor('Rob Bisel','19/10/1998','Estadounidense')
    playList.AgregarAutor('Carter Lang','14/09/2001','Estadounidense')

    playList.ImprimirListadeAutores()

    

    