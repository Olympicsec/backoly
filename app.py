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
    return render_template('our-mission.html')




if __name__ == '__main__':
    app.run(debug=True)