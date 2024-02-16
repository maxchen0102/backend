from waitress import serve
from pyramid.config import Configurator
from pyramid.response import Response
from pyramid.view import view_config
import json



@view_config(route_name='hello', renderer='json')
def hello_world(request):
    print('Incoming request')
    data = {"key":"chris"}
    return data


if __name__ == '__main__':
    with Configurator() as config:
        config.add_route('hello', '/')
        config.add_view(hello_world, route_name='hello')
      
        app = config.make_wsgi_app()
    serve(app, host='0.0.0.0', port=6543)