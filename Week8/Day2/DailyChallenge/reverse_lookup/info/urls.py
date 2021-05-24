from django.urls import path
from .import views  

urlpatterns = [
    path('name/<str:name>',views.name, name='name'),
    path('phone/<str:phone>',views.phone, name='phone'),
]
