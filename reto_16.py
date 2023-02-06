 #* Crea una función que reciba un String de cualquier tipo y se encargue de
 #* poner en mayúscula la primera letra de cada palabra.
 #* - No se pueden utilizar operaciones del lenguaje que
 #*   lo resuelvan directamente.

def upper_first_letter(str):
    sentence=str.split(' ')
    sentence_upper=[word.capitalize() for word in sentence]
    new_sentence=' '.join(sentence_upper)
    return new_sentence

print(upper_first_letter('Este es una prueba. Elton, keta.'))

for element in range(2,3):
    print(element)

my_set={2}
my_set.add(3)
print(my_set)
my_set2={2,3}
print(my_set==my_set2)

my_list=[]
my_list.append({1})
print(my_list)
my_list[0].add(2)
print(my_list)

my_list=[1,2,3,4,5,6]
my_new_list=[]
print(my_list[0:3] )

my_list=[[1,2],[2,3],[3,4],[4,5]]

for match in my_list:
    print(match)