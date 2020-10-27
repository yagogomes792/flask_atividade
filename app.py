from models import Programador, Habilidades, Usuarios
from flask import Flask, request, json
from flask_restful import Resource, Api
from flask_httpauth import HTTPBasicAuth


app = Flask(__name__)
api = Api(app)
auth = HTTPBasicAuth() #serve para utilizar autenticação nos métodos

@auth.verify_password #marcador para utilizar verificador de senha
def verify(login, senha):
    if not (login, senha):
        return False
    return Usuarios.query.filter_by(login=login, senha=senha).first() #retorna o objeto do banco com usuario e senha para fazer o login

class GetProgramador(Resource):
    def get(self, nome):
        try:
            programador = Programador.query.filter_by(nome=nome).first()
            response = {
                'id':programador.id,
                'nome':programador.nome,
                'idade':programador.idade,
                'email':programador.email
            }
            return response
        except AttributeError:
            return {'message':'Usuario não encontrado'}
    
    @auth.login_required #marcador para solicitar login e senha antes de alterar programador
    def put(self, nome):
        try:
            programador = Programador.query.filter_by(nome=nome).first()
            dados = request.json
            if 'nome' in dados:
                programador.nome = dados['nome']
            if 'idade' in dados:
                programador.idade = dados['idade']
            if 'email' in dados:
                programador.email = dados['email']
            programador.save()

            response = {
                'id':programador.id,
                'nome':programador.nome,
                'idade':programador.idade,
                'email':programador.email
            }
            return response
        except AttributeError:
            return {'message':'Usuario não encontrado'}

    @auth.login_required #marcador para solicitar login e senha antes de deletar programador
    def delete(self, nome):
        try:
            programador = Programador.query.filter_by(nome=nome).first()
            programador.delete()
            return {'message':f'usuario {programador.nome} excluido com sucesso'}
        except AttributeError:
            return {'message':'Usuario não encontrado'}


class SetProgramador(Resource):
    def get(self):
        try:
            programador = Programador.query.all()
            response = [{'id':i.id, 'nome':i.nome, 'idade':i.idade, 'email':i.email} for i in programador] #comando 'for' inline utilizando função lambda para listar todos os programadores
            return response
        except:
            return {'message':'Ocorreu um erro, entrar em contato com o adm'}

    @auth.login_required  #marcador para solicitar login e senha antes de inserir programador
    def post(self):
        try:
            dados = request.json
            programador = Programador(nome=dados['nome'], idade=dados['idade'], email=dados['email'])
            programador.save()
            response = {
                'id':programador.id,
                'nome':programador.nome,
                'idade': programador.idade,
                'email':programador.email
            }
            return response
        except:
            return {'message':'Ocorreu um erro, entrar em contato com o adm'}

class SetHabilidade(Resource):
    def get(self):
        habilidade = Habilidades.query.all()
        response = [{'id':i.id, 'nome':i.nome} for i in habilidade] #comando 'for' inline utilizando função lambda para listar todas as habilidades
        return response

    @auth.login_required  #marcador para solicitar login e senha antes de inserir habilidade
    def post(self):
        dados = request.json
        habilidade = Habilidades(nome=dados['nome'])
        habilidade.save()
        response = {'id':habilidade.id, 'nome':habilidade.nome} #comando 'for' inline utilizando função lambda para listar todas as habilidades após inserir uma nova
        return response


api.add_resource(GetProgramador, '/programador/<string:nome>/')
api.add_resource(SetProgramador, '/programador/')
api.add_resource(SetHabilidade, '/habilidades/')


if __name__ == "__main__":
    app.run(debug=True)