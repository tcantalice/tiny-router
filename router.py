from Routes import routes
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

    __routes = routes
    __app = None
    
    def __init__(self, app: Flask):
        self.__app = app
    
    def register(self):
        for group in self.__routes:
            try:
                for rule in group:
                    # Validate rule fields
                    self.__validate_rule(rule)

                    # Get values from rule
                    endpoint = rule.get('endpoint', '')
                    route = rule.get('route')
                    view = rule.get('view')
                    methods = rule.get('method', ['GET'])
                    
                    self.__app.add_url_rule(route, \
                        endpoint, \
                        view, \
                        methods=methods)
            except RuleError as e:
                self.__register_error(e)
                

    def __validate_rule(self, rule: dict):
        if findall(r'[\d\W]', rule.get('endpoint', '')):
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
        
        
