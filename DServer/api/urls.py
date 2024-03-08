from django.urls import path
from . import views 

urlpatterns = [
    path("",views.api_home),
    path("api_post",views.api_post),
    path("product",views.get_product),
    path("product_add",views.add_product),
    path("prodcut_delete",views.delete_prodcut_by_id),
    path("update_product",views.update_product)
]
