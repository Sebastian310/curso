menu = """
Bienvenido al Conversor de monedas re full 😂👍🙌😎😶‍🌫️🤯😰

1- Pesos Colombianos 
2- Pesos Argentinos
3- Pesos mexicanos 

Elige una opción: 
"""
opcion =int(input(menu))

if opcion == 1:
    pesos = float(input("Cúantos pesos Colombianos tienes? : "))
    valor_dolar = 3875
    dolares = round((pesos / valor_dolar),2)
    dolares = str (dolares)
    print ("Tienes $ " + dolares + " dolares")
elif opcion ==2:
    pesos = float(input("Cúantos pesos Argentinos tienes? : "))
    valor_dolar = 9888
    dolares = (pesos / valor_dolar)
    dolares = round(dolares, 2)
    dolares = str (dolares)
    print ("Tienes $ " + dolares + " dolares")
elif opcion ==3:
    pesos = float(input("Cúantos pesos Mexicanos tienes? : "))
    valor_dolar = 2000
    dolares = (pesos / valor_dolar)
    dolares = round(dolares, 2)
    dolares = str (dolares)
    print ("Tienes $ " + dolares + " dolares")
else:
    print("ingresa la opcion correcta plis")











