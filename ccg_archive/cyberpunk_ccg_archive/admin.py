from django.contrib import admin
from ccg_archive.cyberpunk_ccg_archive import models

# Register your models here.

admin.site.register(models.Location)
admin.site.register(models.Sponsor)
admin.site.register(models.Image)
