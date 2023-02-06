# * Enunciado: Crea un función, que dado un año, indique el elemento 
# * y animal correspondiente en el ciclo sexagenario del zodíaco chino.
# * - Info: https://www.travelchinaguide.com/intro/astrology/60year-cycle.htm
# * - El ciclo sexagenario se corresponde con la combinación de los elementos
# *   madera, fuego, tierra, metal, agua y los animales rata, buey, tigre,
# *   conejo, dragón, serpiente, caballo, oveja, mono, gallo, perro, cerdo
# *   (en este orden).
# * - Cada elemento se repite dos años seguidos.
# * - El último ciclo sexagenario comenzó en 1984 (Madera Rata).
import requests
from bs4 import BeautifulSoup
import time
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import pandas as pd
#Scrapping sin elemento tabla, armo la tabla yo de manera más manual.
#url = 'https://www.travelchinaguide.com/intro/astrology/60year-cycle.htm'
#options = Options()#configurar unas opciones para abrir una ventana en navegador
#options.add_argument('--headless')#hace que no se abra en la compu, sino que se "abre" dentro de python nomas. no la veo
#options.add_argument('--disable-gpu')#para que no te consuma gpu. porque no necesita.
#driver = webdriver.Firefox(options=options)#abro navegador(Firefox) con las opciones marcadas antes.
#driver.get(url)#ahora sí que obtengo la url
#time.sleep(1)  # time to wait to start scraping the html
#page = driver.page_source  # obtengo el html.
#driver.quit()#Cierro el navegador virtual
#print(page)
#soup = BeautifulSoup(page, 'html.parser')  # parsing html to text
#data = soup.find_all('tr')[2::]

#OPCION 1:Scrapping con elemento tabla
url = 'https://www.travelchinaguide.com/intro/astrology/60year-cycle.htm'
#Opción:Abriendo navegador web 
#options = Options()#configurar unas opciones para abrir una ventana en navegador
#options.add_argument('--headless')#hace que no se abra en la compu, sino que se "abre" dentro de python nomas. no la veo
#options.add_argument('--disable-gpu')#para que no te consuma gpu. porque no necesita.
#driver = webdriver.Firefox(options=options)#abro navegador(Firefox) con las opciones marcadas antes.
#driver.get(url)#ahora sí que obtengo la url
#page = driver.page_source  # obtengo el html.
#driver.quit()#Cierro el navegador virtual

#OPCION 2: Esto si lo hago con requests:
page=requests.get(url,verify=False).content #sin el verify no funca

soup = BeautifulSoup(page, 'html.parser')  # parsing html to text
table1 = soup.find('table',class_='table1 tbLeft')
table2 = soup.find('table',class_='table1 tbRight')
#Obtengo título de columnas:
headers=[]
for i in table1.find_all('th'):
    title = i.text.replace('\t','_')
    headers.append(title)
# Create a dataframe cuyas columnas sean los headers
mydata = pd.DataFrame(columns = headers)
# Create a for loop to fill mydata. Inserto la data, paso por cada fila, tomo los datos y los inserto en el dataframe.
for j in table1.find_all('tr')[1:]:
    row_data = j.find_all('td')
    row = [i.text for i in row_data]
    length = len(mydata) #Cantidad de columnas
    mydata.loc[length] = row  #el .loc no sé que función cumple.
for j in table2.find_all('tr')[1:]:
    row_data = j.find_all('td')
    row = [i.text for i in row_data]
    length = len(mydata) 
    mydata.loc[length] = row 
# Drop “No.” column
mydata.drop('No.', inplace=True, axis=1)

def get_zodiacsign_and_wuxing(year:int):
    while year not in range(1924,1984):
        if year<1924:
            year+=60
        if year>1983:
            year-=60
    year=str(year)
    zodiac_sign=mydata[mydata['Gregorian___Year']==year]['Zodiac___Sign'].values[0] #Esto lo hice con chatGPT, una joya.
    wu_xing=mydata[mydata['Gregorian___Year']==year]['Wu___Xing'].values[0]
    return (wu_xing,zodiac_sign)
print(get_zodiacsign_and_wuxing(1993))


