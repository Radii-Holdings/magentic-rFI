from fastapi import APIRouter, Request, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from fastapi.responses import JSONResponse

from .db import verify_user

router = APIRouter()

@router.post("/login")
async def login(request: Request, form_data: OAuth2PasswordRequestForm = Depends()):
    if verify_user(form_data.username, form_data.password):
        request.session['user'] = form_data.username
        return JSONResponse({"status": True})
    raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials")

@router.post("/logout")
async def logout(request: Request):
    request.session.pop('user', None)
    return JSONResponse({"status": True})
