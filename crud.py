# Create DB

CREATE DATABASE crud_desafio;

CREATE TABLE cpfs (
    id SERIAL PRIMARY KEY,
    cpf int(11),
);

# CRUD

import psycopg2

conn = psycopg2.connect(database="crud_desafio", user="x_x", password="postgres", host="localhost", port="5432")

def create_cpfs(cpf):
    cursor = conn.cursor()
    cursor.execute(f"INSERT INTO cpfs (cpf) VALUES {cpf}")
    conn.commit()
    cursor.close()

def read_cpfs():
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM cpfs")
    rows = cursor.fetchall()
    cursor.close()
    return rows

def update_cpfs(id, cpf):
    cursor = conn.cursor()
    cursor.execute(f"UPDATE cpfs SET cpf = {cpf} WHERE id = {id}")
    conn.commit()
    cursor.close()

def delete_cpfs(id):
    cursor = conn.cursor()
    cursor.execute(f"DELETE FROM cpfs WHERE id = {id}")
    conn.commit()
    cursor.close()
    
    
    # API
    
from flask import Flask, request
from flask_restful import Resource, Api

app = Flask(_name_)
api = Api(app)

class cpfs(Resource):
    def get(self):
        cpfs = read_cpfs()
        return {'cpfs': cpfs}

    def post(self):
        cpfs = request.json['cpfs']
        create_cpfs(cpfs)
        return {'message': 'CPFs cadastrados'}

    def put(self):
        id = request.json['id']
        cpfs = request.json['cpfs']
        update_cpfs(id, cpfs)
        return {'message': 'CPFs atualizados com sucesso'}

    def delete(self):
        id = request.json['id']
        delete_cpfs(id)
        return {'message': 'CPF deletado com sucesso'}

api.add_resource(cpfs, '/cpfs')

if _name_ == '_main_':
    app.run(debug=True)