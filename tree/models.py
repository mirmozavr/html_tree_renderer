from django.db import models


class Tree(models.Model):
    menu_name = models.CharField(max_length=128, null=False, unique=True)
    structure = models.JSONField(null=False)

    def __repr__(self):
        return self.menu_name

    def __str__(self):
        return self.menu_name
