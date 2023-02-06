# * Crea una función que imprima los 30 próximos años bisiestos
# * siguientes a uno dado.
# * - Utiliza el menor número de líneas para resolver el ejercicio.

def leap_year(year:int):
    print(*[year+(4*i) for i in range (1,31)])
    print('\n'.join([str(year+(4*i)) for i in range (1,31)]))

leap_year(2024)