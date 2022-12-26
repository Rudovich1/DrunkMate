from fastapi import APIRouter, UploadFile, File, HTTPException
from fastapi.responses import FileResponse
from uuid import uuid4
import os

from starlette import status

from drunkMate.project_path_getter import get_project_root

router = APIRouter()


@router.post("/image_api/post_image")
async def post_image(guid: str, file: UploadFile = File(...)):
    file_format = ""
    correct_formats = ['png', 'jpg', 'jpeg']
    try:
        file_format = file.filename.split('.')[-1]
        if file_format not in correct_formats:
            raise Exception
    except:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Invalid file format",
            headers={"WWW-Authenticate": "Bearer"},
        )
    with open(f"{str(get_project_root())}/images/{guid}.{file_format}", 'wb+') as image_file_upload:
        image_file_upload.write(file.file.read())


@router.get("/image_api/get_image/{guid=test}")
async def get_image(guid: str = 'test'):
    prefixed = [filename for filename in os.listdir(f"{get_project_root()}/images/") if filename.startswith(guid)]
    if len(prefixed) > 0:
        return FileResponse(f"{str(get_project_root())}/images/{prefixed[0]}")
    else:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Image not found",
            headers={"WWW-Authenticate": "Bearer"},
        )

