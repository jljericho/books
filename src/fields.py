from pydantic import BaseModel, validator

from .exceptions import FieldError


class Title(BaseModel):
    title: str
    subtitle: str = None

    _title_sep = ": "

    @validator("title")
    def check_title(cls, title):
        if title is None or title == "":
            raise ValueError('title cannot be NULL or empty')
        return title.strip().title()

    @validator("subtitle", always=True)
    def split_titles(cls, subtitle, values):
        if "title" in values and subtitle is None and cls._title_sep in values["title"]:
            values["title"], subtitle = values["title"].split(cls._title_sep)
        return subtitle


class Authors:

    def __init__(self, authors, roles):
        self.authors = authors
        self.roles = roles


