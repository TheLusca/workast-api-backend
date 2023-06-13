from flask import Flask, make_response, jsonify, request
# from db import createdatabase as db
# lib em python para realizar as conexções sql em python
import mysql.connector

# Conexão com o banco de dados utilizando a lib mysql.connector
mydb = mysql.connector.connect(
    host='localhost',
    user='userlucast',
    password='MainPassword',
    database='lucast'

)
# Instanciando o Flask
app = Flask(__name__)
# Ativar ordem nos objetos JSON
app.config['JSON_SORT_KEYS'] = False

# Rota para captura de dados
@app.route('/treino', methods=['GET'])
def get_treino():

    # abrir o cursor do banco ede dados na vbariavel nydb cursor é um agente que vai executar o codigo do banco de dados
    my_cursor = mydb.cursor()
    my_cursor.execute('SELECT * FROM treino')
    meus_treinos = my_cursor.fetchall()

    # Tratamento de dados
    treinos = list()
    for treino in meus_treinos:
        treinos.append(
            {
                "id": treino[0],
                "nome_do_exercicio": treino[1],
                "dia_da_semana": treino[2],
                "carga":  treino[3],
                "repeticoes":  treino[4]

            }
        )

    print(treinos)

    return make_response(
        jsonify(
            message='Lista de Treinos',
            data=treinos
        )
    )


@app.route('/treino', methods=['POST'])
def create_treino():
    treino = request.json

    my_cursor = mydb.cursor()

    sql = f"INSERT INTO treino (nome_do_exercicio, dia_da_semana, carga, repeticoes) VALUES ('{treino['nome_do_exercicio']}', '{treino['dia_da_semana']}', '{treino['carga']}', '{treino['repeticoes']}')"
    my_cursor.execute(sql)
    mydb.commit()

    return make_response(
        jsonify(
            message='Treino cadastrado com sucesso',
            # livro=Livros
        )
    )


app.run(debug=True)
