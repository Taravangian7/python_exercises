# * Crea un programa que comprueba si los paréntesis, llaves y corchetes
# * de una expresión están equilibrados.
# * - Equilibrado significa que estos delimitadores se abren y cieran
# *   en orden y de forma correcta.
# * - Paréntesis, llaves y corchetes son igual de prioritarios.
# *   No hay uno más importante que otro.
# * - Expresión balanceada: { [ a * ( c + d ) ] - 5 }
# * - Expresión no balanceada: { a * ( c + d ) ] - 5 }


def correct_expression(exp):
    delimitadores={')':'(',']':'[','}':'{'}
    expresion=exp
    delim=[]
    for char in expresion:
        if char in delimitadores.values() or char in delimitadores.keys():
            delim.append(char)
    print(delim)
    delim2=delim.copy()
    for char in delim:
        if char in delimitadores.keys():
            posicion=delim2.index(char)
            if delim2[posicion-1]==delimitadores[char]:
                del delim2[posicion]
                del delim2[posicion-1]
            else:
                return False
            print(delim2)
    print(len(delim2))
    return True
    
print(correct_expression('{ [ a * ( c + d ) ] - (5*2*[2+4*{5+2} ]) }'))
