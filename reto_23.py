# * Crea dos funciones, una que calcule el máximo común divisor (MCD) y otra
# * que calcule el mínimo común múltiplo (mcm) de dos números enteros.
# * - No se pueden utilizar operaciones del lenguaje que 
# *   lo resuelvan directamente.

def MCD(num1,num2):
    my_list=[]
    for element in range (1,min(num1,num2)+1):
        my_list.append(element)
    for element in reversed(my_list):
        if num1%element==0 and num2%element==0:
            return element
print(MCD(59,1))

def MCM(num1,num2):
    mcd=MCD(num1,num2)
    return int((num1*num2)/mcd)

print(MCM(72,1))

