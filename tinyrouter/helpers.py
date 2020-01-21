from .router import Route

def __route_builder(endpoint, view, rule, *methods):
    return Route(endpoint).rule(rule).view(view).methods(*methods).build()

def route_get(endpoint, view, rule):
    return __route_builder(endpoint, view, rule, 'GET')

def route_post(endpoint, view, rule):
    return __route_builder(endpoint, view, rule, 'POST')

def route_delete(endpoint, view, rule):
    return __route_builder(endpoint, view, rule, 'DELETE')

def route_put(endpoint, view, rule):
    return __route_builder(endpoint, view, rule, 'PUT')

def route_prefix(prefix, *routes):
    # TODO: Make documentation
    if prefix[:1] != '/':
        prefix = '/' + prefix

    routes = list(map(lambda route: prefix + route['rule'], routes))
    # TODO: Return unpacked routes
    return routes
