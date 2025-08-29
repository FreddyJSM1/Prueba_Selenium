from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from time import sleep
driver = webdriver.Chrome()
import mysql.connector

s= Service(executable_path='chromedriver.exe')
driver = webdriver.Chrome(service=s)
driver.get('https://quotes.toscrape.com/')

resultado = driver.find_elements(By.CSS_SELECTOR, 'div[class="quote"]')

for q in resultado:
    texto = q.find_element(By.CSS_SELECTOR,value='span[class="text"]').text
    autor = q.find_element(By.CSS_SELECTOR,'small[class="author"]').text
    etiqueta = q.find_elements(By.CSS_SELECTOR,'a[class="tag"]')

    print(f"Frase: {texto}\nAutor: {autor}\nEtiqueta: {etiqueta}\n{'-'*9}")

boton = driver.find_element(By.CSS_SELECTOR, value='a[href="/page/2/"]')
boton.click()
sleep(5)

conexion = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="prueba"
)
cursor = conexion.cursor()

for indice, frase in enumerate(texto):
    resultado=[indice]

    sql= 'INSERT INTO frases_pagina VALUES (%s, %s, %s)'
    valores = (texto.text, autor.text, etiqueta.text)

cursor.execute(sql, valores)
conexion.commit()
cursor.close()
conexion.close()
driver.quit()






