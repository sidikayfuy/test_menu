from django import template
from menu.models import MenuObject, Menu
from django.utils.html import escape, mark_safe

register = template.Library()


def check_parents(menu, parents):
    if menu.parent != None:
        parents.append(menu.parent)
        check_parents(menu.parent, parents)
    else:
        return


@register.simple_tag
def draw_menu(menus, submenu):
    full_menu = Menu.objects.get(name=menus)
    content = []
    parents = []
    if submenu == '':
        for menu in full_menu.menu_objects.all():
            content.append(f"<li><a href={menu.slug}>{menu.title}</a></li>")
            if menu.children().count() > 0:
                content.append("<ul>")
                for i in menu.children():
                    content.append(f"<li><a href={i.slug}>{i.title}</a></li>")
                content.append("</ul>")
    else:
        if submenu.parent == None:
            without_parent = submenu.menu().menu_objects.all()
            for i in without_parent:
                if i == submenu:
                    content.append(f"<li><a>{i.title}</a></li>")
                else:
                    content.append(f"<li><a href={i.slug}>{i.title}</a></li>")
                if i.children().count() > 0:
                    content.append("<ul>")
                    for l in i.children():
                        content.append(f"<li><a href={l.slug}>{l.title}</a></li>")
                    content.append("</ul>")
        else:
            check_parents(submenu.parent, parents)
            parents.reverse()
            for i in parents:
                content.append(f"<ul><li><a href={i.slug}>{i.title}</a></li>")
            content.append("<ul>")
            content.append(f"<li><a href={submenu.parent.slug}>{submenu.parent.title}</a></li>")
            content.append(f"<ul><li><a>{submenu.title}</a></li>")
            if submenu.children().count() > 0:
                content.append("<ul>")
                for i in submenu.children():
                    content.append(f"<li><a href={i.slug}>{i.title}</a></li>")
                content.append("</ul>")
            content.append("</ul>")
            content.append("</ul>")
            for i in parents:
                content.append("</ul>")
    content = "".join(content)
    return mark_safe(content)
