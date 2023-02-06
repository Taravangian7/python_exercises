 # Enunciado: Crea UNA ÚNICA FUNCIÓN (importante que sólo sea una) que sea capaz de calcular y retornar el área de un polígono.
 # - La función recibirá por parámetro sólo UN polígono a la vez.
 # - Los polígonos soportados serán Triángulo, Cuadrado y Rectángulo.
 # - Imprime el cálculo del área de un polígono de cada tipo.

def area_poligono(poligono):
    poligono=poligono.lower()
    if poligono=='triángulo':
        base=float(input('ingrese Base: '))
        altura=float(input('ingrese Altura: '))
        area=(base*altura)/2
    if poligono=='rectángulo':
        lado_1=float(input('ingrese Lado 1: '))
        lado_2=float(input('ingrese Lado 2: '))
        area=lado_1*lado_2
    if poligono=='cuadrado':
        lado=float(input('ingrese Lado: '))
        area=lado**2
    return area
    


print(area_poligono('Cuadrado'))