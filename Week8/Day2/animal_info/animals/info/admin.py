from django.contrib import admin
from .models import Animal,Family,Person,Country,Passport
# Register your models here.
admin.site.register(Animal)
admin.site.register(Family)
admin.site.register(Person)
admin.site.register(Country)
admin.site.register(Passport)

