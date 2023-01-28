from django import template
from ..models import Tree
from django.utils.safestring import mark_safe
from django.shortcuts import reverse

register = template.Library()


@register.simple_tag(takes_context=True)
def draw_menu(context, menu_name: str):
    """
    Returns the menu as html
    :param context: Context
    :param menu_name: Menu name
    :return: Safe html
    """
    tree = Tree.objects.get(menu_name=menu_name).structure
    path = context["path"]
    menu_name = context["menu_name"]
    return mark_safe(traverse(menu_name, tree, path, 0))


def traverse(menu_name: str, tree: dict, path: list, index: int = 0) -> str:
    """
    Function to recursively traverse through tree structure and collect all items
    under unordered list tags
    :param menu_name: Menu name
    :param tree: Dictionary representation of a tree
    :param path: Url path
    :param index: Index of an element in path
    :return: Html representation of a tree
    """
    if not isinstance(tree, dict):
        return ""
    if index >= len(path) or not path:
        return ("<ul>"
                + "".join(
                    [
                        f"<li><a href='{get_tree_url('/'.join([menu_name] + path[:index] + [item]))}'>{item}</a></li>"
                        for item
                        in tree.keys()])
                + "</ul>")

    return ("<ul>"
            + "".join(
                [
                    f"<li><a href='{get_tree_url('/'.join([menu_name] + path[:index] + [item]))}'>{item}</a></li>"
                    for item
                    in tree.keys() if item != path[index]])
            + f"<li><a href='{get_tree_url('/'.join([menu_name] + path[:index + 1]))}'>{path[index]}</a></li>"
            + traverse(menu_name, tree[path[index]], path, index + 1)
            + "</ul>")


def get_tree_url(path: str) -> str:
    """
    Generate URL for the path
    :param path:
    :return: URL string
    """
    return reverse("tree_url", args=[path])
