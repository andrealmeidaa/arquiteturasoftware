from typing import List,Optional
from entidades.tarefa import Tarefa
from casos_uso.caso_uso_tarefa import TarefaRepositoryInterface

class InMemoryTarefaRepository(TarefaRepositoryInterface):
    def __init__(self):
        self.tarefas = []

    def listar(self) -> List[Tarefa]:
        return self.tarefas

    def buscar_por_id(self, id: str) -> Optional[Tarefa]:
        for tarefa in self.tarefas:
            if tarefa.id == id:
                return tarefa
        return None

    def salvar(self, tarefa: Tarefa) -> Tarefa:
        for i,t in enumerate(self.tarefas):
            if t.id == tarefa.id:
                self.tarefas[i] = tarefa
                return tarefa
        self.tarefas.append(tarefa)
        return tarefa

    def remover(self, id: str) -> None:
        self.tarefas = [tarefa for tarefa in self.tarefas if tarefa.id != id]