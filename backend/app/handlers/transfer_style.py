from uuid import uuid4

from controllers.transfer_style import TransferStyleController
from fastapi import BackgroundTasks, HTTPException, UploadFile
from fastapi.responses import FileResponse
from styles.styles import styles_class


class TransferStyleHandler:
    controller: TransferStyleController = None

    def __init__(self):
        self.controller = TransferStyleController()
        self.TEMP_FOLDER = "temp"

    def handle(self, file: UploadFile, style: str, background_tasks: BackgroundTasks):
        style_path = self.get_style_model_path(style)
        if not style_path:
            raise HTTPException(status_code=400, detail="Invalid style provided")

        file_id = str(uuid4())
        filename = "{}/{}.jpg".format(self.TEMP_FOLDER, file_id)
        filename_result = "{}/result-{}.jpg".format(self.TEMP_FOLDER, file_id)

        self.controller.save_image(file, filename)
        self.controller.convert_image(filename)

        self.controller.transfer_style(filename, filename_result, style_path)
        background_tasks.add_task(self.controller.remove_file, filename)
        background_tasks.add_task(self.controller.remove_file, filename_result)
        return FileResponse(filename_result)

    def get_style_model_path(self, style: str):
        if style in styles_class.STYLES_MODELS:
            return styles_class.STYLES_MODELS[style]

        return None

transfer_style_handler = TransferStyleHandler()
