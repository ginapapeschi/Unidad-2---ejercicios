from clasemoto import Moto
import csv

class gestor_m:
    __lista_moto = []

    def __init__ (self):
        self.__lista_moto = []
    
    def agregar_m (self, unamoto):
        self.__lista_moto.append (unamoto)

    def leer_datos (self):
        archivo = open ('datosmoto.csv')
        reader = csv.reader (archivo, delimiter = ';')
        bandera = True
        for fila in reader:         #fila es el arreglo que trae los datos, cada componente trae un dato que fue separado por los ";".
            if bandera == True:     #las filas de los csv son arreglos, el primer arreglo de todos es la CABECERA que solo tiene el nombre de los datos, por ende, no interesa guardar.
                bandera = False     #se usa esta bandera para que la PRIMERA VEZ que entra solo la cambie, salteando la cabecera. las sig. veces entran por el ELSE.
        else:
            patente = fila[0]
            marca = fila[1]
            nom = fila[2]
            kilom = fila[3]
            unamoto = Moto (patente, marca, nom, kilom) #se crea una INSTANCIA de la clase Moto y envía las variables leídas del CSV como PARÁMETROS.
            self.agregar_m (unamoto)                    #llama al método agregar_m para que GUARDE ese objeto en la LISTA.

    def buscar (self, pat):
        indice = 0
        bandera = True
        while not bandera and indice < len(self.__lista_moto):
            if self.__lista_moto[indice].getPatente() == pat:
                 bandera = False
            else:
                indice += 1
        return bandera