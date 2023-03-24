from flask import Flask, jsonify, request
from cadastro import pessoa

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False


@app.route('/pessoas',methods=['GET'])
def get():
    return jsonify({'pessoas': pessoa, 'resposta': 'Requisição bem sucedida'}), 200


@app.route('/pessoas/<int:id>',methods=['GET'])
def get_id(id):
    for busca in pessoa:
        if busca.get('id') == id:
            return jsonify(pessoa)
        
                
@app.route('/pessoas',methods=['POST'])
def post():
    novo_cadastro = request.get_json()
    pessoa.append(novo_cadastro)
    return jsonify({'pessoas': pessoa,'resposta': 'pessoa adicionada'})

       
@app.route('/livros/<int:id>',methods=['PUT'])
def put(id):
    cadastro_alterado = request.get_json()
    for busca in pessoa:
        if pessoa.get('id') == id:
            pessoa.update(cadastro_alterado)
            return jsonify(pessoa)
    return jsonify({"message": "pesssoa não encontrado"})


@app.route('/pessoas/<int:id>', methods=['DELETE'])
def delete(id):
    for busca in pessoa:
        if busca['id'] == id:
            pessoa.remove(busca)
            return jsonify({'pessoas': pessoa,'resposta': 'Pessoa excluída com sucesso.'}),200
    return jsonify({'erro': 'Pessoa não encontrada.'}), 404


@app.route('/pessoas', methods=['OPTIONS'])
def options():
    response = jsonify({'Allow': 'GET, POST, PUT, DELETE, OPTIONS'})
    response.headers['Allow'] = 'GET, POST, PUT, DELETE, OPTIONS'
    return response, 200

app.run(port=5000,host='localhost',debug=True)