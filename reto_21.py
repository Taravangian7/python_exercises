#Lee el fichero "Challenge21.txt" incluido en el proyecto, calcula su
# * resultado e imprímelo.
# * - El .txt se corresponde con las entradas de una calculadora.
# * - Cada línea tendrá un número o una operación representada por un
# *   símbolo (alternando ambos).
# * - Soporta números enteros y decimales.
# * - Soporta las operaciones suma "+", resta "-", multiplicación "*"
# *   y división "/".
# * - El resultado se muestra al finalizar la lectura de la última
# *   línea (si el .txt es correcto).
# * - Si el formato del .txt no es correcto, se indicará que no se han
# *   podido resolver las operaciones.

import os

#cwd = os.getcwd()  # Get the current working directory (cwd)
#files = os.listdir(cwd)  # Get all the files in that directory
#print("Files in %r: %s" % (cwd, files))
my_txt=open('30DaysOfPython/retos_de_programación/challenge_21.txt','r')

def calculator_txt(txt):
    operations=list(map(lambda x: x.replace('\n',''),txt.readlines()))
    try:
        resultado=float(operations[0])
    except:
        return f'{operations[0]} is not a valid number'
    for index,element in enumerate(operations):
        if index%2==1:
            try:
                num2=float(operations[index+1])
                if element=='+':
                    resultado+=num2
                elif element=='-':
                    resultado-=num2
                elif element=='*':
                    resultado*=num2
                elif element=='/':
                    resultado/=num2
                else:
                    return f'{element} is not a valid operator.'
            except:
                return f'{operations[index+1]} is not a valid number.'
    return resultado
            

print(calculator_txt(my_txt))
