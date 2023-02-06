#Crea una función que calcule y retorne cuántos días hay entre dos cadenas
# * de texto que representen fechas.
# * - Una cadena de texto que representa una fecha tiene el formato "dd/MM/yyyy".
# * - La función recibirá dos String y retornará un Int.
# * - La diferencia en días será absoluta (no importa el orden de las fechas).
# * - Si una de las dos cadenas de texto no representa una fecha correcta se
# *   lanzará una excepción.
from datetime import datetime,date,timedelta
import re
def days_difference(date1,date2):
    def convert_to_date(str):
        patron=r'^[0-9]{1,2}/[0-9]{1,2}/[0-9]{4}$'
        date_filter=re.findall(patron,str)
        if len(date_filter)==1:
            date_list=str.split('/')
            date_date=date(day=int(date_list[0]),month=int(date_list[1]),year=int(date_list[2]))
            return date_date
        else:
            print(f'The date {str} is wrong. Try dd/mm/yyyy')
    date1_converted=convert_to_date(date1)
    date2_converted=convert_to_date(date2)
    if date1_converted!=None and date2_converted!=None:
        days_diff=abs((date1_converted-date2_converted).days)
        return days_diff
    else:
        return 'Try again with the correct format'

print(days_difference('05/06/2022','08/07/2024'))