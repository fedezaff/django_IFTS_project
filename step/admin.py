from django.contrib import admin
from .models import Aziende, Competenze, Offerte, Offerte_competenze

# Register your models here.

admin.site.register(Aziende)
admin.site.register(Competenze)
admin.site.register(Offerte)
admin.site.register(Offerte_competenze)
