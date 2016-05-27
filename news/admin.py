from django.contrib import admin

from .models import News
from .models import Author

admin.site.register(Author)
admin.site.register(News)