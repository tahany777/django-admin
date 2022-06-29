from django.contrib import admin
from . import models

class BlogAdminArea(admin.AdminSite):
    site_header = 'Bolg Admin Area'

blog_site = BlogAdminArea(name='BlogAdmin')

# Register your models here.
admin.site.register(models.Post)
blog_site.register(models.Post)