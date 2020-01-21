from flask import Flask
from re import findall

class RuleError(Exception): ...
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
        if len(routes) == 1:
            routes = routes[0]
        else:
            routes = self.__unpack_routes(routes)

        for group in routes:
            try:
                for rule in group:
                    # Validate rule fields
                    self.__validate_rule(rule)

                    # Get values from rule
                    endpoint = rule.get('endpoint', '')
                    route = rule.get('route')
                    view = rule.get('view')
                    methods = rule.get('method', ['GET'])
                    
                    # Add route to application
                    self.__app.add_url_rule(route, \
                        endpoint, \
                        view, \
                        methods=methods)
                    
                    self.__endpoints.add(endpoint)
            except RuleError as e:
                self.__register_error(e)            

    def __validate_rule(self, rule: dict):
        
        if findall(r'[^\.A-z]', rule.get('endpoint', '')):
            raise InvalidCharsError('endpoint')
        
        if not rule.get('route', None):
            raise FieldRequiredError('route')
        
        if not rule.get('view', None):
            raise FieldRequiredError('view')
        
        if not callable(rule.get('view')):
            raise InvalidValueError('view')
    

    def __register_error(self, error):
        '''
            Retorno de error do registrador
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
    
    __endpoint = ''
    __rule = ''
    __view = None
    __methods = {'GET'}
    
    __parameters = dict()

    def __init__(self, endpoint, rule, view, methods={'GET'}):
        self.__endpoint = endpoint
        self.view(view)
        self.__rule = rule


    def view(self, view):
        '''Set view for route
        '''
        # Required view
        if not view: raise Exception
        
        # Required callable view
        if not callable(view): raise TypeError('View needs to be callable')

        self.__view = view

    def rule(self, rule):
        '''Set rule pattern for route
        '''
        if rule[:1] != '/':
            rule = '/' + rule
        
        
        self.__rule = rule
        return self
    
    def methods(self, *methods):
        '''Set methods for route
        '''
        if not methods:
            # TODO: Specific exception
            raise Exception
        self.__methods = set(method.upper() for method in method)
        return self
    
    def build(self):
        # TODO: Specific exceptions
        if not self.__rule:
            raise Exception
        
        if not self.__view:
            raise Exception

        return {
            'endpoint': self.__endpoint,
            'rule': self.__rule,
            'view': self.__view,
            'methods': self.__methods
        }

    