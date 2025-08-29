# Prueba_Selenium
Se utiliza Selenium para automatizar la extracción de frases, autores y etiquetas (tags) desde una página web. Los datos extraídos son posteriormente almacenados en una base de datos MySQL.

Requisitos

Python 3.x

Google Chrome instalado

ChromeDriver
 (descargado y compatible con tu versión de Chrome)

Librerías de Python:

selenium

mysql-connector-python

Instalación

Instala las dependencias necesarias:

pip install selenium mysql-connector-python


Se descarga el controlador de Chrome (ChromeDriver) desde el siguiente enlace:
https://sites.google.com/chromium.org/driver/getting-started


Funcionamiento

Se importan las siguientes librerías en el script:

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from time import sleep
import mysql.connector


Se inicializa el controlador de Chrome con Selenium:

driver = webdriver.Chrome()


Se accede a la página objetivo y se extraen los siguientes datos para cada frase:

Texto de la frase:

texto = q.find_element(By.CSS_SELECTOR, 'span[class="text"]').text


Autor:

autor = q.find_element(By.CSS_SELECTOR, 'small[class="author"]').text


Etiquetas:

etiqueta = q.find_elements(By.CSS_SELECTOR, 'a[class="tag"]')


El proceso se repite 9 veces (una por cada elemento en la página).

Para navegar a la siguiente página, se hace clic en el botón de paginación:

boton = driver.find_element(By.CSS_SELECTOR, 'a[href="/page/2/"]')
boton.click()


Se repite el proceso de recolección de datos en la nueva página.

Una vez finalizado el scraping, se cierra el navegador controlado por Selenium.

# Base de Datos

Se crea una base de datos llamada prueba.

Dentro de esta base de datos, se crea la tabla frases_pagina con las siguientes columnas:

ID	Frase	Autor	Tag

Los datos recopilados son insertados en esta tabla utilizando mysql-connector-python.
