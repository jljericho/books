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


class Contributor(BaseModel):
    name: str
    role: str = "author"

    @validator("name")
    def check_name(cls, name):
        if name is None or name == "":
            raise ValueError('name cannot be NULL or empty')
        if ", " not in name:
            raise ValueError(f'name must be last, first. Not {name}')
        return name.strip()


class Authors(BaseModel):
    authors: list[Contributor]

    ###
    # Validators
    ###

    @validator("authors", pre=True, each_item=True)
    def parse_authors(cls, v):
        if isinstance(v, str):
            v = {"name": v}
        if isinstance(v, tuple):
            v = dict(zip(Contributor.__fields__, v))
        return v

    ###
    # Accessors
    ###

    def __getitem__(self, item):
        return self.authors[item]

    def __len__(self):
        return len(self.authors)
