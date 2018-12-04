from django.contrib import admin

from layouts import models


class LayoutSectionAdmin(admin.TabularInline):
    model = models.LayoutSection


class LayoutAdmin(admin.ModelAdmin):
    inlines = (LayoutSectionAdmin,)


class ContentInlineAdmin(admin.TabularInline):
    model = models.Content


class SectionAdmin(admin.ModelAdmin):
    inlines = (ContentInlineAdmin,)

admin.site.register(models.Layout, LayoutAdmin)
admin.site.register(models.Section, SectionAdmin)
admin.site.register(models.Content)
