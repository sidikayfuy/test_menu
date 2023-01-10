from django.contrib import admin
from .models import MenuObject, Menu


class MenuAdmin(admin.ModelAdmin):
    def formfield_for_manytomany(self, db_field, request, **kwargs):
        if db_field.name == "menu_objects":
            kwargs["queryset"] = MenuObject.objects.filter(parent=None)
        return super(MenuAdmin, self).formfield_for_manytomany(db_field, request, **kwargs)


admin.site.register(MenuObject)
admin.site.register(Menu, MenuAdmin)

