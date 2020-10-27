from sqlalchemy import create_engine, Integer, Column, String, ForeignKey
from sqlalchemy.orm import scoped_session, sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base


engine = create_engine('sqlite:///atividade.db', convert_unicode=True)
db_session = scoped_session(sessionmaker(autocommit=False, bind=engine))

Base = declarative_base()
Base.query = db_session.query_property()

class Programador(Base):
    __tablename__='programador'
    id = Column(Integer, primary_key=True)
    nome = Column(String(40))
    idade = Column(Integer)
    email = Column(String(40))

    def save(self):
        db_session.add(self)
        db_session.commit()
    
    def delete(self):
        db_session.delete(self)
        db_session.commit()

    def __repr__(self):
        return f'<Pessoa {self.nome}>'


class Habilidades(Base):
    __tablename__='habilidades'
    id = Column(Integer, primary_key=True)
    nome = Column(String(100))

    def save(self):
        db_session.add(self)
        db_session.commit()
    
    def delete(self):
        db_session.delete(self)
        db_session.commit()

    def __repr__(self):
        return f'<Pessoa {self.nome}>'


class Programador_Habilidade(Base):
    __tablename__='programador_habilidade'
    id = Column(Integer, primary_key=True)
    programador_id = Column(String(100), ForeignKey('programador.id'))
    habilidades_id = Column(String(100), ForeignKey('habilidades.id'))

    prog = relationship('Programador')
    habil = relationship('Habilidades')


class Usuarios(Base):
    __tablename__ = 'usuarios'
    id = Column(Integer, primary_key=True)
    login = Column(String(20), unique=True)
    senha = Column(String(20))
    

    def __repr__(self):
        return f'<Usuario {self.login}>'
    
    def save(self):
        db_session.add(self)
        db_session.commit()
    
    def delete(self):
        db_session.delete(self)
        db_session.commit()


def init_db():
    Base.metadata.create_all(bind=engine)

if __name__=='__main__':
    init_db()