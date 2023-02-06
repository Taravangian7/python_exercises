#/*
# * Crea un programa que invierta el orden de una cadena de texto
# * sin usar funciones propias del lenguaje que lo hagan de forma automática.
# * - Si le pasamos "Hola mundo" nos retornaría "odnum aloH"
texto='Elton'
print(texto[::-1])

def invert_string(string):
    new_string=''
    total_index=len(string)
    for index in range(total_index):
        new_string+=string[total_index-index-1]
    return new_string
print(invert_string('Pablo Hergenreder'))
