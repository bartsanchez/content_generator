from django.db import models


class Layout(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return 'layout {id}: {name}'.format(id=self.id, name=self.name)
