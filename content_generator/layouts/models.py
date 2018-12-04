from django.db import models


class Section(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return 'section {id}: {name}'.format(id=self.id, name=self.name)


class Content(models.Model):
    name = models.CharField(max_length=255)
    content = models.TextField()
    section = models.ForeignKey(Section, on_delete=models.SET_NULL,
                                null=True, blank=True)

    def __str__(self):
        return 'content {id}: {name}'.format(id=self.id, name=self.name)


class Layout(models.Model):
    name = models.CharField(max_length=255)
    sections = models.ManyToManyField(Section, through='LayoutSection')

    def __str__(self):
        return 'layout {id}: {name}'.format(id=self.id, name=self.name)


class LayoutSection(models.Model):
    layout = models.ForeignKey(Layout, on_delete=models.CASCADE)
    section = models.ForeignKey(Section, on_delete=models.CASCADE)
    priority = models.PositiveIntegerField()

    class Meta:
        unique_together = ('layout', 'priority')
