from typing import List
from fastapi import APIRouter, UploadFile, Request, File
from fastapi.responses import FileResponse
import os
import base64
import uuid
import time


router = APIRouter(prefix="/file", tags=["Files"])


def get_file_path(file_name):
    base_directory = os.path.dirname(os.path.abspath(__file__))
    upload_dir = os.path.join(
        os.path.abspath(os.path.join(base_directory, "..")), "files"
    )

    file_path = os.path.join(upload_dir, file_name)

    return file_path


def generate_unique_filename(file_extension):
    timestamp = int(time.time() * 1000)
    unique_id = str(uuid.uuid4().hex)
    return f"{timestamp}_{unique_id}.{file_extension}"


@router.get("/images/{image_name}")
async def get_image(image_name: str):
    image_path = get_file_path(image_name)
    if os.path.exists(image_path):
        return FileResponse(image_path)
    else:
        return {"error": "Image not found"}


@router.post("/upload/")
async def upload_file(file: UploadFile):
    if file.filename:
        file_extension = file.filename.split(".")[-1]
        unique_filename = generate_unique_filename(file_extension)
        file_path = get_file_path(unique_filename)
        with open(file_path, "wb") as f:
            f.write(file.file.read())

        return {"message": "File uploaded successfully", "filename": unique_filename}

    return {"message": "File not uploaded"}
