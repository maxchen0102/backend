
from pyramid.view import view_config
from pyramid.response import Response
from sqlalchemy.exc import SQLAlchemyError


from webargs import fields
from webargs.pyramidparser import use_args
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
def hello_world(request):
    print('Incoming request')
    params = request.params
    res1=params.get("id")
    res2 = params.get("name")
    flag = params.get("flag")
    data2 = request.json_body
    name = data2.get('name')
    print(name)

    data2["d"] = 123
    data2["status"] = "ok"
    data2["s"]="被增加了"
    data2['params']=res2

    if flag == "1" :
        return data2
    if flag == "0" :
        return data2



@view_config(route_name='example_route', renderer='json')
def example_view(request):
    # 获取查询参数
    params = request.params
    param1 = params.get('flag')

    # 获取 JSON 数据
    json_data = request.json_body

    json_data["name"]= "no_guys"
    json_data["age"]=123123

    # 做一些处理


    # 返回结果
    return json_data




# 在您的视图文件中引入参数验证规则类，并使用它
from pyramid.view import view_config
from webargs.pyramidparser import use_args


@view_config(route_name='example_route2', renderer='json')
def post(request, payload):


    data={
        "name":"data",
        "city":"日本",
        'age':1203123,
    }
    return data

    # 在这



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
