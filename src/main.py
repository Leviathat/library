from fastapi import FastAPI

from controllers import books
from containers import containers

container = containers.Container()
container.init_wiring()

app = FastAPI()
app.include_router(books.router)
