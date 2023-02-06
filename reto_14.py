#* Escribe una función que calcule si un número dado es un número de Armstrong
# * (o también llamado narcisista).
# * Si no conoces qué es un número de Armstrong, debes buscar información 
# * al respecto.
def is_armstrong(num):
    digits=list(str(num))
    exp=len(digits)
    sum_dig=0
    for dig in digits:
        sum_dig+=(int(dig)**exp)
    if sum_dig==num:
        return True
    return False
print(is_armstrong(407))
