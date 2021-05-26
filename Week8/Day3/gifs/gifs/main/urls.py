from django.urls import path
from .import views  

urlpatterns = [ 
    path('homepage/',views.homepage, name='homepage'),
    path('add_gif/', views.add_gif,name='add_gif'),
    path('add_category/', views.add_category,name='add_category'),
    path('category/<int:category_id>', views.single_category, name='single_category'),
    path('all_categories/', views.all_categories,name='all_categories'),
    path('gif/<int:gif_id>', views.gif,name='gif'),
]