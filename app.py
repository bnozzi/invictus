

import sqlite3
from flask import Flask,render_template, request, url_for, flash, redirect

app=Flask(__name__)
app.config['SECRET KEY']='dev'
@app.route("/")
def index():
    return render_template("index.html")


@app.route('/inscripcion', methods=("GET","POST"))
def inscripcion():

    if request.method=="POST": # si hay una peticion al servidor del tipo post 
        # guardo los datos del formulario del index 
        nombre=request.form['nombre']
        apellido=request.form['apellido']
        tel=request.form['tel']
        correo=request.form['correo']
        #.
        #. falta el resto de campos 
        #.

        conn=get_db_connection()
        conn.execute("insert into persona(nombre, apellido, numero, correo) values(?,?,?,?)",(nombre,apellido,tel,correo))
        conn.commit()
        conn.close()
         
        print(f"datos de ", nombre,"  guardados ")
        
        return redirect(url_for("index"))    



    else:
        print (" not post ")
        
    def clear_form():
        pass

    return render_template('inscripcion.html')


def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn
