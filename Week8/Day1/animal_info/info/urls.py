from django.urls import path
from . import views
urlpatterns = [
	path('animal/<int:animal_id>',views.animal, name='animal'),
	path('family/<int:fam_id>',views.family,name='family')
]