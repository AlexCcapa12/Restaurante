from django.urls import path
from . import views
urlpatterns = [
    path('platos_list/', views.platos_list, name='post_list'),
    path('platos_search/', views.platos_search, name='post_search'),
    # URLs serializers
    path('platos_list_serializer/', views.ListPlatosSerializer(), name="platos_lis_srr"),
    
]


