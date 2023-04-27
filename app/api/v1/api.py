from fastapi import APIRouter

from app.api.v1.endpoints.site import router as site_router

api_router = APIRouter()
api_router.include_router(site_router)
