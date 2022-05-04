# def run():
#     nombre = input("Escribe tu nombre :")
#     for letra in nombre :               #Sirve para que muestre letra por letra el nombre ingresado
#         print (letra)                   #La variable letra se cargará con cada vuelta que haga luego de ingresar el nombre

# if __name__ == "__main__" :
#     run()

def run() :
    frase=(input("Escribe una Frase :"))
    for caracter in frase:
        print (caracter.upper())


if __name__=="__main__":
    run()