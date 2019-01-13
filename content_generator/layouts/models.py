from django.db import models


class Section(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return 'section {id}: {name}'.format(id=self.id, name=self.name)

    def get_random_content(self):
        return self.content_set.order_by('?').first()


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

    def get_prioritized_sections(self):
        layout_sections = self.layoutsection_set.order_by('priority')
        return [layout_section.section for layout_section in layout_sections]

    def generate_text(self):
        sections = self.get_prioritized_sections()
        text = '\n'.join(
            [section.get_random_content().content for section in sections]
        )
        return text


class LayoutSection(models.Model):
    layout = models.ForeignKey(Layout, on_delete=models.CASCADE)
    section = models.ForeignKey(Section, on_delete=models.CASCADE)
    priority = models.PositiveIntegerField()

    class Meta:
        unique_together = ('layout', 'priority')
