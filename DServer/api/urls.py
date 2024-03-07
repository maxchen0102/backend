from django.urls import path
from . import views 

urlpatterns = [
    path("",views.api_home),
    path("api_post",views.api_post)
]
