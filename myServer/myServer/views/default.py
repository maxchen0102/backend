from pyramid.view import view_config
from pyramid.response import Response
from sqlalchemy.exc import SQLAlchemyError

from .. import models
import json

@view_config(route_name='home', renderer='myServer:templates/mytemplate.mako')
def my_view(request):
    try:
        query = request.dbsession.query(models.MyModel)
        one = query.filter(models.MyModel.name == 'one').one()
    except SQLAlchemyError:
        return Response(db_err_msg, content_type='text/plain', status=500)
    return {'one': one, 'project': 'myServer'}

@view_config(route_name='hello', renderer='json')
def hello_world(request ):
    print('Incoming request')
    data = {"key" : "chris"}
    data2 = request.json_body
    name = data2.get('name')
    name=1
    print(name)
    a=1
    b=2
    d=a+b
    data["d"] = d
    return data







db_err_msg = """\
Pyramid is having a problem using your SQL database.  The problem
might be caused by one of the following things:

1.  You may need to initialize your database tables with `alembic`.
    Check your README.txt for descriptions and try to run it.

2.  Your database server may not be running.  Check that the
    database server referred to by the "sqlalchemy.url" setting in
    your "development.ini" file is running.

After you fix the problem, please restart the Pyramid application to
try it again.
"""
