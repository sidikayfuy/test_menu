from django.shortcuts import render
from .models import MenuObject, Menu


def index(request):
    menus = Menu.objects.all()
    return render(request, 'menu/index.html', {'menus': menus})


def check_parents(menu, parents):
    if menu.parent != None:
        parents.append(menu.parent)
        check_parents(menu.parent, parents)
    else:
        return


def menu_page(request, slug):
    menu_object = MenuObject.objects.get(slug=slug)
    need_menu = ''
    parents = []
    check_parents(menu_object, parents)
    if len(parents) == 0:
        menu_filter = menu_object
    else:
        menu_filter = parents[-1]

    for i in Menu.objects.all():
        if menu_filter in i.menu_objects.all():
            need_menu = i
    return render(request, 'menu/menu.html', {'need_menu': need_menu, 'submenu': menu_object})
