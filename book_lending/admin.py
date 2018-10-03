from django.contrib import admin
from .models import People, Book, BookLending

adminModels = [People, Book, BookLending]
admin.site.register(adminModels)

