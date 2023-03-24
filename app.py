from flask import Flask, jsonify, request
from cadastro import pessoas

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False


@app.route('/pessoas',methods=['GET'])
def get():
    return jsonify({'pessoas': pessoas, 'resposta': 'Requisição bem sucedida'}), 200


@app.route('/pessoas/<int:id>',methods=['GET'])
def get_id(id):
    for busca in pessoas:
        if busca.get('id') == id:
            return jsonify(pessoas)
        
                
@app.route('/pessoas',methods=['POST'])
def post():
    novo_cadastro = request.get_json()
    pessoas.append(novo_cadastro)
    return jsonify({'pessoas': pessoas,'resposta': 'pessoa adicionada'})

       
@app.route('/livros/<int:id>',methods=['PUT'])
def put(id):
    cadastro_alterado = request.get_json()
    for busca in pessoas:
        if pessoas.get('id') == id:
            pessoas.update(cadastro_alterado)
            return jsonify(pessoas)
    return jsonify({"message": "pesssoa não encontrado"})


@app.route('/pessoas/<int:id>', methods=['DELETE'])
def excluir_pessoa(id):
    for busca in pessoas:
        if busca['id'] == id:
            pessoas.remove(busca)
            return jsonify({'pessoas': pessoas,'resposta': 'Pessoa excluída com sucesso.'}),200
    return jsonify({'erro': 'Pessoa não encontrada.'}), 404


@app.route('/pessoas', methods=['OPTIONS'])
def options():
    response = jsonify({'Allow': 'GET, POST, PUT, DELETE, OPTIONS'})
    response.headers['Allow'] = 'GET, POST, PUT, DELETE, OPTIONS'
    return response, 200

app.run(port=5000,host='localhost',debug=True)

from flask import Flask, jsonify, request
from cadastro import pessoas



app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False



@app.route('/pessoas',methods=['GET'])
def get():
    return jsonify({'pessoas': pessoas, 'resposta': 'Requisição bem sucedida'}), 200

   

@app.route('/pessoas/<int:id>',methods=['GET'])
def get_id(id):
    for busca in pessoas:
        if busca.get('id') == id:
            return jsonify(pessoas)
        

@app.route('/pessoas', methods=['HEAD'])
def head():
    return '', 200, {'Content-Type': 'application/json'}
        
        
@app.route('/pessoas',methods=['POST'])
def post():
    novo_pessoa = request.get_json()
    pessoas.append(novo_pessoa)
    return jsonify({'pessoas': pessoas,'resposta': 'pessoa adicionada'})


@app.route('/pessoas/<int:id>', methods=['PATCH'])
def update_pessoa(id):
    pessoa_atualizada = request.get_json()
    for pessoa in pessoas:
        if pessoa.get('id') == id:
            pessoa.update(pessoa_atualizada)
            return jsonify({'pessoa': pessoa, 'resposta': 'pessoa atualizada'}), 200
    return jsonify({'resposta': 'pessoa não encontrada'}), 404


@app.route('/pessoas/<int:id>', methods=['PUT'])
def update_livro(id):
    pessoa_alterado = request.get_json()
    for busca in pessoas:
        if busca['id'] == id:
            busca.update(pessoa_alterado)
            return jsonify(busca)
    return jsonify({"message": "pessoa não encontrado"})

@app.route('/pessoas/<int:id>', methods=['DELETE'])
def excluir_pessoa(id):
    for pessoa in pessoas:
        if pessoa['id'] == id:
            pessoas.remove(pessoa)
            return jsonify({'pessoas': pessoas,'resposta': 'Pessoa excluída com sucesso.'}),200
    return jsonify({'erro': 'Pessoa não encontrada.'}), 404

app.run(port=5000,host='localhost',debug=True)