from django.urls import path
from . import views


app_name = "mainapp"

urlpatterns = [
    path("index/", views.index_view),
    path("create/coders/suzanna/", views.create_view),
    path("detail/<str:product_id>/<int:coders_id>/", views.detail_view),

    path("products/list/", views.product_list_view, name="list"),
    path("products/list2/", views.product_list_view, name="list2"),
    path("products/create/", views.product_create_view, name="create"),
    path("products/add/", views.product_create_add_view, name="add"),
    path("products/detail/<id>/", views.product_detail_view, name="detail"),
    path("products/update/<id>/", views.product_update_view, name="update"),
]


