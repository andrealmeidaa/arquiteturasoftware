from typing import List,Optional
from entidades.tarefa import Tarefa
from sqlalchemy import create_engine, Column, String,Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from casos_uso.caso_uso_tarefa import TarefaRepositoryInterface

DATABASE_URL = "sqlite:///tarefa.db"
engine = create_engine(DATABASE_URL, echo=True)

Base = declarative_base()

class TarefaModel(Base):
    __tablename__='tarefas'
    id=Column(String,primary_key=True)
    titulo=Column(String)
    descricao=Column(String)
    completa=Column(Boolean)
    def __repr__(self):
        return f"<TarefaModel(id={self.id}, titulo={self.titulo}, descricao={self.descricao}, completa={self.completa})>"

class UtilTarefa:
    @classmethod
    def dataclassToModel(tarefa:Tarefa)->TarefaModel:
        return TarefaModel(id=tarefa.id,titulo=tarefa.titulo,descricao=tarefa.descricao,completa=tarefa.completa)
    @classmethod
    def modelToDataclass(tarefaModel:TarefaModel) -> Tarefa:
        return Tarefa(id=tarefaModel.id,titulo=tarefaModel.titulo,descricao=tarefaModel.descricao,completa=tarefaModel.completa)   t

class SQLiteTarefaRepository(TarefaRepositoryInterface):
    def __init__(self):
        # Cria a tabela no banco de dados
        Base.metadata.create_all(engine)

        # Cria uma sessão para interagir com o banco de dados
        Session = sessionmaker(bind=engine)
        self.session = Session()

    def listar(self) -> List[Tarefa]:
        tarefa_models = self.session.query(TarefaModel).all()
    
    # Converte cada UserModel para a dataclass User
        return [UtilTarefa.modelToDataclass(tarefa_model) for tarefa_model in tarefa_models]

    def buscar_por_id(self, id: str) -> Optional[Tarefa]:
        tarefa_model=self.session.query(TarefaModel).filter_by(id=id).first()
        if tarefa_model is not None:
            tarefa=UtilTarefa.modelToDataclass(tarefa_model)
            return tarefa
        return None

    def salvar(self, tarefa: Tarefa) -> Tarefa:
        tarefa=self.buscar_por_id(tarefa.id)
        if tarefa:
            trefa_model=UtilTarefa.dataclassToModel(tarefa)
            self.sessiona
        return tarefa

    def remover(self, id: str) -> None:
        self.tarefas = [tarefa for tarefa in self.tarefas if tarefa.id != id]