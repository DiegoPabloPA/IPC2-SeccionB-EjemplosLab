import os
from lecturaxml import Lector
from escrituraxml import Escritor
from Graficar import GeneradorGrafico
information={}
class Menu:
    
    def start():
        global information
        opc=0
        while opc!=4:
            print("Por favor Seleccione una opción: \n1.Cargar Archivo\n2.Escribir Archivo\n3.Graficar Matriz\n4.Salir")
            opc=int(input("Selección: "))  
            if opc==1:
                dire=input("Ingrese la dirección del archivo de entrada: ")
                information=Lector.Lectura(dire)
            elif opc==2:
                if information:
                    Escritor.Escritura(information)
                else:
                    print("No hay información cargada")
            elif opc==3:
                if information:
                    GeneradorGrafico.Graficar(information)
                else:
                    print("No hay información cargada")
            
            elif opc==4:
                os.system('cls')
                print("Facultad de Ingeniería Todos los derechos reservados.")
            else:
                os.system('cls')
                print("Opción inválida por favor seleccione una opción correcta\n")