from django.urls import path
from . import views

app_name = 'cashcollection_api'


urlpatterns = [
    # path("cashcollections/", views.cashcollection_list, name="cashcollection_list"),
    # path("cashcollections/<int:id>/", views.cashcollection_detail, name="cashcollection_detail"),
    # path("cashcollections/<int:id>/delete/", views.cashcollection_delete, name="cashcollection_delete"),
    path("cashcollections/create/", views.enroll_customer_in_scheme, name="cashcollection_create"),
    # path("cashcollections/<int:id>/update/", views.cashcollection_update, name="cashcollection_update"),

    path("schemes/", views.scheme_list, name="scheme_list"),
    # path("schemes/<int:id>/", views.scheme_detail, name="scheme_detail"),
    # path("schemes/<int:id>/delete/", views.scheme_delete, name="scheme_delete"),
    # path("schemes/<int:id>/update/", views.scheme_update, name="scheme_update"),
    path("schemes/create/", views.scheme_create, name="scheme_create"),

    path("cashcollection/create/", views.cash_collection_create, name="cash-collection-entry"),

] 