from flask import Flask
from re import findall, match
from re import compile as compile_re


class RuleError(Exception):
    ...


class FieldRequiredError(RuleError):
    def __init__(self, field_name):
        self.message = 'Field "{}" is required for route rule'.format(
            field_name
        )


class InvalidCharsError(RuleError):
    def __init__(self, field_name):
        self.message = 'Field "{}" contains invalid characters'.format(
            field_name
        )


class InvalidValueError(RuleError):
    def __init__(self, field_name):
        self.message = 'Field "{}" contains invalid value'.format(
            field_name
        )


class Router():
    __app = None
    __endpoints = set()

    def __init__(self, app: Flask):
        self.__app = app


    def register(self, *routes):
        '''Registra as rotas dentro da aplicação
        '''
        if len(routes) == 1:
            routes = routes[0]
        else:
            routes = self.__unpack_routes(routes)

        for group in routes:
            try:
                for route in group:
                    # Validate rule fields
                    self.__validate_route(rule)

                    # Get values from rule
                    endpoint = route.get('endpoint', '')
                    rule = route.get('rule')
                    view = route.get('view')
                    methods = route.get('method', ['GET'])

                    # Add route to application
                    self.__app.add_url_rule(rule,
                                            endpoint,
                                            view,
                                            methods=methods)

                    self.__endpoints.add(endpoint)
            except RuleError as e:
                self.__register_error(e)


    def __validate_route(self, rule: dict):
        '''Validador da rota
        '''
        if findall(r'[^\.A-z]', rule.get('endpoint', '')):
            raise InvalidCharsError('endpoint')

        if not rule.get('route', None):
            raise FieldRequiredError('route')

        if not rule.get('view', None):
            raise FieldRequiredError('view')

        if not callable(rule.get('view')):
            raise InvalidValueError('view')


    def __register_error(self, error):
        '''Retorno de error do registrador
        '''
        if self.__app.config['DEBUG']:
            print(error)
        else:
            raise error


    def __unpack_routes(self, pack):
        unpacked = []
        for routes in pack:
            unpack += routes
        return unpacked


class Route():

    __slots__ = ('__endpoint', '__rule',
        '__view', '__methods',
        '__parameters',)

    def __init__(self, endpoint, rule, view, methods={'GET'}):
        self.__endpoint = endpoint
        self.view(view)
        self.rule(rule)
        self.methods(*methods)
        self.__parameters = dict()

    def view(self, view):
        '''Set view for route
        '''
        self.__view = view

    def rule(self, rule: str):
        '''Set rule pattern for route
        '''
        # Added slash on start if not found
        if not rule.startswith('/'):
            rule = '/' + rule

        self.__rule = rule

    def methods(self, *methods):
        '''Set methods for route
        '''
        if not methods:
            # TODO: Specific exception
            raise Exception
        self.__methods = set(method.upper() for method in methods)

    def __extract_parameters(self):
        '''Extract parameter from rule
        '''
        pattern = compile_re(r'<([A-z]+:)?([A-z_]+)>')

        paths = self.__rule.split('/')

        for path in paths:
            if not pattern.match(path):
                continue

            path = path.strip('<>')
            parameter = path.split(':') if path.find(':') else ['string', path]
            self.__parameters[parameter[1]] = parameter[0]

    def __str__(self):
        return '''{{
endpoint: '{}',
rule: '{}',
view: '{}',
methods: {}
}}'''.format(self.__endpoint,self.__rule,self.__view.__name__,repr(self.__methods))
    
    def __repr__(self):
        return str(self)