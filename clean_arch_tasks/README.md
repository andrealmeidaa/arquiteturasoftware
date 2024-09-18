# Arquitetura Limpa

Neste diretório temos a estrutura básica de um projeto em Python usando FastAPI. Os modelos são armazenados em memória.

## Estrutura de pastas

### Entidades

Contém a definição dos modelos usando dataclass, o que deixa agnóstico de framework, um dos princípios da arquitetura limpa.

### Casos de Uso
Os casos de uso mantém as operações de manuseio dos dados do modelo, ou seja, todas as regras de negócio constam nesse arquivo. Cabe destacar que as operações nesse nível também são agnósticas de framework. Ao definir a interface *TarefaRepositoryInterface* com as operações de regra de negócio, indica que o provedor concreto das funcionalidades precisa honrar esse contrato. Já a classe *TarefaUseCase* implementa efetivamente as operações de negócio com base na interface *TarefaRepositoryInterface*.

### Infraestrutura

Nessa pasta temos uma possível implementação da interface *TarefaRepositoryInterface*, nesse caso para realizar persistência em memória. Se fosse realizada a implementação para persistir em banco de dados, seria necessário criar uma classe específica que fizesse essa implementação

### Controles

Na pasta de controles, temos a implementação dos endpoints do FastAPI, ou seja, é uma etapa em que a dependência do framework precisa ser explicitada. Aqui são criados os schemas necessários para operação da API e ao criar uma instância da classe *TarefaUseCase* precisamos definir qual a *Infraestrutura* que será utilizada, nesse caso, o armazenamento em memória

## Executando a Aplicação

Para executar a aplicação, deveremos usar o arquivo main.py, sendo necessário instalar as dependências constantes no arquivo requirements.txt

```bash

python main.py

```