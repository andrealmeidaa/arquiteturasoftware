from typing import List,Optional
from entidades.tarefa import Tarefa
import uuid



class TarefaRepositoryInterface:
    def listar(self) -> List[Tarefa]:
        raise NotImplementedError

    def buscar_por_id(self, id: str) -> Optional[Tarefa]:
        raise NotImplementedError

    def salvar(self, tarefa: Tarefa) -> Tarefa:
        raise NotImplementedError

    def remover(self, id: str) -> None:
        raise NotImplementedError

class TarefaUseCase:
    def __init__(self, tarefa_repository: TarefaRepositoryInterface):
        self.tarefa_repository = tarefa_repository

    def listar_tarefas(self) -> List[Tarefa]:
        return self.tarefa_repository.listar()

    def buscar_tarefa(self, id: int) -> Optional[Tarefa]:
        return self.tarefa_repository.buscar_por_id(id)

    def criar_tarefa(self, titulo:str,descricao:str,completa:bool) -> Tarefa:
        tarefa=Tarefa(id=str(uuid.uuid4()),descricao=descricao,titulo=titulo,completa=completa)
        return self.tarefa_repository.salvar(tarefa)

    def atualizar_tarefa(self, id: str, titulo: str, descricao: str, completa: bool) -> Optional[Tarefa]:
        tarefa = self.tarefa_repository.buscar_por_id(id)
        if tarefa:
            tarefa.titulo = titulo
            tarefa.descricao = descricao
            tarefa.completa = completa
            return self.tarefa_repository.salvar(tarefa)
        return None

    def remover_tarefa(self, id: str) -> None:
        return self.tarefa_repository.remover(id)