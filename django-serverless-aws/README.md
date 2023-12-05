# Django Rest Framework - Servless

O objetivo deste tutorial é apresentar um passo-a-passo para implantação de uma infraestrutura de backend, com Django Rest Framework, em uma arquitetura parcialmente baseada em microserviços, com o emprego de computação serverless e banco de dados gerenciado em nuvem. Neste tutorial utilizaremos AWS como plataforma de nuvem, através da experimentação no AWS Academy.

Pré-requisitos:

* Conhecimentos básicos de Git
* Conhecimentos de Python, Django Rest Framework
* Conhecimentos básicos de banco de dados (MySQL)

## Estrutura do Tutorial
1. Preparação do Ambiente de Desenvolvimento
2. Criação do Banco de Dados - RDS
3. Instalação de Dependências e Configuração
4. Codificação da API(Básico)
5. Implantação
6. Utilização

## Preparação do Ambiente de Desenvolvimento

Para desenvolvimento deste tutorial utilizaremos exclusivamente a infraestrutura em nuvem da AWS, não sendo necessário a instalação de nenhum aplicativo na sua máquina local. Só é necessário um browser e acesso a internet para execução do tutorial.

### AWS Academy

Para iniciar o uso, será necessário entrar no ambiente da [AWS Academy](https://awsacademy.instructure.com/), utilizando o e-mail escolar.ifrn.edu.br. Para o primeiro acesso, usem o link de convite enviado para criação da senha. Acessaremos o curso denominado AWS Academy Learner Lab.

Ao acessar o curso, clique em **Modules** --> **Launch AWS Academy Learner Lab** e aguarde o carregamento da tela. Após carregado clique em **Start Lab**. Esse procedimento irá ativar o ambiente de experimentação da AWS. Nesse ambiente o aluno tem direito a usar 100 dólares em serviços. Esse laboratório ficará disponível até 3 meses após o final da disciplina. Para saber os serviços disponíveis, clique [aqui](https://labs.vocareum.com/web/2930000/2384012.0/ASNLIB/public/docs/lang/en-us/README.html#services). Observe o texto que indica algumas orientações, que deve ser lidas para permitir o uso mais racional dos recursos, além das limitações inerentes. O ambiente estará disponível para uso quando ao lado da palavra AWS, tivermos um ponto verde. Quando isso acontecer, clique em AWS. Esse link nos leverá ao console AWS.

### Console AWS

O Console AWS é uma ferramenta que permite gerenciar os serviços de nuvem oferecidos pela AWS. A partir do Console acessaremos os gerenciadores dos serviços que precisaremos para esse tutorial. Parte das etapas de configuração serão feitas pela biblioteca Zappa, que introduziremos mais a frente. No escopo deste trabalho, utilizaremos diretamente os serviços AWS Cloud9, para criar o ambiente de desenvolvimento e o serviço AWS RDS, para criação de um banco de dados gerenciado na nuvem.

### AWS Cloud9

O serviço AWS Cloud9 permite a criação de um ambiente de desenvolvimento, composto por uma IDE WEB, que é um VS Code simplificado, atrelado a uma máquina virtual, onde poderemos executar nossos códigos, rodar testes e etc. Também é possível acessar essa máquina virtual a partir do seu VSCODE. Disponibilizo um tutorial para realizar esse procedimento aqui(TODO). 

Vamos iniciar a criação do nosso ambiente. Para isso, na parte superior do console, onde temos uma caixa de texto para buscar os serviços, digite Cloud9. Ao localizar o serviço clique em Cloud9. Ao abrir a tela do Cloud9, realize os seguintes procedimentos:

1. Clique em Criar Ambiente
2. Informe um nome. Sugestão: DevCloudPython
3. Deixe os campos Descrição e Tipo de Ambiente com os valores atuais
4. Na seção **Nova Instância do EC2** selecione a opção t2.medium, no campo **Tipos de Instância Adicionais**. Essa opção criará uma máquina virtual com 4GB de Memória RAM e 2 Unidades de processamento, que são mais do que suficientes para o que iremos desenvolver. Quanto mais recursos a máquina tiver, mais caro ela será.
5. Deixe a opção de Plataforma como sendo Amazon Linux 2 e Tempo Limite
6. Na opção Configurações de Rede, caso você deseje acessar sua máquina virtual pelo VSCODE na sua máquina, selecione aopção Secure Shell. Caso contrário, deixe a opção AWS Systems Manager (SSM) selecionada.
7. Deixe as opções adcionais conforme estão selecionadas
8. Clique no botão **Criar**

Aguarde a criação do ambiente. Se quiser saber mais o que você pode fazer com o AWS Cloud9, clique [aqui](https://docs.aws.amazon.com/pt_br/cloud9/latest/user-guide/ide.html).

Após a criação do ambiente, lembre-se de criar o virtual env do Python, clonar o repositório e configurar as informações do git para permitir a realização dos commits.

## Banco de Dados na Nuvem - RDS

Para o exemplo iremos utilizar o banco de dados MySQL usando um serviço de gerenciamento de banco de dados da AWS, chamado [Amazon RDS](https://docs.aws.amazon.com/rds/?nc2=h_ql_doc_rds). Esse serviço permite criar um banco de dados gerenciável, o que significa que você não precisa fazer configurações de baixo nível para administrar o banco de dados.

### Criando o Banco de Dados

Para criar o banco de dados, vamos acessar o serviço através do console AWS. Busce por RDS, clique no serviço. Ao entrar na página principal, clique em **Criar Banco de Dados**.

No assistente de criação iremos preencher as seguintes opções:

1. Escolha Criação Padrão
2. Em Opções de Mecanismo escolha MySQL
3. Em Modelos escolha Nível Gratuito
4. Em Configurações, no campo **Identificador de Instância de Banco de Dados** defina o nome da instância. Observar que aqui é nome da instância do servidor de banco de dados e não de um banco de dados em si. Sugiro que coloque o nome db_<nome_Projeto>
5. Em Nome do Usuário principal, você pode deixar admin ou trocar. Fica a seu critério.
6. Defina senha principal e confirme
7. Na seção conectividade, na opção **Acesso Público** escolha Sim. Isso vai permitir que o banco possa ser acessado inclusive da sua própria máquina. Através de grupos de segurança poderemos restringir esse acesso. Essa configuração será feita mais a adiante.
8. Na seção configuração adicional, preencha o campo **Nome do banco de dados inicial** com o nome desejado para o seu banco de dados. Sugiro usar a sigla da aplicação.
9. Desmarque a opção **Habilitar Backups Automatizados**
10. Confira as informações e clique no botão **Criar Banco de Dados**

O processo de criação da instância pode demorar alguns minutos. 

### Configurações de Segurança

Um dos passos adicionais é permitir com que a nossa instância do EC2, onde roda nosso ambiente de desenvolvimento, consiga acessar o banco de dados. Para isso, precisaremos informar no grupo de segurança associado ao banco de dados, que a instância pode fazer o acesso.

Para realizar essa operação, siga os seguintes passos:

1. Clique na instância do banco de dados
2. Localize a aba **Segurança e Conexão** e localize **Grupos de segurança da VPC** e clique no link do grupo
3. Na listagem de grupos de segurança, clique no grupo de segurança listado.
4. Na aba **Regras de Entrada**, localize o botão **Editar Regras de Entrada**
5. Clique em **Adicionar Regra**. 
    1. Na primeira opção escolha **MySQL/Aurora**
    2. Deixa a opção personalizado
    3. No campo de busca, procure por Grupos de Segurança e escolha opção que consta aws-cloud9-<Nome do ambiente>.
    4. Depois clique em salvar.
Para testar a conexão com o MySQL. Iremos tentar uma conexão via terminal. Volte a aba do navegador em que o Cloud9 está aberto, abra uma seção de terminal e tente executar o seguinte comando:

```
mysql --host=[host_rds] --user=admin -p
```

Onde host rds é o endereço do endpoint disponível após a criação do banco. Após digitar a senha, deve ser aberto o terminal do cliente mysql. Execute o comando ```show databases;``` para listar os bancos de dados criados.

## Configurando Aplicação para acessar o Banco de Dados

Agora devemos configurar nossa aplicação Django Rest para acessar o banco de dados recém-criado. Para isso, realizaremos os seguintes passos:

1. Instale as dependências necessárias para execução do projeto. Você pode utilizar o arquivo requirements disponível [aqui](https://github.com/andrealmeidaa/arquiteturasoftware/blob/django-aws-microservices/django-serverless-aws/adocato/requirements.txt). Só observe se a sua aplicação precisa de alguma biblioteca adicional.
2. Na pasta do projeto, onde fica o arquivo settings.py crie um arquivo chamado db.cnf, que constará as informações de conexão com o banco. Sugiro que esse arquivo seja incluído no seu .gitignore, para evitar que você salve credenciais no seu repositório. Um template dele pode se encontrado [aqui](https://github.com/andrealmeidaa/arquiteturasoftware/blob/django-aws-microservices/django-serverless-aws/adocato/adocato/template_db.cnf).
3. No arquivo settings.py, realize as seguintes modificações
    1. Adicione os seguintes imports
    ```python
        import configparser
        import pymysql
    ```
    2. Adicione a seguinte linha no código. Em função de uma incompatibilidade do motor das funções Lambdas é necessários trocar a biblioteca comumente usada para lidar com o MySQL, usando a lib [PyMYSQL](https://pypi.org/project/pymysql/). Em seguida indique onde está o arquivo com as configurações de acesso ao banco de dados. Troque <projeto> pelo nome da pasta onde está o arquivo. Além disso, permita que qualquer host faça requisições a sua aplicação.
    ```python
        pymysql.install_as_MySQLdb()
        #Abrir o arquivo de configuração
        config=configparser.ConfigParser()
        config.read(os.path.join(BASE_DIR, '<projeto>/db.cnf'))
        #Localize a linha e faça o ajuste
        ALLOWED_HOSTS = ['*']
    ```
    3. Localize a configuração de conexão com o banco de dados e troque para o seguinte código
    ```python
        DATABASES = {
            "default": {
                "ENGINE": "django.db.backends.mysql",
                "NAME": config['mysql']['database'],
                "HOST": config['mysql']['host'],
                "USER": config['mysql']['user'],
                "PASSWORD": config['mysql']['password'],
                "PORT": config['mysql']['port'],
                }
        }
    ```
4. O próximo passo é executar o a migração do modelos para que as tabelas sejam criadas no banco de dados. Lembre-se que se você fez alguma alteração nos módulos é necessário rodar o comando makemigrations primeiro.
5. Depois de realizada a migração, execute a aplicação ```python manage runserver 8080``` para que seja possível acessar a aplicação. Em seguida, clique no botão **Preview** e depois clique no botão **Pop-out in new Window**. A aplicação deverá estar disponível para uso.

## Implantando a aplicação serverless com Zappa

Nesse momento temos a aplicação rodando em uma máquina virtual na Nuvem, acessando um banco de dados gerenciado. Agora iremos implantar a aplicação em formato [serverless](https://www.redhat.com/pt-br/topics/cloud-native-apps/what-is-serverless), com [Zappa](https://github.com/zappa/Zappa). Zappa permite implantar aplicações web Python, seja com Django, Flask ou FASTAPI, no formato serverless. Essa dependência já foi instalada anteriormente, se você usou o arquivo de requirements fornecido.

### Inicializando Zappa

Para realizar as configurações iniciais, acesse o terminal na raiz do projeto, onde está localizado o arquivo manage.py e execute os seguintes passos:

1. Execute o comando ```zappa init```. Ele irá solicitar a confirmação de algunas informações.
    1. Nome do ambiente, que pode ficar como **dev**
    2. S3 bucket name. Esse é o nome do bucket que irá guardar os arquivos que serão colocados na nuvem. S3 é um serviço da AWS, parecido com Onedrive, Dropbox, entre outros, que permite o armazenamento de arquivos. 
    3. Ao ser perguntado se a implantação deve ser global, informe no
    4. Se tudo correu bem você deverá receber as informações de que um arquivo de configurações do zap foi criado, além de instruções de comandos a serem executados.
2. Após a criação do arquivo e em função de limitações do ambiente da AWS Academy, precisaremos realizar algumas modificações no arquivo, de forma a garantir o funcionamento. Localize o arquivo zappa_settings.json e faça as alterações para que ele fique semelhante ao conteúdo abaixo:
    ```json
    {
        "dev": {
            "aws_region": "us-east-1",
            "django_settings": "seuprojeto.settings",
            "profile_name": "default",
            "project_name": "seuprojeto",
            "runtime": "python3.10",
            "s3_bucket": "zappa-seuprojeto-dev",
            "manage_roles":false,
            "role_name": "LabRole",
            "role_arn": "xxxx"
        }
    }
    ``````
3. O atributo **role_arn** diz respeito a identificação do papel usado pela AWS para executar as funções lambda. Como o ambiente do AWS Academy é restrito, é necessário usar as informações do ambiente. Para localizar o role_arn da sua conta, acesse o consol AWS, busque por IAM, em seguida Funções, localize LabRole, clique na função e identifique o campo ARN. Copie esse campo para o arquivo de configurações.

### Realizando Implantação

Depois de feita a configuração, devemos aplicar os comandos necessários para execução da aplicação. Para realizar a implantação, execute o comando ```zappa deploy dev```. Esse comando só precisa ser feito uma única vez. Caso o código seja atualizado, execute o comando ```zappa update dev``` para atualizar a implantação. 
Caso o processo ocorra sem problemas, será informando o endpoint do API GAteway por onde as requisições podem ser feitas. Para testar, use o curl ou postman para emitir as requisições.


