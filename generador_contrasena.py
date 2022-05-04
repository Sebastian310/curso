import random

def generar_contrasena():
    upper=["A","B","C","D", "E", "F", "G"]
    lower=["a","b","c","d","e","f","g"]
    symbols=["!","#","$","&","/","(",")"]
    numbers=["1","2","3","4","5","6","7","8","9","0"]

    characters=upper+lower+symbols+numbers
    contrasena=[]                               #vamos a generar una lista vacía para colocarcaracteres aleatorios de las listas definidas anteriormente 

    for i in range(15):                             # para i en el rango (rango es la cantidad de ciclos que quiero que tenga el ciclo. en este caso 15 caracteres)
        caracter_random=random.choice(characters)  #creamos nueva variable que era cargada con un numero al azar de la lista de caracteres .choice es una funcion especial de ramdom.
        contrasena.append(caracter_random)          #agregamos el caracter generado a la lista contrasena
    contrasena = "".join(contrasena)                #esto es para convertir una lista en un STRING ** unimos todos los caracteres. para generar un string de las listas
    return contrasena                                  #las "" simbolizan un string vacío


def run():
    password=generar_contrasena()
    print("tu nueva cntraseña es :"+password)


if __name__=="__main__":
    run()