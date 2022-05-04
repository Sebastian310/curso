from ast import Try


def divisors(num):
    divisors=[]
    for i in range(1,num + 1):
        if num % i == 0:  #aquí es cero
            divisors.append(i)
    return divisors

def run():
        num=input("ingresa un numero :") 
        assert int(num) > 0,"you must to type a positive number"   #only apply for one case
        print(divisors(int(num)))
        print("termino el programa")

#    assert num.isnumeric() and int(num)>0,"you must to type a positive number"  Apply for both
#    assert num.isnumeric() ,"you must to type a positive number"  Apply for both because 
#isnumero, only receive positive strings without "-" symbol

if __name__ == "__main__":
   run()