def ParImpar(numero):
   if numero % 2 == 0:
       print("El numero es par")
   else:
       print("el numero es impar")


def PosNegOrZero(numero):
    if numero > 0:
        print("el numero es positivo")
    elif numero < 0:
        print("el numero es negativo")
    else:
        print("el numero es cero")



def Prime(num, module = 2):
    if num % module != 0:
        if module < num:
            Prime(num, module+1)
    else:
        if num != module:
            print("El numero no es primo")
        else:
            print("El numero es primo")

def YearBis(numero):
    if numero % 4 == 0:
        if numero % 100 != 0:
            print("Es año bisiesto")
        elif numero % 400 == 0:
            print("Es año bisiesto")
        else:
            print("No es año bisiesto")
    else:
        print("No es año bisiesto")


if __name__=='__main__':
    print("ingresa un numero :\n")
    numero = int(input())

    Prime(numero)
    PosNegOrZero(numero)
    ParImpar(numero)
    YearBis(numero)