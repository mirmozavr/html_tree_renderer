from django.shortcuts import render

from tree.models import Tree


def home_page(request):
    query = Tree.objects.order_by("menu_name").all().values("menu_name")
    menu_list = (item["menu_name"] for item in query)
    context = {"menu_list": menu_list}
    return render(request, "tree/home.html", context)


def tree_page(request, path):
    path = path.split("/")
    context = {
        "menu_name": path[0],
        "path": path[1:],
    }
    return render(request, "tree/tree.html", context)
