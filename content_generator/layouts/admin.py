from django.contrib import admin

from layouts import models


class LayoutSectionAdmin(admin.TabularInline):
    model = models.LayoutSection


class LayoutAdmin(admin.ModelAdmin):
    inlines = (LayoutSectionAdmin,)

admin.site.register(models.Layout, LayoutAdmin)
admin.site.register(models.Section)
