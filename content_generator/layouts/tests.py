import unittest

from layouts import factories


class LayoutPriorityTests(unittest.TestCase):
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

    def test_get_prioritized_sections(self):
        self.assertEqual(
            self.layout.get_prioritized_sections(),
            [self.section_2, self.section_3, self.section_1],
        )
