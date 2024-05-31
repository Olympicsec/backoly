from flask import Flask, render_template
import psycopg2

app = Flask(__name__)

# Configuración de la conexión
host = "35.223.204.64"
database = "olympicsec"
user = "postgres"
password = "admin"

# Render pagina index
@app.route('/')
def index():
    return render_template('index-3.html')

@app.route('/mision')
def mission():
    return render_template('our-mission.html')

@app.route('/about')
def about():
    return render_template('about-us.html')

@app.route('/404')
def error():
    return render_template('404.html')

@app.route('/contacto')
def contact():
    return render_template('contact.html')

@app.route('/donacion')
def donation():
    return render_template('donation-1.html')

@app.route('/donacion_singular')
def donation_singular():
    return render_template('donation-single.html')

if __name__ == '__main__':
    app.run(debug=True)