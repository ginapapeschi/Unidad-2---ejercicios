class Moto:
    __patente = str
    __marca = str
    __nom_cond = str
    __kilom = float
    
    def __init__ (self, pat, marca, nom, km):
        self.__patente = pat
        self.__marca = marca
        self.__nom_cond = nom
        self.__kilom = km

    def getPatente (self):
        return self.__patente
    
    def getMarca (self):
        return self.__marca
    
    def getNyA (self):
        return self.__nom_cond
    
    def getKm (self):
        return self.__kilom
    