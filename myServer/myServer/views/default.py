
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


def verification(**kw):
    enable_keys=["chris","max","bob"]
    data = {k: kw[k] for k in kw if k in enable_keys}
    data["status"]="ok"
    return data 


@view_config(route_name='test_get', renderer='json')
def get(request):
    # 获取查询参数
    params= request.params
    flag=params["flag"]
    
    if flag =="1" : 
        json_data={
            "status":"chooose 1 "
        }
        return json_data
    if flag=="2" : 
        json_data2={
            "status":"choose 2 "
        }
        return json_data2 
    # 返回结果

@view_config(route_name='test_post', renderer='json')
def post(request):
    
    payload=request.json
    print(type(payload))
    
    payload_verify=verification(**payload)
    print(payload_verify)
    return payload_verify


