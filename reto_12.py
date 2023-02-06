# * Escribe una función que reciba un texto y retorne verdadero o
# * falso (Boolean) según sean o no palíndromos.
# * Un Palíndromo es una palabra o expresión que es igual si se lee
# * de izquierda a derecha que de derecha a izquierda.
# * NO se tienen en cuenta los espacios, signos de puntuación y tildes.
# * Ejemplo: Ana lleva al oso la avellana.
from string import ascii_letters
def  is_palindromo(str):
    str=str.lower()
    list_str=list(filter(lambda x:x in ascii_letters,str)) #A Filter le podes pasar un str y lo lee como lista.
    list_str_rev=list_str.copy()
    list_str_rev.reverse()
    if list_str==list_str_rev:
        return True
    return False


print(is_palindromo('Ana lleva al oso la avellana.'))