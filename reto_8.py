 #* Crea un programa se encargue de transformar un número
 #* decimal a binario sin utilizar funciones propias del lenguaje que lo hagan directamente.

def decimal_to_bin(num):
    binary=[]
    while num!=1 and num!=0:
        binary.append(num%2)
        num=num//2
    else:
        binary.append(num)
    binary.reverse()
    bin=''
    for element in binary:
        bin+=str(element)
    return bin

print(decimal_to_bin(28))