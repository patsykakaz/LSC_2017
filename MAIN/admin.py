#-*- coding: utf-8 -*-

from copy import deepcopy
from django.contrib import admin
from mezzanine.pages.admin import PageAdmin
from .models import *

from mezzanine.blog.admin import BlogPostAdmin
from mezzanine.blog.models import BlogPost


client_fieldsets = deepcopy(PageAdmin.fieldsets)
client_fieldsets[0][1]["fields"].insert(-1, "logo")
# client_fieldsets[0][1]["fields"].insert(-1, "illustration")
client_fieldsets[0][1]["fields"].insert(-1, "level")
class ClientAdmin(PageAdmin):
    fieldsets = client_fieldsets

campagne_fieldsets = deepcopy(PageAdmin.fieldsets)
campagne_fieldsets[0][1]["fields"].insert(-1, "illustration")
campagne_fieldsets[0][1]["fields"].insert(-1, "baseline")
campagne_fieldsets[0][1]["fields"].insert(-1, "clientKey")
campagne_fieldsets[0][1]["fields"].insert(-1, "level")
class CampagneAdmin(PageAdmin):
    fieldsets = campagne_fieldsets

worker_fieldsets = deepcopy(PageAdmin.fieldsets)
worker_fieldsets[0][1]["fields"].insert(-1, "picture")
worker_fieldsets[0][1]["fields"].insert(-1, "job")
worker_fieldsets[0][1]["fields"].insert(-1, "level")
worker_fieldsets[0][1]["fields"].insert(-1, "linkedin")
worker_fieldsets[0][1]["fields"].insert(-1, "twitter")
class WorkerAdmin(PageAdmin):
    fieldsets = worker_fieldsets



fakeBlog_fieldsets = deepcopy(PageAdmin.fieldsets)
fakeBlog_fieldsets[0][1]["fields"].insert(-1, "baseline")
fakeBlog_fieldsets[0][1]["fields"].insert(-1, "illustration")
fakeBlog_fieldsets[0][1]["fields"].insert(-1, "content")
class FakeBlogGaleryInline(admin.TabularInline):
    model = FakeBlogGalery
class FakeBlogAdmin(PageAdmin):
    inlines = (FakeBlogGaleryInline,)
    fieldsets = deepcopy(fakeBlog_fieldsets)

admin.site.register(Client, ClientAdmin)
admin.site.register(Campagne, CampagneAdmin)
admin.site.register(Worker, WorkerAdmin)
admin.site.register(FakeBlog, FakeBlogAdmin)

