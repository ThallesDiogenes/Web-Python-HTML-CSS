# -- Ocean Samsung
# -- Prof. Guilherme Feulo
# -- Second class about WEB programming using the following languages: python, css and html. (11/11/2021)
# -- This project was developed usign gitpod.io plataform

# First try | Print in the screen this expression "Hello world": print("Hello world")

import sqlite3
from flask import Flask, g

DATABASE = "blog.db"
SECRET_KEY = "pudim"

app = Flask(__name__)
app.config.from_object(__name__)

def conectar_db():
    return sqlite3.connect(DATABASE)

# -- g is a global variable
@app.before_request

def pre_requisicao():
    g.db = conectar_db()

def pos_requisicao(exception):
    g.db.close()

@app.route('/')
def exibir_entradas():
    sql = "SELECT titulo, texto FROM entradas ORDER BY id DESC"
    cur = g.db.execute(sql)
    entradas = []
    for titulo, texto in cur.fetchall():
        entradas.append({'titulo':titulo, 'texto':texto})
    return str(entradas) 



# return "<h1 style='color:purple'>Hello everyone! Everything is okay?</h1> <a href='/pudim'>Pudim</a>"

@app.route('/pudim')
def pudim():
    return "<h1 style='color:blue'>I like pudim!</h1>"

