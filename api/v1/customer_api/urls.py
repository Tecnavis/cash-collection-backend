from django.urls import path
from . import views

app_name = 'customer_api'


urlpatterns = [
    path("customers/", views.customer_list, name="customer_list"),
    path("customers/<int:id>/", views.customer_detail, name="customer_detail"),
    path("customers/<int:id>/delete/", views.customer_delete, name="customer_delete"),
    path("customers/create/", views.customer_create, name="customer_create"),
    path("customers/<int:id>/update/", views.customer_update, name="customer_update"),

]