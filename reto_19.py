# * Crea una función que reciba días, horas, minutos y segundos (como enteros)
# * y retorne su resultado en milisegundos.

import datetime
def convert_ms(dias:int,horas:int,min:int,seg:int):
    range=datetime.timedelta(days=dias,hours=horas,minutes=min,seconds=seg)
    return 1000*range.total_seconds()

print(convert_ms(1,0,0,0))