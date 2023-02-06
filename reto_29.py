# * Crea una función que ordene y retorne una matriz de números.
# * - La función recibirá un listado (por ejemplo [2, 4, 6, 8, 9]) y un parámetro
# *   adicional "Asc" o "Desc" para indicar si debe ordenarse de menor a mayor
# *   o de mayor a menor.
# * - No se pueden utilizar funciones propias del lenguaje que lo resuelvan
# *   automáticamente.

my_list=[2,4,6,6, 8, 9,9]

def sort_matrix (my_list:list,order:str):
    new_list=[]
    if order=='Desc':
        while len(my_list)!=0:
            new_list.append(my_list.pop(my_list.index(max(my_list))))
    elif order=='Asc':
        while len(my_list)!=0:
            new_list.append(my_list.pop(my_list.index(min(my_list))))
    return new_list

print(sort_matrix(my_list,'Asc'))
