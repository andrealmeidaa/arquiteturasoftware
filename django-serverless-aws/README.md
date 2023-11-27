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