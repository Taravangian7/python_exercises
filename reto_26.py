 # Crea un programa que dibuje un cuadrado o un triángulo con asteriscos "*".
 # - Indicaremos el tamaño del lado y si la figura a dibujar es una u otra.
 # - EXTRA: ¿Eres capaz de dibujar más figuras?

def print_figure (figure,side1,side2=0):
    if figure=='cuadrado':
        l1=[]
        l2=[]
        for a in range(side1):
            l1.append('*')
            if a==0 or a==(side1-1):
                l2.append('*')
            else:
                l2.append(' ')
        print(*l1)
        for a in range(side1-2):
            print(*l2)
        print(*l1)
    elif figure=='rectangulo':
        l1=[]
        l2=[]
        for a in range(side1):
            l1.append('*')
            if a==0 or a==(side1-1):
                l2.append('*')
            else:
                l2.append(' ')
        print(*l1)
        for a in range(side2-2):
            print(*l2)
        print(*l1)
    elif figure=='triangulo':
        for a in range (side1):
            l1=[]
            for b in range ((2*side1)-1):
                l1.append(' ')
            if a!=side1-1:
                l1[side1-1-a]='*'
                l1[side1-1+a]='*'
            else:
                for b in range ((2*side1)-1):
                    if b%2==0:
                      l1[b]='*'
            print(*l1)



            

print_figure('cuadrado',10)
print_figure('rectangulo',10,5)
print_figure('triangulo',6)
lista1=['*','*','*','*']
lista2=['*',' ',' ','*']
