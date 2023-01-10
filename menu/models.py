from django.db import models
from pytils.translit import slugify


class MenuObject(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(blank=True, null=True)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(MenuObject, self).save(*args, **kwargs)

    def children(self):
        return MenuObject.objects.filter(parent=self)

    def menu(self):
        menu_object = self
        need_menu = ''
        if menu_object.parent != None:
            menu_filter = menu_object.parent
        else:
            menu_filter = menu_object
        for i in Menu.objects.all():
            if menu_filter in i.menu_objects.all():
                need_menu = i
        return need_menu


class Menu(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(blank=True, null=True)
    menu_objects = models.ManyToManyField(MenuObject)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super(Menu, self).save(*args, **kwargs)


