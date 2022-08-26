from dataclasses import dataclass

from fields import Title, Authors


@dataclass
class Book:
    title: Title
    authors: Authors
