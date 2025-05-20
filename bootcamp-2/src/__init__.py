from fastapi import FastAPI
from src.books.routes import book_router
from contextlib import asynccontextmanager
from src.db.main import init_db

@asynccontextmanager
async def lifespan(app: FastAPI):
    print("server is started")
    await init_db()
    yield
    print("server is stopped")

version = "v1"

app = FastAPI(
    title = "xyra-test",
    description="book app description",
    version=version,
    lifespan=lifespan
)

app.include_router(book_router, prefix="/api/{version}/books", tags=["books"])


@app.get("/", tags=["root"])
async def root():        
    return {"message": "Hello World"}