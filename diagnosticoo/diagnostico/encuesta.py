
from Trabajador import Trabajador


class encuesta():
    def __init__(self,lista):
        self.__lista=lista
    #Getters
    def get_lista(self):
        return self.__lista
    #Setters
    def set_lista(self,lista):
        self.__lista=lista
        
    def Crear_Trabajador(self,lista):
        print("Ingreso de Cliente\n")
        sexo=str(input("Ingrese el sexo: "))
        nombre=str(input("Ingrese el nombre: "))
        edad=int(input("Ingrese su edad: "))
        profesion=int(input("Ingrese su profesion= 1:ingeniero 2:abogado 3:otra "))
        sueldo=int(input("Ingrese su sueldo: "))
        marin=Trabajador(sexo,nombre,edad,sueldo,profesion)
        lista.append(marin)
        print("Se ha agregado con exito.")
        repetir=str(input("Quiere crear otro cliente? SI(1) o NO "))
        if str(repetir) == str("1"):
            encuesta.Crear_Trabajador(self,lista)
        else:
            return lista
        
    def Mostrar_Datos(lista):
        print("\t\tencuesta")
        j=1
        for i in lista:
            print("Datos cliente: ",j)
            Trabajador.Mostrar_Datos(i)
            j+=1
    def Menu(encuesta):
        print("encuesta trabajador.")
        print("1- empezar encuesta.")
        print("2- Mostrar datos de uso.")
        print("- Finalizar.")
        op=int(input("Ingrese la opción: "))
        while int(op) < int(1) or int(op) > int(4):
            op=int(input("Ingrese la opción: "))
        if int(op) == int(1):
            encuesta.Crear_Trabajador(encuesta.get_lista())
            encuesta.Menu()
        elif int(op) == int(2):
            lista=encuesta.get_lista()
            abo=0
            inge=0
            nosoc=0
            for i in lista:
                temp1=Trabajador.get_profesion(i)
                comp1=1
                comp11=2
                comp12=3
                if int(temp1) == comp1:
                    inge+=1
                elif int(temp1) == comp11:
                    abo+=1
                elif int(temp1)== comp12:
                    nosoc+=1
            total=abo+inge+nosoc
            for i in lista:
                comm=Trabajador.get_profesion(i)
                if comm==1:
                    sum=0
                    for comm in lista:
                        com=Trabajador.get_sueldo(i)
                        sum=sum+com
                    prom=sum/inge
            for i in lista:
                comm1=Trabajador.get_profesion(i)
                if comm1==2:
                    sum1=0
                    com1=0
                    for comm1 in lista:
                        com1=Trabajador.get_sueldo(comm1)
                        sum1=sum1+com1
                        prom1=sum1/abo
            for i in lista:
                comm2=Trabajador.get_profesion(i)
                if comm2==3:
                    sum2=0
                    com2=0
                    for comm2 in lista:
                        com2=Trabajador.get_sueldo(i)
                        sum2=sum2+com2
                        prom2=sum2/nosoc
                        
            
            print("Datos de uso.\n")
            print(f"La cantidad de ingenieros es: {(inge/total)*100}%\nLa cantidad de abogados es:{(abo/total)*100}% \nLa cantidad de otros es: {(nosoc/total)*100}%\nEl promedio de ingenieros es: {prom}\nEl promedio de abogados es: {prom1}\nEl promedio de otros es: {prom2}")
            encuesta.Menu()
