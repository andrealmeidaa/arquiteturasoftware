from dataclasses import dataclass

@dataclass
class Tarefa:
    id: str
    titulo: str
    descricao: str
    completa: bool = False