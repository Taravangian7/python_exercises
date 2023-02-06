# * Crea una función que reciba un texto y muestre cada palabra en una línea,
# * formando un marco rectangular de asteriscos.
# * - ¿Qué te parece el reto? Se vería así:
# *   **********
# *   * ¿Qué   *
# *   * te     *
# *   * parece *
# *   * el     *
# *   * reto?  *
# *   **********

def frame_str(string):
    list_str=string.split(' ')
    max_len=0
    for element in list_str:
        if len(element)>max_len:
            max_len=len(element)
    print('*'*(max_len+4))
    for element in list_str:
        print('* '+element+(' '*(max_len+1-len(element)))+'*')
    print('*'*(max_len+4))

frame_str('elton, keta dnd?')
