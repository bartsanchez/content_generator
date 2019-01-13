import factory

from layouts import models


class SectionFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.Section

    name = 'fake_section'


class ContentFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.Content

    name = 'fake_section'
    content = 'fake_content'
    section = factory.SubFactory(SectionFactory)


class LayoutFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.Layout

    name = 'fake_layout'


class LayoutSectionFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.LayoutSection

    layout = factory.SubFactory(LayoutFactory)
    section = factory.SubFactory(SectionFactory)
    priority = factory.Sequence(lambda n: n)
