# * Crea un programa que sea capaz de transformar texto natural a código
# * morse y viceversa.
# * - Debe detectar automáticamente de qué tipo se trata y realizar
# *   la conversión.
# * - En morse se soporta raya "—", punto ".", un espacio " " entre letras
# *   o símbolos y dos espacios entre palabras "  ".
# * - El alfabeto morse soportado será el mostrado en
# *   https://es.wikipedia.org/wiki/Código_morse.
import string
def is_morse(txt):
    import re
    patron=r'[A-Za-zÀ-ÿ]'
    word_catcher=re.findall(patron,txt)
    morse= len(word_catcher)==0
    return morse
word_to_morse={'a':'.-','b':'-...','c':'-.-.','d':'-..','e':'.','f':'..-.','g':'--.','h':'....'
,'i':'..','j':'.---','k':'-.-','l':'.-..','m':'--','n':'-.','ñ':'--.--','o':'---','p':'.--.'
,'q':'--.-','r':'.-.','s':'...','t':'-','u':'..-','v':'...-','w':'.--','x':'-..-','y':'-.--','z':'--..',' ':'  '}
morse_to_word={v:k for k,v in word_to_morse.items()}

def convert(txt):
    import re
    if is_morse(txt)==True:
        patron=r'[.-]+|  '
        letras=re.findall(patron,txt)
        print(letras)
        nuevo=''
        for letter in letras:
            nuevo+=morse_to_word[letter]
        return nuevo
    else:
        patron=r'[a-z ]'
        letras=re.findall(patron,txt)
        print(letras)
        nuevo=''
        for letter in letras:
            if letter in string.ascii_letters:
                nuevo+=word_to_morse[letter]+' '
            else:
                nuevo+=' '
        return nuevo


txt='. ... - ---  . ... - .-  . ... -.-. .-. .. - ---  . -.  .-.. . - .-. .- ...'
print(convert(txt))
txt='esto va para morse'
txt=convert(txt)
print(txt)
print(convert(txt))
