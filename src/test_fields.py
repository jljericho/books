import unittest

from . import fields


class TitleFieldTests(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.valid_title = "Noise"
        cls.valid_subtitle = "A Flaw In Human Judgement"

    def test_create_title(self):
        title = fields.Title(title=self.valid_title)
        self.assertIsInstance(title, fields.Title)

    def test_title_cannot_by_none(self):
        with self.assertRaises(ValueError):
            fields.Title(title=None)

    def test_title_cannot_by_empty(self):
        with self.assertRaises(ValueError):
            fields.Title(title="")

    def test_create_title_with_subtitle(self):
        title = fields.Title(title=self.valid_title, subtitle=self.valid_subtitle)
        self.assertEqual(title.subtitle, self.valid_subtitle)

    def test_title_splits_subtitle(self):
        combined_title = self.valid_title + ": " + self.valid_subtitle
        title = fields.Title(title=combined_title)
        self.assertEqual(title.title, self.valid_title)
        self.assertEqual(title.subtitle, self.valid_subtitle)

    def test_title_to_dict(self):
        title = fields.Title(title=self.valid_title, subtitle=self.valid_subtitle)
        self.assertEqual(
            title.dict(),
            {"title": self.valid_title, "subtitle": self.valid_subtitle}
        )
