# API Silvertec


## Tecnologias Usadas:
- Python 3.6
- Django (2+)
- Django REST Framework
- Django Rest Auth
- Docker
- Heroku

## Instalação
```
	pip install -r requirements.txt
	
```
## Estrutura

A API está dividida em 2 sessões, onde a primeira é responsável por listar todos pedidos e adicionar um novo pedido baseado nos computadores criados.
A segunda parte é a criação dos computadores, onde no primeiro endpoint lista todos os computadores montados e no segundo detalha um computador baseado no seu id.

Aqui temos uma tabela pra simplificar o fluxo:

Endpoint | Método HTTP  | CRUD  | Resultado
-- | -- |-- |--
`montar/` | GET | READ | Lista todos computadores 
`detalhar/:id` | GET | READ | Lista um único computador
`montar/`| POST | CREATE | Cria um novo computador
`detalhar/:id` | PUT | UPDATE | Edita as peças de um computador
`detalhar/:id` | DELETE | DELETE | Deleta um computador
`pedidos/:` | GET | READ | Mostra todos pedidos
`pedidos/:` | POST | CREATE | Cria um novo pedido


## Uso

Para testar e criar as requisições, pode-se usar o Postman ou Insomnia, caso queira testar já em produção acesse :
https://silvertecdeploy.herokuapp.com/


Outra opção é o httpie :
```
pip install httpie
```

Inicie o servidor Django:
```
	python manage.py runserver
```
Apenas usuários autenticados podem recuperar as requisições:
```
	http  http://127.0.0.1:8000/montar/
```
Este é o retorno, caso não esteja autenticado:
```
 {  "detail":  ""Você precisa estar logado !"  }
```
Acessando com as credenciais, você consegue o retorno da requisição:
```
	http http://127.0.0.1:8000/listar/ "Authorization: Token 7530ec9186a31a5b3dd8d03d84e34f80941391e3"
```


## Login e Tokens

Para cadastrar um token é possível acessando o endpoint abaixo:
```
	http http://127.0.0.1:8000/rest-auth/login/ username="admin" password="admin"
```
Que depois de logado é retornado o token
```
{
    "key": "2d500db1e51153318e300860064e52c061e72016"
}
```
**Todas requisições precisam ser validadas via token**

É possível criar novos usuários. (password1 e password2 devem ser iguais)
```
http POST http://127.0.0.1:8000/rest-auth/registration/ username="USUARIO" password1="SENHA" password2="SENHA"
```
E é possível fazer logout:
```
http POST http://127.0.0.1:8000/rest-auth/logout/ "Authorization: Token <SEU_TOKEN>" 
```

Algumas restrições da API:
-   Os computadores criados são associados ao seu criador.
-   Apenas usuários autenticados conseguem criar e listar.
-   O servidor retorna caso alguma restrição de montagem ocorra
-   Todas requisições sem autenticação não são retornadas
-   Para ter as peças de montagem é nessesário adicioná-las no banco(Via Django Admin)


### Deploy em containers

Caso queira fazer um deploy em container é possível através do docker-compose, onde possui todas dependências nessesárias para poder executar.

```
docker-compose up -d --build
```


### Paginação

A API suporta paginação, por padrão as requisições tem um tamanho de page_size=10, mas é possível editar esse valor caso necessário

```
http http://127.0.0.1:8000/montar/?page=1 "Authorization: Token <SEU_TOKEN>"
http http://127.0.0.1:8000/montar/?page=3&page_size=15 "Authorization: Token <SEU_TOKEN>"
```
