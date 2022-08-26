from exceptions import FieldError


class Title:

    def __init__(self, title: str, subtitle: str = None):
        self.title = title
        self.subtitle = subtitle

    def validate(self):
        if self.title is None or self.title == "":
            raise FieldError("Title should not be NULL or empty.")


class Authors:

    def __init__(self, authors, roles):
        self.authors = authors
        self.roles = roles


