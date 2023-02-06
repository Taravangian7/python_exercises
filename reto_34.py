# * Enunciado: Dado un array de enteros ordenado y sin repetidos, 
# * crea una función que calcule y retorne todos los que faltan entre
# * el mayor y el menor.
# * - Lanza un error si el array de entrada no es correcto.
# */

def missing_numbers(numbs:list):
    try:
        if numbs!=sorted(numbs):
            return 'The numbers are not sorted or their type is not int'
        missing=[]
        for num in range(numbs[0],numbs[-1]+1):
            if numbs.count(num)>1:
                return f'The number {num} is repeated'
            elif num not in numbs:
                missing.append(num)
    except Exception as error:
        return error
    return missing

print(missing_numbers([3,4,6]))