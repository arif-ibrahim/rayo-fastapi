from typing import List
from fastapi import APIRouter, UploadFile, Request, File
from fastapi.responses import FileResponse
import os
import base64


router = APIRouter(prefix="/file", tags=["Files"])


@router.get("/images/{image_name}")
async def get_image(image_name: str):
    base_directory = os.path.dirname(os.path.abspath(__file__))
    images_directory = os.path.join(base_directory, "images")

    image_path = os.path.join(images_directory, image_name)
    if os.path.exists(image_path):
        return FileResponse(image_path)
    else:
        return {"error": "Image not found"}


@router.post("/dynamic")
def dynamic(request: Request, file: UploadFile = File()):
    data = file.file.read()
    print(type(data))

    base_directory = os.path.dirname(os.path.abspath(__file__))
    grandparent_directory = os.path.abspath(os.path.join(base_directory, ".."))
    images_directory = os.path.join(grandparent_directory, "files")
    image_path = os.path.join(images_directory, "saved_")

    with open(image_path + file.filename, "wb") as f:
        f.write(data)
    file.file.close()

    encoded_image = base64.b64encode(data).decode("utf-8")

    return encoded_image
