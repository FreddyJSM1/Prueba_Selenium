<h1> Prueba Selenium</h1>

<p>Este proyecto realiza <strong>web scraping</strong> en la página 
<a href="https://quotes.toscrape.com/" target="_blank">Quotes to Scrape</a> 
utilizando <strong>Selenium</strong> para extraer frases, autores y etiquetas, y luego guarda estos datos en una base de datos <strong>MySQL</strong>.</p>

<hr>

<h2> Descripción del código</h2>

<ol>
  <li><strong>Configuración del WebDriver:</strong> Se utiliza <code>chromedriver.exe</code> para controlar Google Chrome mediante Selenium y se abre la página objetivo.</li>
  <li><strong>Conexión a la base de datos MySQL:</strong> Se conecta a la base de datos <code>prueba_selenium</code> en <code>localhost</code> usando <code>mysql.connector</code>.</li>
  <li><strong>Creación de la tabla:</strong> Si no existe, se crea la tabla <code>frases</code> con columnas <em>id</em>, <em>frase</em>, <em>autor</em> y <em>etiqueta</em>.</li>
  <li><strong>Extracción y almacenamiento:</strong> Se recorren los elementos <code>div.quote</code>, se obtienen los datos y se insertan en la base de datos.</li>
  <li><strong>Navegación entre páginas:</strong> El script hace clic en "Next" hasta que no haya más páginas.</li>
  <li><strong>Cierre de recursos:</strong> Se cierra el navegador y la conexión a la base de datos.</li>
</ol>

<hr>

<h2> Instalación y dependencias</h2>

<h3>Instalar Python y pip</h3>
<p>Asegúrarse de tener <strong>Python </strong> y <strong>pip</strong> instalados.</p>

<h3>Instalar librerías necesarias</h3>
<pre><code>pip install selenium
pip install mysql-connector-python
</code></pre>

<h3>Instalar ChromeDriver</h3>
<ol>
  <li>Visita <a href="https://googlechromelabs.github.io/chrome-for-testing/" target="_blank">ChromeDriver - Página oficial</a>.</li>
  <li>Buscar la versión ChromeDriver 64 bit  y copia el enlace para <strong>Win64</strong>.</li>
  <li>Descarga el archivo <code>.zip</code> y extráelo.</li>
  <li>Copia <code>chromedriver.exe</code> a la carpeta del proyecto.</li>
</ol>

<h3>Instalar y configurar XAMPP</h3>
<ol>
  <li>Descarga XAMPP desde <a href="https://www.apachefriends.org/es/download.html" target="_blank">apachefriends</a>.</li>
  <li>Instala la versión de 64 bits.</li>
  <li>Inicia los servicios <strong>Apache</strong> y <strong>MySQL</strong> desde el panel de control de XAMPP.</li>
  <li>Abre <a href="http://localhost/phpmyadmin" target="_blank">phpMyAdmin</a> y crea la base de datos:
    <pre><code>CREATE DATABASE prueba_selenium;</code></pre>
  </li>
  <li>La tabla <code>frases</code> se creará automáticamente, pero se puede crear manualmente:
    <pre><code>CREATE TABLE frases (
    id INT AUTO_INCREMENT PRIMARY KEY,
    frase TEXT,
    autor VARCHAR(255),
    etiqueta TEXT
);</code></pre>
  </li>
</ol>

<hr>

<h2> Ejecución del script</h2>
<ol>
  <li>Guarda el código en un archivo, por ejemplo: <code>scraper.py</code>.</li>
  <li>Abre una terminal en la carpeta del proyecto.</li>
  <li>Ejecuta:
    <pre><code>scraper.py</code></pre>
  </li>
</ol>

<hr>

<h2>Estructura del proyecto</h2>
<pre>
proyecto_scraping
│── scraper.py
│── chromedriver.exe
│── README.md
</pre>

<hr>

<h2>Ejemplo de datos guardados</h2>
<table>
  <tr>
    <th>id</th>
    <th>frase</th>
    <th>autor</th>
    <th>etiqueta</th>
  </tr>
  <tr>
    <td>1</td>
    <td>“The world as we have created it is a process of our thinking...”</td>
    <td>Albert Einstein</td>
    <td>change, deep-thoughts, thinking, world</td>
  </tr>
  <tr>
    <td>2</td>
    <td>“It is our choices, Harry, that show what we truly are...”</td>
    <td>J.K. Rowling</td>
    <td>abilities, choices</td>
  </tr>
</table>

<hr>

<h2>Tecnologías utilizadas</h2>
<ul>
  <li>Python</li>
  <li>Selenium</li>
  <li>MySQL</li>
  <li>ChromeDriver</li>
  <li>XAMPP</li>
</ul>

<hr>

<h2>Notas</h2>
<ul>
  <li>Asegúrate de que la versión de ChromeDriver coincida con la versión de tu navegador Chrome.</li>
  <li>Crear la base de datos como "prueba_selenium, y si se crea la tabla de forma manual que esta se llame frases"</li>
</ul>

<h2>Flujo de trabajo</h2>
<ul>
	<li>Inicializa el navegador Chrome mediante Selenium.
	</li>
	<li>Conecta a la base de datos MySQL y crea la tabla frases si no existe.
	</li>
	<li> Extrae de cada pagina la frase, el autor y las etiquetas
	</li>
	<li> Inserta la información en la base de datos
	</li>
	<li> Navega por todas las paginas hasta que no hayan mas
	</li>
	<li> Cierra el navegador y la base de datos
	</li>
</ul>
