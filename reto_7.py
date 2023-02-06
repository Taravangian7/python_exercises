#Crea un programa que cuente cuantas veces se repite cada palabra
# * y que muestre el recuento final de todas ellas.
# * - Los signos de puntuación no forman parte de la palabra.
# * - Una palabra es la misma aunque aparezca en mayúsculas y minúsculas.
# * - No se pueden utilizar funciones propias del lenguaje que
# *   lo resuelvan automáticamente.
import re

def most_commun_words(str):
    str=str.lower()
    patron=r'[a-z0-9À-ÿ]+'
    words=re.findall(patron,str)
    my_set=set(words)
    words_count=[]
    for word in my_set:
        words_count.append((words.count(word),word))
    words_count.sort(reverse=True)
    return words_count
print(most_commun_words('Este es un párrafo de prueba para ver si este método funciona, y es eficiente para contar palabras en un párrafo.'))