from fastapi import APIRouter

from app.features.admin.router import router as admin_router

api_router = APIRouter()

api_router.include_router(admin_router)


@api_router.get("/health")
def health():
    return {"message": "OK!"}
