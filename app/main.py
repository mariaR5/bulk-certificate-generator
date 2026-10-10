from contextlib import asynccontextmanager
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.core.config import settings
from app.api.v1.router import api_router
from app.db.session import init_db
import app.models  # noqa: F401 - ensures models are registered with Base metadata


@asynccontextmanager
async def lifespan(app: FastAPI):
    settings.init_storage()
    init_db()
    yield


app = FastAPI(
    title=settings.PROJECT_NAME,
    description="Backend service for bulk certificate generation",
    version="0.1.0",
    lifespan=lifespan,
)


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(api_router, prefix=settings.API_V1_STR)


@app.get("/", summary="Root Index")
async def root():
    return {
        "message": "Bulk Certificate Generator API",
        "docs_url": "/docs",
        "health_check": f"{settings.API_V1_STR}/health",
    }
