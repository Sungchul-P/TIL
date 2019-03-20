from django.contrib import admin
from .models import Article, Reporter, Publication
from .models import *

admin.site.register(Reporter)
admin.site.register(Article)
admin.site.register(Publication)
admin.site.register(Place)
admin.site.register(Restaurant)
admin.site.register(Waiter)
admin.site.register(Profile)