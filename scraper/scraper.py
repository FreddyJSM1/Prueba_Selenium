from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import NoSuchElementException
import mysql.connector
from time import sleep

# Configuración del driver
s = Service(executable_path='chromedriver.exe')
driver = webdriver.Chrome(service=s)
driver.get('https://quotes.toscrape.com/')

# Conexión a la base de datos
conn = mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='prueba_selenium'
)
cursor = conn.cursor()

# Crear tabla si no existe
cursor.execute("""
CREATE TABLE IF NOT EXISTS frases (
    id INT AUTO_INCREMENT PRIMARY KEY,
    frase TEXT,
    autor VARCHAR(255),
    etiqueta TEXT
)
""")

# Función para extraer y guardar datos
def extraer_y_guardar():
    resultado = driver.find_elements(By.CSS_SELECTOR, 'div.quote')
    for q in resultado:
        texto = q.find_element(By.CSS_SELECTOR, 'span.text').text
        autor = q.find_element(By.CSS_SELECTOR, 'small.author').text
        etiquetas = q.find_elements(By.CSS_SELECTOR, 'a.tag')
        etiquetas_texto = ', '.join([e.text for e in etiquetas])  # Convertir lista a string

        # Insertar en la base de datos
        cursor.execute("INSERT INTO frases (frase, autor, etiqueta) VALUES (%s, %s, %s)",
                       (texto, autor, etiquetas_texto))
        conn.commit()

# Recorrer todas las páginas
while True:
    extraer_y_guardar()
    try:
        siguiente = driver.find_element(By.CSS_SELECTOR, 'li.next > a')
        siguiente.click()
        sleep(2)
    except NoSuchElementException:
        break

# Cierre
driver.quit()
cursor.close()
conn.close()
