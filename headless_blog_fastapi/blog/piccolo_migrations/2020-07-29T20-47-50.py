from piccolo.apps.migrations.auto import MigrationManager
from piccolo.columns.defaults.timestamp import TimestampNow


ID = "2020-07-29T20:47:50"
VERSION = "0.12.2"


async def forwards():
    manager = MigrationManager(migration_id=ID, app_name="blog")

    manager.add_table("Post", tablename="post")

    manager.add_column(
        table_class_name="Post",
        tablename="post",
        column_name="title",
        column_class_name="Varchar",
        params={
            "length": 255,
            "default": "",
            "null": False,
            "primary": False,
            "key": False,
            "unique": False,
            "index": False,
        },
    )

    manager.add_column(
        table_class_name="Post",
        tablename="post",
        column_name="content",
        column_class_name="Text",
        params={
            "default": "",
            "null": False,
            "primary": False,
            "key": False,
            "unique": False,
            "index": False,
        },
    )

    manager.add_column(
        table_class_name="Post",
        tablename="post",
        column_name="published",
        column_class_name="Boolean",
        params={
            "default": False,
            "null": False,
            "primary": False,
            "key": False,
            "unique": False,
            "index": False,
        },
    )

    manager.add_column(
        table_class_name="Post",
        tablename="post",
        column_name="created_on",
        column_class_name="Timestamp",
        params={
            "default": TimestampNow(),
            "null": False,
            "primary": False,
            "key": False,
            "unique": False,
            "index": False,
        },
    )

    return manager
