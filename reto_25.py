# * Crea un programa que calcule quien gana más partidas al piedra,
# * papel, tijera.
# * - El resultado puede ser: "Player 1", "Player 2", "Tie" (empate)
# * - La función recibe un listado que contiene pares, representando cada jugada.
# * - El par puede contener combinaciones de "R" (piedra), "P" (papel)
# *   o "S" (tijera).
# * - Ejemplo. Entrada: [("R","S"), ("S","R"), ("P","S")]. Resultado: "Player 2".

def rock_paper_scissors(game:list):
    win_condition={'R':'S','P':'R','S':'P'}
    player1_score=0
    player2_score=0
    for match in game:
        if win_condition[match[0]]==match[1]:
            player1_score+=1
        elif win_condition[match[1]]==match[0]:
            player2_score+=1
    if player1_score==player2_score:
        return 'Tie'
    elif player1_score>player2_score:
        return 'Player 1'
    else:
        return 'Player 2'

print(rock_paper_scissors([("R","S"), ("S","R"), ("P","R")]))