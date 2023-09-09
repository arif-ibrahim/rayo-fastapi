from typing import List
from fastapi import APIRouter, UploadFile, Request, File
from fastapi.responses import FileResponse
from fastapi.templating import Jinja2Templates
import os
import base64


router = APIRouter(prefix="/file", tags=["Files"])

templates = Jinja2Templates(directory="templates")


@router.post("/uploadfile/")
async def create_upload_file(file: UploadFile):
    print(type(file.file.read()))
    return {"filename": file}


@router.get("/images/{image_name}")
async def get_image(image_name: str):
    # Get the absolute path to the 'images' directory
    base_directory = os.path.dirname(os.path.abspath(__file__))
    images_directory = os.path.join(base_directory, "images")

    # Construct the image path
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
    images_directory = os.path.join(base_directory, "images")
    image_path = os.path.join(images_directory, "saved_")

    # Image will be saved in the uploads folder prefixed with uploaded_
    with open(image_path + file.filename, "wb") as f:
        f.write(data)
    file.file.close()

    # encoding and decoding the image bytes
    encoded_image = base64.b64encode(data).decode("utf-8")

    return encoded_image
