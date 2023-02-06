 #Enunciado: Escribe un programa que se encargue de comprobar si un número es o no primo.
 #Hecho esto, imprime los números primos entre 1 y 100.

def is_prime(number):
    if number<2:
        return False
    multiplos=[]
    for index in range(1,number):
        if number%index==0:
            multiplos.append(index)
    if len(multiplos)>1:
        return False
    return True

for number in range (1,101):
    if is_prime(number)==True:
        print(number)
