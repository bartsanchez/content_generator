from django import http
from django.contrib import admin

from layouts import models


class LayoutSectionAdmin(admin.TabularInline):
    model = models.LayoutSection


class LayoutAdmin(admin.ModelAdmin):
    inlines = (LayoutSectionAdmin,)
    actions = ('generate_text',)

    def generate_text(self, request, queryset):
        if queryset.count() != 1:
            self.message_user(request, 'You should select only 1 layout!')
        else:
            layout = queryset.first()
            response = http.HttpResponse(
                layout.generate_text(),
                content_type='text/plain',
            )
            return response


class ContentInlineAdmin(admin.TabularInline):
    model = models.Content


class SectionAdmin(admin.ModelAdmin):
    inlines = (ContentInlineAdmin,)


admin.site.register(models.Layout, LayoutAdmin)
admin.site.register(models.Section, SectionAdmin)
admin.site.register(models.Content)
