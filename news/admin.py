from django.contrib import admin

from .models import News, Menu
from .models import Author

admin.site.register(Author)
admin.site.register(News)
admin.site.register(Menu)