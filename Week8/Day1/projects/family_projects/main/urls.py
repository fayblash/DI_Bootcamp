from django.urls import path
from . import views

urlpatterns=[
    path('', views.homepage),
    path('about/<str:name>',views.about),
    path('myposts/<int:person_id>',views.myposts),
    path('myposts/',views.myposts),
]
