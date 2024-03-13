

def comprar():
    print("compra de casas con bienes raices")
    casa=float(input("ingrese el valor de la casa que desea comprar: "))
    sueldo=float(input("ingrese su sueldo: "))
    if sueldo < 80000 and sueldo>0:
        pie=casa*0.30
        o=casa*0.70
        mensual=o/84
        round (mensual, 3)
        print(f"el pie sera de {pie}$")
        print(f"el pago mensual sera de {round (mensual,3)}$ por los siguientes 7 años")
    if sueldo >= 80000:
        pie=casa*0.15
        o=casa*0.85
        mensual=o/84
        round (mensual, 3)
        print(f"el pie sera de {pie}$")
        print(f"el pago mensual sera de {round (mensual,3)}$ por los siguientes 7 años")
    else:
        print("usted no cumple con los requisitos para la casa")
comprar()
        