class Trabajador():
    def __init__(self,sexo,nombre,edad,profesion,sueldo):
        self.__sexo=sexo
        self.__nombre=nombre
        self.__edad=edad
        self.__profesion=profesion
        self.__sueldo=sueldo
 
    #Getters
    def get_sexo(self):
        return self.__sexo
    def get_nombre(self):
        return self.__nombre
    def get_edad(self):
        return self.__edad
    def get_profesion(self):
        return self.__profesion
    def get_sueldo(self):
        return self.__sueldo

    #Setters
    def set_sexo(self,sexo):
        self.__sexo=sexo
    def set_nombre(self,nombre):
        self.__nombre=nombre  
    def set_edad(self,edad):
        self.__edad=edad  
    def set_profesion(self,profesion):
        self.__profesion=profesion  
    def set_sueldo(self,sueldo):
        self.__sueldo=sueldo
