from uuid import uuid4

from controllers.stylize import StylizeController
from fastapi import BackgroundTasks, HTTPException, UploadFile
from fastapi.responses import FileResponse
from styles.styles import Styles


class TransferStyleHandler:
    controller: StylizeController = None

    def __init__(self, styles: Styles):
        self.controller = StylizeController()
        self.TEMP_FOLDER = "temp"
        self.STYLE_MAP = styles.get_styles_models()

    def handle(self, file: UploadFile, style: str, background_tasks: BackgroundTasks):
        style_path = self.get_style_model_path(style)
        if not style_path:
            raise HTTPException(status_code=400, detail="Invalid style provided")

        file_id = str(uuid4())
        filename = "{}/{}.jpg".format(self.TEMP_FOLDER, file_id)
        filename_result = "{}/result-{}.jpg".format(self.TEMP_FOLDER, file_id)

        self.controller.save_image(file, filename)
        self.controller.convert_image(filename)

        self.controller.stylize(filename, filename_result, style_path)
        background_tasks.add_task(self.controller.remove_file, filename)
        background_tasks.add_task(self.controller.remove_file, filename_result)
        return FileResponse(filename_result)

    def get_style_model_path(self, style: str):
        if style in self.STYLE_MAP:
            return self.STYLE_MAP[style]

        return None
