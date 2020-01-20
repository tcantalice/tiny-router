'''
Estrutura do marcador de rotas

routes = {
    {
        "endpoint": <value:str>,
        "route": <value:str>,
        "view": <value:callable>,
        "methods": <value:iterable> 
    }
}

Esta estrutura deve seguir este fluxo.
São opcionais (mas recomendados) 'endpoint' e 'methods'.

Exemplo.:
-> Caso não seja informado o endpoint o padrão será ''

routes = {
    {
        "endpoint": '',
        "route": <value:str>,
        "view": <value:callable>,
        "methods": <value:iterable>
    }
}

-> Caso não sejam informados os métodos o padrão será ['GET']
routes = {
    {
        "endpoint": <value:str>,
        "route": <value:str>,
        "view": <value:callable>,
        "methods": ['GET']
    }
}
'''

from views import hello_world
routes = [
    {
        "route": '/',
        "view": hello_world
    }
]