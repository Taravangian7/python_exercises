# * Crea una función que reciba dos array, un booleano y retorne un array.
# * - Si el booleano es verdadero buscará y retornará los elementos comunes
# *   de los dos array.
# * - Si el booleano es falso buscará y retornará los elementos no comunes
# *   de los dos array.
# * - No se pueden utilizar operaciones del lenguaje que
# *   lo resuelvan directamente.

lista1=[1,2,3,4,5]
lista2=[4,5,6,7,8]
valor=True
def function_xtrange(array1,array2,bool):
    set1=set(array1)
    set2=set(array2)
    if bool:
        return list(set1.intersection(set2))
    else:
        return list(set1.symmetric_difference(set2))

def function_xtrange2(array1,array2,bool):
    commun=[]
    not_commun=[]
    for element in array1:
        if element in array2:
            commun.append(element)
        else:
            not_commun.append(element)
    for element in array2:
        if element not in array1:
            not_commun.append(element)
    if bool:
        return commun
    else:
        return not_commun

print(function_xtrange(lista1,lista2,valor))
print(function_xtrange2(lista1,lista2,valor))