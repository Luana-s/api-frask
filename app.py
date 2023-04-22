from flask import Flask, jsonify, request
from cadastro import pessoas

#409

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False

id = 0

@app.route('/person',methods=['GET'])
def get():
    return jsonify({'person': pessoas, 'resposta': 'Requisição bem sucedida'}), 200

   

def verificaEmail(email):
    for pessoa in pessoas:
        if pessoa.get('email') == email:
            return True
    return False
        




@app.route('/person', methods=['POST'])
def post():
    global id
    nova_pessoa = request.get_json()
    if verificaEmail(nova_pessoa['email']):
        return jsonify({'resposta': 'Esse E-mail já está cadastrado no sistema.'}), 409
    
    nova_pessoa['id'] = id + 1
    pessoas.append(nova_pessoa)
    id += 1
    return jsonify({'pessoas': pessoas,'resposta': 'pessoa adicionada'})


@app.route('/person/<int:id>', methods=['PATCH'])
def patch(id):
    pessoa_atualizada = request.get_json()
    for busca in pessoas:
        if busca.get('id') == id:
            busca.update(pessoa_atualizada)
            return jsonify({'pessoa': busca, 'resposta': 'pessoa atualizada'}), 200
    return jsonify({'resposta': 'pessoa não encontrada'}), 404

@app.route('/pessoas', methods=['HEAD'])

def head():
    return '', 200, {'Content-Type': 'application/json'}

@app.route('/person/<int:id>', methods=['PUT'])
def put(id):
    pessoa_alterada = request.get_json()
    for busca in pessoas:
        if busca['id'] == id:
            busca.update(pessoa_alterada)
            return jsonify(busca)
    return jsonify({"message": "pessoa não encontrado"})



@app.route('/person/<int:id>', methods=['DELETE'])
def delete(id):
    for busca in pessoas:
         if 'id' in busca and busca['id'] == id:
            pessoas.remove(busca)
            return jsonify({'pessoas': pessoas,'resposta': 'Pessoa excluída com sucesso.'}),200
    return jsonify({'erro': 'Pessoa não encontrada.'}), 404


@app.route('/pessoas', methods=['OPTIONS'])
def options():
    response = jsonify({'Allow': 'GET, POST, PUT, DELETE, OPTIONS'})
    response.headers['Allow'] = 'GET, POST, PUT, DELETE, OPTIONS'
    return response, 200




app.run(port=5002,host='0.0.0.0',debug=True)
