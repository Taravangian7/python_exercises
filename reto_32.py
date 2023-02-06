# * Dado un listado de números, encuentra el SEGUNDO más grande.
my_numbers=[5,2,25,36,-15,0,100.4,100.5]

def second_largest_number(my_list:list):
    max_numer=max(my_list)
    while max_numer in my_list:
        my_list.remove(max_numer)
    return max(my_list)

print(second_largest_number(my_numbers))