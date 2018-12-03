from django.db import models


class Layout(models.Model):
    name = models.CharField(max_length=255)
