# API Silvertec


## Tecnologias Usadas:
- Python 3.6
- Django (2+)
- Django REST Framework
- Django Rest Auth
- Docker
- Heroku

## Instalação

Instale as dependências no ambiente virtual


```
	pip install -r requirements.txt
	
```
## Estrutura

A API está dividida em 2 sessões, onde a primeira é responsável por listar todos pedidos e adicionar um novo pedido baseado nos computadores criados.
A segunda parte é a criação dos computadores, onde o primeiro endpoint lista todos os computadores montados e no segundo detalha um computador baseado no seu id.

Aqui temos uma tabela pra simplificar:

Endpoint | Método HTTP  | CRUD  | Resultado
-- | -- |-- |--
`montar/` | GET | READ | Lista todos computadores 
`detalhar/:id` | GET | READ | Lista um único computador
`montar/`| POST | CREATE | Cria um novo computador
`detalhar/:id` | PUT | UPDATE | Edita as peças de um computador
`detalhar/:id` | DELETE | DELETE | Deleta um computador
`pedidos/:` | GET | READ | Mostra todos pedidos
`pedidos/:` | POST | CREATE | Cria um novo pedido
`pedidos/:id` | GET | READ | Detalha um pedido específico

## Uso

Para testar e criar as requisições, pode-se usar o Postman ou Insomnia, caso queira testar já em produção acesse :


Link| Função
-- | --
`https://silvertecdeploy.herokuapp.com/pedidos` | Listar todos pedidos
`https://silvertecdeploy.herokuapp.com/pedidos/<id>` | Detalha Pedido
`https://silvertecdeploy.herokuapp.com/montar` | Lista computadores já montados e cria novo computador
`https://silvertecdeploy.herokuapp.com/detalhar/<id>`| Detalha Computador


OBS - A validação via token no ambiente Heroku está desativada para melhor experiência visual no teste

Usuário Teste:

    Usuário: teste
    Senha: 123De456
    Token: 73cfaa160c6e8d079dd8d123a8aa4465c8645553


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
	http http://127.0.0.1:8000/listar/ "Authorization: Token 73cfaa160c6e8d079dd8d123a8aa4465c8645553"
```


## Login e Tokens

Para cadastrar um token é possível acessando o endpoint abaixo:
```
	http http://127.0.0.1:8000/rest-auth/login/ username="teste" password="123De456"
```
Que depois de logado é retornado o token
```
{
    "key": "73cfaa160c6e8d079dd8d123a8aa4465c8645553"
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
-   Para ter as peças de montagem é nessesário adicioná-las no banco (Via Django Admin)


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
