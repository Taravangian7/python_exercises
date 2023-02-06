# * Escribe una función que calcule y retorne el factorial de un número dado
# * de forma recursiva.
def factorial(num):
    factorial=1
    for number in range(1,num+1):
        factorial=factorial*number
    return factorial
print(factorial(5))