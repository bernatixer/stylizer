import os
import shutil
from uuid import uuid4

from fastapi import BackgroundTasks, HTTPException, UploadFile
from fastapi.responses import FileResponse
from src.libs.style.models.styles import styles_class
from src.libs.style.style_transformer import style_transformer
from PIL import Image


class TransferStyleHandler:

    def __init__(self):
        self.TEMP_FOLDER = "temp"

    def handle(
        self, file: UploadFile, style: str, background_tasks: BackgroundTasks
    ):
        style_path = self.get_style_model_path(style)
        if not style_path:
            raise HTTPException(status_code=400, detail="Invalid style provided")

        file_id = str(uuid4())
        filename = "{}/{}.jpg".format(self.TEMP_FOLDER, file_id)
        filename_result = "{}/result-{}.jpg".format(self.TEMP_FOLDER, file_id)

        self.save_image(file, filename)
        self.convert_image(filename)

        style_transformer.apply(filename, filename_result, style_path)
        background_tasks.add_task(self.remove_file, filename)
        background_tasks.add_task(self.remove_file, filename_result)

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