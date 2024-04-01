from django.contrib import admin
from .models import Valk, Signet, Build, SignetCategory

admin.site.register(Valk)
admin.site.register(SignetCategory)
admin.site.register(Signet)
admin.site.register(Build)