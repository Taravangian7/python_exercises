# * Crea un programa que determine si dos vectores son ortogonales.
# * - Los dos array deben tener la misma longitud.
# * - Cada vector se podría representar como un array. Ejemplo: [1, -2]

vector1=[5,0,1]
vector2=[-1/5,1,2]

def is_orto(vect1,vect2):
    prod_int=0
    for val1,val2 in zip(vect1,vect2):
        prod_int+=(val1*val2)
    if prod_int==0:
        return True
    return False

print(is_orto(vector1,vector2))