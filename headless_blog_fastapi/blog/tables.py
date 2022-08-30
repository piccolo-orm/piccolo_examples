from piccolo.table import Table
from piccolo.columns import Varchar, Boolean, Timestamptz, Text


class Post(Table):
    """
    A simple blog post.
    """

    title = Varchar()
    content = Text()
    published = Boolean(default=False)
    created_on = Timestamptz()
