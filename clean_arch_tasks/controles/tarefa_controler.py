
from typing import List
from fastapi import FastAPI
from pydantic import BaseModel
from casos_uso.caso_uso_tarefa import TarefaUseCase
from infraestrutura.tarefa_repository import InMemoryTarefaRepository

api=FastAPI()
# TODO: Melhorar a documentação com base em https://medium.com/codex/how-to-document-an-api-for-python-fastapi-best-practices-for-maintainable-and-readable-code-a183a3f7f036
class TarefaSchema(BaseModel):
    id: str
    titulo: str
    descricao: str
    completa: bool

class TarefaCreateSchema(BaseModel):
    titulo: str
    descricao: str
 
caso_uso_tarefa=TarefaUseCase(InMemoryTarefaRepository())

@api.get("/tarefas",response_model=List[TarefaSchema])
async def listar_tarefas():
    """
    Retorna toda as tarefas cadastradas no banco de dados
    - Returns:
        - **dict**: Um dicionário contendo os atributos da classe Tarefa
    """
    return caso_uso_tarefa.listar_tarefas()

@api.get("/tarefas/{id}",response_model=TarefaSchema)
def buscar_tarefa(id:str):
    return caso_uso_tarefa.buscar_tarefa(id)

@api.post("/tarefas",response_model=TarefaSchema)
def criar_tarefa(tarefa:TarefaCreateSchema):
    return caso_uso_tarefa.criar_tarefa(tarefa.titulo,tarefa.descricao,False)

@api.put("/tarefas/{id}",response_model=TarefaSchema)
def atualizar_tarefa(tarefa:TarefaSchema):
    return caso_uso_tarefa.atualizar_tarefa(tarefa.id,tarefa.titulo,tarefa.descricao,tarefa.completa)

@api.delete("/tarefas/{id}")
def remover_tarefa(id:str):
    caso_uso_tarefa.remover_tarefa(id)
    return {"message":"Tarefa removida com sucesso"}