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


class AuthorsFieldTests(unittest.TestCase):

    def setUp(self) -> None:
        self.a_1 = "Kahneman, Daniel"
        self.a_2 = "Sibony, Oliver"

    def test_create_authors(self):
        a = fields.Authors(authors=[self.a_1])
        self.assertIsInstance(a, fields.Authors)
        self.assertIsInstance(a[0], fields.Contributor)
        self.assertEqual(a[0].name, self.a_1)

    def test_create_multiple_authors(self):
        a = fields.Authors(authors=[self.a_1, self.a_2])
        self.assertEqual(len(a), 2)

    def test_create_authors_defaults_to_author(self):
        a = fields.Authors(authors=[self.a_1])
        self.assertEqual(a[0].role, "author")

    def test_authors_requires_name(self):
        with self.assertRaises(ValueError):
            fields.Authors(authors=None)
        with self.assertRaises(ValueError):
            fields.Authors(authors=[None])
        with self.assertRaises(ValueError):
            fields.Authors(authors=[""])
