from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse

from app.features.auth.dependencies import get_current_user, require_admin_role
from app.features.auth.models import User

router = APIRouter(prefix="/admin", tags=["admin"])


@router.get("/health")
def admin_health():
    return {"status": "ok", "service": "management-api"}


@router.get("/users")
def list_users(
    current_user: User = Depends(require_admin_role),
):
    """Stub: will be implemented in Phase 4."""
    return JSONResponse(status_code=501, content={"detail": "Not yet implemented"})


@router.get("/reports")
def list_reports(
    current_user: User = Depends(require_admin_role),
):
    """Stub: will be implemented in Phase 4."""
    return JSONResponse(status_code=501, content={"detail": "Not yet implemented"})


@router.get("/inspections")
def list_inspections(
    current_user: User = Depends(require_admin_role),
):
    """Stub: will be implemented in Phase 4."""
    return JSONResponse(status_code=501, content={"detail": "Not yet implemented"})


@router.get("/dashboard")
def dashboard_stats(
    current_user: User = Depends(require_admin_role),
):
    """Stub: will be implemented in Phase 4."""
    return JSONResponse(status_code=501, content={"detail": "Not yet implemented"})


@router.get("/institutions")
def list_institutions(
    current_user: User = Depends(require_admin_role),
):
    """Stub: will be implemented in Phase 4."""
    return JSONResponse(status_code=501, content={"detail": "Not yet implemented"})
