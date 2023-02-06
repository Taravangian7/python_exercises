# * Crea una función que analice una matriz 3x3 compuesta por "X" y "O"
# * y retorne lo siguiente:
# * - "X" si han ganado las "X"
# * - "O" si han ganado los "O"
# * - "Empate" si ha habido un empate
# * - "Nulo" si la proporción de "X", de "O", o de la matriz no es correcta.
# *   O si han ganado los 2.
# * Nota: La matriz puede no estar totalmente cubierta.
# * Se podría representar con un vacío "", por ejemplo.

matrix=[['O','X','O'],['X','X','O'],['O','O','X']]
for index in range(3):
    print(matrix[index])
def four_in_line(mat):
    def is_game(val):
        for index in range(3):
            if val==mat[index][0]==mat[index][1]==mat[index][2]:
                return True
            if val==mat[0][index]==mat[1][index]==mat[2][index]:
                return True
        if (val==mat[0][0]==mat[1][1]==mat[2][2]) or (val==mat[0][2]==mat[1][1]==mat[2][0]):
            return True
        return False
    x=is_game('X')
    o=is_game('O')
    qty_x=0
    qty_o=0
    for row in mat:
        qty_x+=row.count('X')
        qty_o+=row.count('O')
    diff=abs(qty_x-qty_o)
    if diff>1 or (x==True and o==True):
        return 'Null'
    elif x==False and o==False:
        return 'Tie'
    elif x==True:
        return 'X win'
    elif o==True:
        return 'O Win'

print (four_in_line(matrix))




