import unittest

import mock

from layouts import factories
from layouts import models


class LayoutTests(unittest.TestCase):
    def setUp(self):
        self.layout = factories.LayoutFactory()

        self.section_1 = factories.SectionFactory(name='section_1')
        self.section_2 = factories.SectionFactory(name='section_2')
        self.section_3 = factories.SectionFactory(name='section_3')

        factories.LayoutSectionFactory(
            layout=self.layout,
            section=self.section_1,
            priority=10,
        )
        factories.LayoutSectionFactory(
            layout=self.layout,
            section=self.section_2,
            priority=0,
        )
        factories.LayoutSectionFactory(
            layout=self.layout,
            section=self.section_3,
            priority=4,
        )

        self.content_1 = factories.ContentFactory(content='foo')
        self.content_2 = factories.ContentFactory(content='bar')
        self.content_3 = factories.ContentFactory(content='spam')

    def test_get_prioritized_sections(self):
        self.assertEqual(
            self.layout.get_prioritized_sections(),
            [self.section_2, self.section_3, self.section_1],
        )

    @mock.patch('layouts.models.Section.get_random_content')
    def test_generate_text(self, generate_random_content_mock):
        generate_random_content_mock.side_effect = [
            self.content_2, self.content_3, self.content_1
        ]

        self.assertEqual(
            self.layout.generate_text(),
            'bar\nspam\nfoo',
        )


class RandomContentTests(unittest.TestCase):
    def setUp(self):
        self.section = factories.SectionFactory()

        self.content_1 = factories.ContentFactory(
            section=self.section,
            name='fake_content_1',
            content='foo',
        )
        self.content_2 = factories.ContentFactory(
            section=self.section,
            name='fake_content_2',
            content='bar',
        )
        self.content_3 = factories.ContentFactory(
            section=self.section,
            name='fake_content_3',
            content='spam',
        )

    def test_get_random_content(self):
        self.assertEqual(self.section.content_set.count(), 3)

        content_set = set()
        for i in range(100):
            content_set.add(self.section.get_random_content())

        self.assertGreater(len(content_set), 1)

        self.assertTrue(isinstance(content_set.pop(), models.Content))
