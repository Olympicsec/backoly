from flask import Flask, render_template
import psycopg2
from flask import request

app = Flask(__name__)

# Configuración de la conexión
host = "35.223.204.64"
database = "postgres"
user = "postgres"
password = "admin"

# Render pagina index
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/mision')
def mission():
    return render_template('mission.html')

@app.route('/about')
def about():
    return render_template('aboutus.html')

@app.route('/404')
def error():
    return render_template('404.html')

@app.route('/contacto')
def contact():
    return render_template('contact.html')

@app.route('/donacion')
def donation():
    # Establecer la conexión
    conn = psycopg2.connect(host=host, database=database, user=user, password=password)
    # Crear un cursor
    cur = conn.cursor()
    
    # Ejecutar la consulta SQL
    cur.execute("SELECT * FROM Campanas")
    
    # Obtener los resultados
    campanas = cur.fetchall()
    
    # Cerrar el cursor y la conexión
    cur.close()
    conn.close()
    
    return render_template('donation1.html', campanas=campanas)

@app.route('/donacion_singular', methods=['GET'])
def donation_singular():
    campaign_id = request.args.get('id')  # Obtener el ID de la campaña desde los parámetros de la URL

    # Establecer la conexión
    conn = psycopg2.connect(host=host, database=database, user=user, password=password)

    # Crear un cursor
    cur = conn.cursor()

    # Ejecutar la consulta SQL para obtener la campaña por su ID
    cur.execute("SELECT * FROM Campanas WHERE ID_Campana = %s", (campaign_id,))

    # Obtener el resultado
    campana = cur.fetchone()

    # Cerrar el cursor y la conexión
    cur.close()
    conn.close()

    return render_template('donation-single.html', campana=campana)
if __name__ == '__main__':
    app.run(debug=True)