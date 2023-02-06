# * Crea una función que reciba dos cadenas como parámetro (str1, str2)
# * e imprima otras dos cadenas como salida (out1, out2).
# * - out1 contendrá todos los caracteres presentes en la str1 pero NO
# *   estén presentes en str2.
# * - out2 contendrá todos los caracteres presentes en la str2 pero NO
# *   estén presentes en str1.
def characters(str1,str2):
    out_1=''
    out_2=''
    for letter in str1:
        if letter not in str2:
            out_1+=letter
    for letter in str2:
        if letter not in str1:
            out_2+=letter
    return out_1,out_2
    
print(characters('Elton','Elon Musk'))