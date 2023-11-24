from fastapi import FastAPI

from ex1 import router as ex1_routes
from ex2 import router as ex2_routes
from ex3 import router as ex3_routes
from ex4 import router as ex4_routes

app = FastAPI()

app.include_router(ex1_routes)
app.include_router(ex2_routes)
app.include_router(ex3_routes)
app.include_router(ex4_routes)
