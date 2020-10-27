from models import Programador, Habilidades, Usuarios
from flask_httpauth import HTTPBasicAuth

auth = HTTPBasicAuth()

@auth.verify_password
def verify(login, senha):
    if not (login, senha):
        return False
    return Usuarios.query.filter_by(login=login, senha=senha).first()


#Métodos para manipular dados da tabela programador
def insere_programador():
    programador = Programador(nome='Gomes', idade=22, email='gomes@gomes.com')
    print(programador)
    programador.save()


def consulta_programador():
    programador = Programador.query.all()
    print(programador)
"""     programador = Programador.query.filter_by(nome='Gomes').first()
    print(programador.nome)
    print(programador.idade)
    print(programador.email) """

def alterar_programador():
    programador = Programador.query.filter_by(nome='Gomes').first()
    programador.idade = 28
    programador.save()

def excluir_programador():
    programador = Programador.query.filter_by(nome='Gomes').first()
    programador.delete()


#Métodos para manipular dados da tabela habilidades
def insere_habilidade():
    habilidade = Habilidades(nome='Python')
    print(habilidade)
    habilidade.save()


def consulta_habilidade():
    habilidade = Habilidades.query.all()
    print(habilidade)
"""     habilidade = Habilidades.query.filter_by(nome='Python').first()
    print(habilidade) """

def altera_habilidade():
    habilidade = Habilidades.query.filter_by(nome='Python').first()
    habilidade.nome = 'Flask'
    habilidade.save()

def excluir_habilidade():
    habilidade = Habilidades.query.filter_by(nome='Flask').first()
    habilidade.delete()


def insere_usuario(login, senha):
    usuario = Usuarios(login=login, senha=senha)
    usuario.save()

def consulta_usuario():
    usuarios = Usuarios.query.all()
    print(usuarios)


if __name__ == "__main__":
    #insere_programador()
    #consulta_programador()
    #alterar_programador()
    #excluir_programador()

    #insere_habilidade()
    #altera_habilidade()
    #excluir_habilidade()
    #consulta_habilidade()

    #insere_usuario(login='Yago', senha='123')
    #consulta_usuario()