#DataBase

from flask import Flask, request, jsonify, send_file
from flask_restful import Resource, Api
import psycopg2
import pandas as pd

app = Flask(__name__)
api = Api(app)

# Configurações do banco de dados
db_host = 'localhost'
db_port = '5432'
db_name = 'crud_ceps'
db_user = 'postgres'
db_password = 'postgres'

# Conexão com o banco de dados
conn = psycopg2.connect(
    host=db_host,
    port=db_port,
    dbname=db_name,
    user=db_user,
    password=db_password
)

# Criação da tabela no banco de dados
with conn.cursor() as cur:
    cur.execute('''
        CREATE TABLE IF NOT EXISTS pessoas (
            id SERIAL PRIMARY KEY,
            nome VARCHAR(100) NOT NULL,
            cep VARCHAR(8) NOT NULL
        );
    ''')
    conn.commit()

# Classes modelo
class Pessoa:
    def __init__(self, id, nome, cep):
        self.id = id
        self.nome = nome
        self.cep = cep

    def to_dict(self):
        return {
            'id': self.id,
            'nome': self.nome,
            'cep': self.cep
        }

#CRUD

def create_pessoa(pessoa):
    with conn.cursor() as cur:
        cur.execute(f'''
            INSERT INTO pessoas (nome, cep)
            VALUES ({pessoa.nome}, {pessoa.cep})
            RETURNING id;
        ''')
        id = cur.fetchone()[0]
        conn.commit()
    return id

def read_ceps(id):
    with conn.cursor() as cur:
        cur.execute(f'''SELECT id, nome, cep 
                    FROM pessoas 
                    WHERE id = {id}''',)
        row = cur.fetchone()
    if row:
        return Pessoa(*row)
    else:
        return
    
def update_ceps(id, cep):
    cursor = conn.cursor()
    cursor.execute(f'''UPDATE ceps 
                   SET cep = {cep} 
                   WHERE id = {id}''')
    conn.commit()
    cursor.close()

def delete_ceps(id):
    cursor = conn.cursor()
    cursor.execute(f'''DELETE FROM ceps 
                   WHERE id = {id}''')
    conn.commit()
    cursor.close()

# API
app = Flask(_name_)
api = Api(app)

class Pessoa(Resource):
    def get(self):
        pessoas = read_pessoas()
        return {'pessoas': pessoas}

    def post(self):
        nome = request.json['nome']
        cep = request.json['cep']
        create_pessoa(nome, cep)
        return {'message': 'Pessoa criada com sucesso'}

    def put(self):
        id = request.json['id']
        nome = request.json['nome']
        cep = request.json['cep']
        update_pessoa(id, nome, cep)
        return {'message': 'Pessoa atualizada com sucesso'}

    def delete(self):
        id = request.json['id']
        delete_pessoa(id)
        return {'message': 'Pessoa(s) deletada(s) com sucesso'}

api.add_resource(ceps, '/ceps')

if _name_ == '_main_':
    app.run(debug=True)
    
# Conexão com o banco de dados
conn = psycopg2.connect(
    host=db_host,
    port=db_port,
    dbname=db_name,
    user=db_user,
    password=db_password
)

# Configurações do ViaCEP
viacep_url = 'https://viacep.com.br/ws/'

# Criação da tabela no banco de dados
with conn.cursor() as cur:
    cur.execute('''
        CREATE TABLE IF NOT EXISTS entregas (
            id SERIAL PRIMARY KEY,
            nome VARCHAR(100) NOT NULL,
            cep VARCHAR(8) NOT NULL,
            rua VARCHAR(50),
            numero VARCHAR(10),
            complemento VARCHAR(100),
            bairro VARCHAR(40),
            cidade VARCHAR(400),
            estado VARCHAR(2)
        );
    ''')
    conn.commit()
    
class Entrega:
    def __init__(self, id, nome, cep, rua=None, numero=None, complemento=None, bairro=None, cidade=None, estado=None):
        self.id = id
        self.nome = nome
        self.cep = cep
        self.rua = rua
        self.numero = numero
        self.complemento = complemento
        self.bairro = bairro
        self.cidade = cidade
        self.estado = estado

    def to_dict(self):
        return {
            'id': self.id,
            'nome': self.nome,
            'cep': self.cep,
            'rua': self.rua,
            'numero': self.numero,
            'complemento': self.complemento,
            'bairro': self.bairro,
            'cidade': self.cidade,
            'estado': self.estado
        }
        
def criar_entrega(entrega):
    endereco = obter_endereco_pelo_cep(entrega.cep)
    with conn.cursor() as cur:
        cur.execute('''
            INSERT INTO entregas (nome, cep, rua, numero, complemento, bairro, cidade, estado)'''

# Arquivo CSV
class CSV(Resource):
    def get(self):