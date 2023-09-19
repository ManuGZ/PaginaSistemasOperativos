from flask import Flask
from flask import render_template, request, redirect
from flaskext.mysql import MySQL
from datetime import datetime

app = Flask(__name__)

mysql = MySQL()

app.config['MYSQL_DATABASE_HOST'] = 'localhost'
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'Luka12345'
app.config['MYSQL_DATABASE_DB'] = 'sitio'
mysql.init_app(app)


@app.route('/')
def inicio():
    conexion = mysql.connect()
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM sitio.eventos")
    eventos = cursor.fetchall()
    conexion.commit()
    return render_template('index.html', eventos=eventos)


@app.route('/eventos')
def admin():
    conexion = mysql.connect()
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM sitio.eventos")
    eventos = cursor.fetchall()
    conexion.commit()
    return render_template('eventos.html', eventos=eventos)


@app.route('/guardar', methods=['POST'])
def guardar_eventos():
    _nombre = request.form['txtNombre']
    _imagen = request.form['txtImagen']
    _desc = request.form['txtDesc']
    _boletos = request.form['txtBoletos']

    sql = f"INSERT INTO `sitio`.`eventos` (`nombre`, `imagen`, `descripcion`, `boletos`) VALUES ('{_nombre}', '{_imagen}', '{_desc}', '{_boletos}');"
    conexion = mysql.connect()
    cursor = conexion.cursor()
    cursor.execute(sql)
    conexion.commit()
    return redirect('/eventos')


if __name__ == '__main__':
    app.run(debug=True)
