def conversor (tipo_pesos,valor_dolar):
    moneda =float(input("ingrese pesos " + tipo_pesos +" Parcerito :"))
    dolares= str(round((moneda/valor_dolar),2))
    print("tienes $"+ dolares + "Dolares")

menu = """
Bienvenido al conversor de monedas mas potente V2.0 🌝

1- Pesos Colombianos
2- Pesos Argentinos
3- Pesos Mexicanos

Elije una opción : """

opcion=int(input(menu))

if   opcion == 1:
   conversor ("Colombianos",3875)
elif opcion == 2:
   conversor ("Argentinos",65)
elif opcion == 3:
    conversor ("Argentinos",24)
else:
    print("ingresa una opcion valida")