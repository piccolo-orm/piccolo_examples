from piccolo_admin.endpoints import create_admin
from piccolo_api.crud.endpoints import PiccoloCRUD
from piccolo_api.fastapi.endpoints import FastAPIWrapper
from piccolo.engine import engine_finder
from starlette.routing import Mount
from fastapi import FastAPI

from blog.tables import Post
from blog.piccolo_app import APP_CONFIG


app = FastAPI(
    routes=[
        Mount("/admin/", create_admin(tables=APP_CONFIG.table_classes)),
    ],
)


FastAPIWrapper(
    root_url="/posts/",
    fastapi_app=app,
    piccolo_crud=PiccoloCRUD(
        table=Post,
        read_only=True,
    ),
)


@app.on_event("startup")
async def open_database_connection_pool():
    engine = engine_finder()
    await engine.start_connnection_pool()


@app.on_event("shutdown")
async def close_database_connection_pool():
    engine = engine_finder()
    await engine.close_connnection_pool()
