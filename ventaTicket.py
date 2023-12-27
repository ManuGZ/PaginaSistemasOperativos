from flask import Flask
from flask import render_template, request, redirect
from flaskext.mysql import MySQL
from datetime import datetime
import random as r

app = Flask(__name__)

mysql = MySQL()

app.config["MYSQL_DATABASE_HOST"] = "localhost"
app.config["MYSQL_DATABASE_USER"] = "root"
app.config["MYSQL_DATABASE_PASSWORD"] = "Luka123"
app.config["MYSQL_DATABASE_DB"] = "sitio"
mysql.init_app(app)


@app.route("/")
def inicio():
    conexion = mysql.connect()
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM sitio.eventos")
    eventos = cursor.fetchall()
    conexion.commit()
    return render_template("index.html", eventos=eventos)


@app.route("/eventos")
def admin():
    conexion = mysql.connect()
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM sitio.eventos")
    eventos = cursor.fetchall()
    conexion.commit()
    return render_template("eventos.html", eventos=eventos)


@app.route("/guardar", methods=["POST"])
def guardar_eventos():
    _nombre = request.form["txtNombre"]
    _imagen = request.form["txtImagen"]
    _desc = request.form["txtDesc"]
    _boletos = request.form["txtBoletos"]
    _precio = request.form["txtPre"]

    sql = f"INSERT INTO `sitio`.`eventos` (`nombre`, `imagen`, `descripcion`, `boletos`,`precio`) VALUES ('{_nombre}', '{_imagen}', '{_desc}', '{_boletos}','{_precio}');"
    conexion = mysql.connect()
    cursor = conexion.cursor()
    cursor.execute(sql)
    conexion.commit()
    return redirect("/eventos")


@app.route("/ventas")
def ventas_app():
    conexion = mysql.connect()
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM sitio.eventos")
    eventos = cursor.fetchall()
    conexion.commit()
    return render_template("ventas.html", eventos=eventos)


@app.route("/ventas/exito", methods=["POST"])
def ventas_exito():
    _nombre = request.form["nombre_eventos"]
    _cantidad = request.form["cantidad_boletos"]
    _correo = request.form["correo_"]
    _ciudad = request.form["ciudad_"]
    _codigoPostal = request.form["codigo_postal"]
    codigo = r.randint(0, 2500)

    sql = f"INSERT INTO `sitio`.`ventas` (`codigo`, `correo_electronico`, `nombre_evento`, `ciudad`,`codigo_postal`,`precio`) VALUES ('{codigo}', '{_correo}', '{_nombre}', '{_ciudad}','{_codigoPostal}','{0.0}');"
    conexion = mysql.connect()
    cursor = conexion.cursor()
    cursor.execute(sql)
    conexion.commit()

    sql = f"UPDATE `sitio`.`eventos` SET `boletos` = `boletos`-'{_cantidad}' WHERE (`nombre` = '{_nombre}');"
    conexion = mysql.connect()
    cursor = conexion.cursor()
    cursor.execute(sql)
    conexion.commit()

    cursor.execute("SELECT * FROM sitio.eventos")
    eventos = cursor.fetchall()

    return render_template("ventas.html", eventos=eventos)


if __name__ == "__main__":
    app.run(debug=True)


if __name__ == '__main__':
    app.run(debug=True)
