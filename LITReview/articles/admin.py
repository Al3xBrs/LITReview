from django.contrib import admin
from users.models import User
from articles.models import Review




admin.site.register(User)
admin.site.register(Review)

# Register your models here.
