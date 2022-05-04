
def read():
    numbers=[]
    with open("./files/numbers.txt","r",encoding="utf-8") as f:      #as f por que es el nobre de variable con el que nos vamos a refeerir al archivo 
        for line in f:
            numbers.append(int(line))  # se convierte a entero porque line es un string                                                                 #aquí se coloca encoding para evitar caracteres especiales del español. 
        print(numbers)                                                            # todo lo que etá despues de dos puntos es un bloque de código.

def write():
    names=["pepe","papo","Pedro","José"]
    with open ("./files/archive.txt","w",encoding="utf-8") as f:
        for name in names:
            f.write(name)
            f.write("\n")   #esto es un salto de página

def write2():
    names=["pepe2","papo2","Pedro2","José2"]
    with open ("./files/archive.txt","a",encoding="utf-8") as f:  #"a" de append
        for name in names:
            f.write(name)
            f.write("\n")   #esto es un salto de página

def run():
    write2()


if __name__=="__main__":
    run()