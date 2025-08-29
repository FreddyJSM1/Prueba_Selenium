# Prueba_Selenium
Se realiza la importancion de las librerias a utilizar, ademas de que en el proyecto se descarga el controlador que utiliza Selenium para ejecutar Chrome desde la pagina "https://sites.google.com/chromium.org/driver/getting-started".

from selenium import webdriver

from selenium.webdriver.common.by import By

from selenium.webdriver.chrome.service import Service

from time import sleep

driver = webdriver.Chrome()

import mysql.connector


Se ejecuta el controlador para que habra automaticamente el navegador y se empizan a recibir los datos de la frase, autor y tags por medio de los Scripts
texto = q.find_element(By.CSS_SELECTOR,value='span[class="text"]').text

    autor = q.find_element(By.CSS_SELECTOR,'small[class="author"]').text

    etiqueta = q.find_elements(By.CSS_SELECTOR,'a[class="tag"]')

esta ejecucion se hace 9 veces por los elementos que hay en la pagina, luego se utiliza la linea de codigo

boton = driver.find_element(By.CSS_SELECTOR, value='a[href="/page/2/"]')

boton.click()

para actualizar la pagina al siguiente ventana y se toman los otros 9 elementos que esta contiene.
Una vez hecho, se cierra el proceso de Selenium para subir la informacion a la base de datos.
Se crea la base de datos prueba con una tabla de "frases_pagina" donde contiene 4 columnas
ID
Frase:
Autor:
Tag:
una vez subido la base de datos se actualiza y queda la informacion isertada en la tabla
