import os
import shutil
from uuid import uuid4
from src.core.logger import LOG

from fastapi import BackgroundTasks, HTTPException, UploadFile
from fastapi.responses import FileResponse
from src.repositories.transformation import transformations_repository
from src.schemas.transformation import Transformation
from src.libs.style.models.styles import styles_class
from src.api.clients.inference_client import InferenceClient
from PIL import Image

import requests

class TransferStyleHandler:

    def __init__(self):
        self.INFERENCE_CLIENT = InferenceClient()
        self.TEMP_FOLDER = "temp"

    def handle(
        self, file: UploadFile, style: str, background_tasks: BackgroundTasks, db, current_user
    ):
        style_path = self.get_style_model_path(style)
        if not style_path:
            raise HTTPException(status_code=400, detail="Invalid style provided")

        file_id = str(uuid4())
        filename = "{}/{}.jpg".format(self.TEMP_FOLDER, file_id)
        filename_result = "{}/result-{}.jpg".format(self.TEMP_FOLDER, file_id)

        self.save_image(file, filename)
        self.convert_image(filename)
        response = self.INFERENCE_CLIENT.stylize(filename)

        with open(filename_result, 'wb') as f:
            f.write(response)

        # background_tasks.add_task(self.remove_file, filename)
        # background_tasks.add_task(self.remove_file, filename_result)

        transformation = Transformation(style=style, user=current_user.id)
        transformations_repository.create(db=db, obj_in=transformation)

        return FileResponse(filename_result)

    def get_style_model_path(self, style: str):
        if style in styles_class.STYLES_MODELS:
            return styles_class.STYLES_MODELS[style]

        return None

    def save_image(self, file, filename):
        with open(filename, "wb") as f_destination:
            shutil.copyfileobj(file.file, f_destination)

    def convert_image(self, filename):
        img = Image.open(filename)
        rgb_img = img.convert("RGB")
        rgb_img.save(filename)

    def remove_file(self, path):
        os.remove(path)


transfer_style_handler = TransferStyleHandler()
