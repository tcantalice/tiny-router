# Flask-Router
Flask-Router é um roteador de caminhos para aplicações [Flask](https://github.com/pallets/flask). A biblioteca fornece um conjunto de normas simples para registrar as rotas da aplicação.

## Criando rotas

Estrutura do marcador de rotas é simples. Uma lista de dicionários contendo os elementos chave para a criação de uma 'rule' na aplicação Flask.

* **endpoint** (Obrigatório) - Nome utilizado para identificar a rota. Em caso de endpoints com múltiplos termos, recomendado separá-los por ponto ou sublinhado.
* **rule** (Obrigatório) - Caminho para um recurso específico
* **view** (Obrigatório) - Função ou classe que irá manipular a requisição
* **methods** - Métodos HTTP para chamada da rota

Exemplo:
```python
routes = [
    {
        'endpoint': 'rota.exemplo',
        'rule': '/exemplo',
        'view': view_exemplo,
        'methods': ['GET', 'POST'] 
    }
]
```

Esta estrutura deve seguir este fluxo.
É opcional (mas recomendado) o atributo ```methods```.

Caso não sejam informados os métodos o padrão será ```['GET']```

Exemplo:
```python
routes = [
    {
        ...
        'methods': ['GET']
    }
]
```

Pode utilizar o construtor de rotas - RouteBuilder

Código:
```python
from flask_router.router import RouteBuilder as Route

Route('user.index').rule('/user').view(hello)
    .methods('GET').build()
```
Esta função irá funcionar igual ao bloco:
```python
{
    'endpoint': 'user.index',
    'rule': '/user',
    'view': hello,
    'methods': ('GET')
}
```

## Registrando as rotas
Primeiro cria uma instância do roteador
```python
from flask import Flask
from flaskrouter import Router

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