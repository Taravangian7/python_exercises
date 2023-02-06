 #Enunciado: Escribe una función que reciba dos palabras (String) y retorne verdadero o falso (Boolean) según sean o no anagramas.
 # Un Anagrama consiste en formar una palabra reordenando TODAS las letras de otra palabra inicial.
 # NO hace falta comprobar que ambas palabras existan.
 # Dos palabras exactamente iguales no son anagrama.
import re
def is_an_anagram(txt1,txt2):
    txt1=txt1.lower()
    txt2=txt2.lower()
    def list_of_letters(txt):
        patrón=r'[a-zÀ-ÿ]'
        list_letter=re.findall(patrón,txt)
        list_letter.sort()
        return list_letter
    list_txt1=list_of_letters(txt1)
    list_txt2=list_of_letters(txt2)
    same_letters=list_txt1==list_txt2
    only_letters= len(txt1)==len(list_txt1)
    different_word=txt1!=txt2
    return same_letters and different_word and only_letters

print(is_an_anagram('Árbol','Bolár'))