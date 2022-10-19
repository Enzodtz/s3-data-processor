# lambda-edesoft

Função lambda para processamento de dados utilizando SAM e ORM do SQLAlchemy.

### Ponderações Importantes

O Arquivo template utilizado não abrange a criação do banco de dados, nem grupos de segurança ou de rede. Poderia ser feito, e melhoraria a infraestrutura, mas por uma questão de agilidade, não foi priorizado. Além disso, as keys não estão sendo utilizadas como secrets, algo que poderia ser feito com mais tempo.

### Tecnologias Utilizadas

- Mensageria
- CloudFormation
- SAM (Serverless Application Model)
- ORM (SQLAlchemy)
- Python + Pandas

### Requisitos

- Um banco de dados público para que a função se conecte.
- Docker instalado
- Python 3.9
- SAM (Server Application Model)
- Credenciais AWS salvas de acordo com o link [https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-getting-started-set-up-credentials.html]() com permissões de S3, Lambda, CloudFormation, IAM etc.

### Deploy

Configure a string do banco em `template.yaml` de acordo com a seguinte forma: `DB_CONNECTION_STRING:<BANCO ex: postgresql>://<usuario>:<senha>@<host>:<porta>` e as keys da AWS.

Em seguida, execute os seguintes comandos:

```
sam build --use-container
sam deploy --guided
```

O segundo comando fará uma série de perguntas sobre a aplicação a ser subida:

- **Stack Name**: O nome da stack a ser criada no CloudFormation.
- **AWS Region**: A região da AWS a ser feito o deploy
- **Allow SAM CLI IAM role creation**: Permitir criação das roles do IAM automaticamente pelo SAM.
- **Save arguments to samconfig.toml**: Salvar respostas para o arquivo, evitando prompts posteriores

Após o comando, o endpoint ficará disponível no console.

### Testar

Para testar, basta subir um arquivo no bucket S3 criado, e verificar que o banco de dados já possuirá uma tabela com os registros, que serão atualizados de acordo com os uploads. Caso desejado, pode se fazer um request GET, informando os parâmetros pela query.

### Deletar Stack

Para deletar a aplicação criada, execute o seguinte comando:

```bash
aws cloudformation delete-stack --stack-name <stackname>
```
