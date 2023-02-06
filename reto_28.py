# * Simula el funcionamiento de una máquina expendedora creando una operación
# * que reciba dinero (array de monedas) y un número que indique la selección
# * del producto.
# * - El programa retornará el nombre del producto y un array con el dinero
# *   de vuelta (con el menor número de monedas).
# * - Si el dinero es insuficiente o el número de producto no existe,
# *   deberá indicarse con un mensaje y retornar todas las monedas.
# * - Si no hay dinero de vuelta, el array se retornará vacío.
# * - Para que resulte más simple, trabajaremos en céntimos con monedas
# *   de 5, 10, 50, 100 y 200.
# * - Debemos controlar que las monedas enviadas estén dentro de las soportadas.

productos={1:{'item':'Chocolate','precio':200},
           2:{'item':'Caramelos','precio':15},
           3:{'item':'Alfajor','precio':70},
           4:{'item':'Chicle','precio':20}}
flata=[10,50,10]

def maquina_exp(plata,prod):
    monedas_admitidas=[200,100,50,10,5]
    dinero_ingresado=0
    vuelto=[]
    if prod not in productos:
        print('El producto no existe')
        return plata
    for moneda in plata:
        dinero_ingresado+=moneda
        if moneda not in monedas_admitidas:
            print ('Moneda no admitida')
            return plata
    dinero_a_cobrar=productos[prod]['precio']
    vuelto_a_entregar=dinero_ingresado-dinero_a_cobrar
    if vuelto_a_entregar<0:
        print('El dinero ingresado no es suficiente')
        return plata
    while vuelto_a_entregar!=0:
        monedas_disponibles=list(filter(lambda x: x<=vuelto_a_entregar,monedas_admitidas))
        vuelto.append(monedas_disponibles[0])
        vuelto_a_entregar-=monedas_disponibles[0]
    item=productos[prod]['item']
    print(item)
    return vuelto



print(maquina_exp(flata,3))





