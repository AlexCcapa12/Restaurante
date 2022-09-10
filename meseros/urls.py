from django.urls import path
from . import views
urlpatterns = [
    path('meseros_list/', views.meseros_list, name='post_list')

]
