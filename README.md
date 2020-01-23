# Tiny Router
Tiny Router é um roteador de caminhos para aplicações [Flask](https://github.com/pallets/flask). A biblioteca centraliza a definição e gerenciamento das rotas utilizadas na aplicação, criar, editar, remover ou trocar controladores facilmente evitando conflitos.

## Criando rotas

Uma rota é representada pela classe ```Route```. Ela possui os seguinte atributos:

* **endpoint** - Nome utilizado para identificar a rota. Em caso de endpoints com múltiplos termos, recomendado separá-los por ponto ou sublinhado.
* **rule** - Caminho para um recurso específico
* **view** - Função ou classe que irá manipular a requisição
* **methods** - Métodos HTTP para chamada da rota (Default: ```{'GET'}```)
* **parameters** - Parâmetros que podem ser passados na url.

Ao criar uma rota apenas são obrigatórios ```endpoint```, ```rule``` e ```view```.

Exemplo de uma rota simples:
```python
from tinyrouter import Route
from views import user_index

Route('user.index', '/user', user_index)
```
Por padrão, as rotas são definidas para aceitas apenas o método ```GET```. Entretanto outros métodos podem ser definidos, ou até mais de um.
```python
from tinyrouter import Route
from views import user_index

# Definição dos métodos
methods = ['GET', 'POST']

Route('user.index', '/user', user_index, methods)
```
## Registrando as rotas

Primeiro cria-se uma instância do roteador
```python
from flask import Flask
from tinyrouter import Router

app = Flask(__name__)
router = Router(app)
```

E invoca o método ```register``` passando a lista de rotas que deseja registrar na aplicação
```python
'''
Importaçãoes anteriores
'''
from my_app.routes import routes

'''
 Instância da aplicação e do roteador
'''
router.register(routes)
```

Pronto! As rotas agora estão registradas na aplicação.

É possível registrar vários grupos de rotas.
```python
from webapp.routes import routes as web_routes
from api.routes import routes as api_routes

router.register(web_routes)
router.register(api_routes)
```
Ou ainda...
```python
router.register(web_routes, api_routes)
```

## Funções auxiliares
*A FAZER*
## Dicas de Uso
1. Utilizar um arquivo de rotas para cada parte da aplicação. Ex.:
```python
# ./clientes/routes.py
from tinyrouter import Route
from .views

routes = [
    *route_prefix('/cliente',
        Route('cliente.index', '/', views.index),
        Route('cliente.show', '/<int:id>', views.show),
        Route('cliente.create', '/create', views.create, ['GET', 'POST'])
    )
]
```
```python
# ./app.py
from flask import Flask
from tinyrouter import Router
from clientes.routes import routes as rotas_clientes

app = Flask(__name__)
router = Router(app)
router.register(rotas_clientes)
```