from django.contrib import admin

# Register your models here.
from favorites.models import Favorite


admin.site.register(Favorite)