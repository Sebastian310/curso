from ast import Try


def divisors(num):
    divisors=[]
    for i in range(1,num + 1):
        if num % i == 0:  #aquí es cero
            divisors.append(i)
    return divisors

def run():
    try:
        num=int(input("ingresa un numero :"))
        print(divisors(num))
        print("termino el programa")
    except ValueError:
        print("you have to enter a number")

if __name__ == "__main__":
   run()