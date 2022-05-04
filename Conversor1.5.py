
menu= """
Bienvenido al conversor de monedas mas potente V2.0 🌝

1- Pesos Colombianos
2- Pesos Argentinos
3- Pesos Mexicanos

Elije una opción : """

opcion=int(input(menu))

if opcion == 1:
    moneda=float(input("ingreso pesos Colombianos Parcerito :"))
    valor_dolar=3875
    dolares= moneda/valor_dolar
    dolares=round(dolares,2)
    dolares=str(dolares)
    print("tienes $"+ dolares + "Dolares")
elif opcion == 2:
    moneda=float(input("ingreso pesos Argentinos Pibe :"))
    valor_dolar=65
    dolares= moneda/valor_dolar
    dolares=round(dolares,2)
    dolares=str(dolares)
    print("tienes $"+ dolares + "Dolares")
elif opcion == 3:
    moneda=float(input("ingreso pesos mexicanos GUEY :"))
    valor_dolar=24
    dolares= moneda/valor_dolar
    dolares=round(dolares,2)
    dolares=str(dolares)
    print("tienes $"+ dolares + "Dolares")
else:
    print("ingresa una opcion valida")                
         






