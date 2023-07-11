from django.contrib import admin
from users.models import User
from articles.models import Review, Ticket


admin.site.register(User)
admin.site.register(Review)
admin.site.register(Ticket)

# Register your models here.
