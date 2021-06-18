import sqlite3
from flask import Flask

# Configurações

DATABASE = './flaskr.db'
SECRET_KEY = "app"
USERNAME = 'fredy'
PASWORD = '120609'

# Aplicação

app = Flask(__name__)
app.config.from_object(__name__)

def connect_db():
    return sqlite3.connect(DATABASE)