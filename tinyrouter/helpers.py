from .router import Route

def __route_builder(endpoint, rule, view, *methods):
    # TODO: Make documentation
    return Route(endpoint, rule, view, *methods)

def route_get(endpoint, rule, view):
    # TODO: Make documentation
    return __route_builder(endpoint, rule, view, 'GET')

def route_post(endpoint, rule, view):
    # TODO: Make documentation
    return __route_builder(endpoint, rule, view, 'POST')

def route_delete(endpoint, rule, view):
    # TODO: Make documentation
    return __route_builder(endpoint, rule, view, 'DELETE')

def route_put(endpoint, rule, view):
    # TODO: Make documentation
    return __route_builder(endpoint, rule, view, 'PUT')

def route_prefix(prefix, *routes):
    # TODO: Make documentation
    if not prefix.startswith('/'):
        prefix = '/' + prefix

    for n in range(len(routes)):
        routes[n].rule = prefix + routes[n].rule
    return routes
