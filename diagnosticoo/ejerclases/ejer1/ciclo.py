
ca1=0
ca2=0
ca3=0
ca4=0
ca5=0


while True:
    print("""venta entradas para teatro 
              edad de descuento
         Categoría 1: 05 - 14 35 %
         Categoría 2: 15 - 19 25 %
         Categoría 3: 20 - 45 10 %
         Categoría 4: 46 - 65 25 %
         Categoría 5: 66 en adelante 35 %
         Pulse 6 para terminar y ver perdida
              valor entrada 100$""")
    op=int(input("Ingrese la categoria/opcion que pertenezca: ")) 
    if int(op) == int(1):
        ca1=int(input("cuantas quiere: "))
    if int(op) == int(2):
        ca2=int(input("cuantas quiere: "))
            
    if int(op) == int(3):
        ca3=int(input("cuantas quiere: "))
    
    if int(op) == int(4):
        ca4=int(input("cuantas quiere: "))
    
    
    if int(op) == int(5):
        ca5=int(input("cuantas quiere: "))
    
    
    cat1=ca1*0.35*100
    cat2=ca2*0.25*100
    cat3=ca3*0.1*100
    cat4=ca4*0.25*100
    cat5=ca5*0.35*100    
    

    if int(op) == int(6):
        cat2=ca2*0.25*100
        cat3=ca3*0.1*100
        cat4=ca4*0.25*100
        cat5=ca5*0.35*100
        print("perdida en dinero ")
        print(f"categoria 1: {cat1}")
        print(f"categoria 2: {cat2}")
        print(f"categoria 3: {cat3}")
        print(f"categoria 4: {cat4}")
        print(f"categoria 5: {cat5}")
        break
        