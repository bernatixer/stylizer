from fastapi import UploadFile, HTTPException
from fastapi.responses import FileResponse
from styles.styles import Styles
from controllers.stylize import StylizeController
from uuid import uuid4
import shutil


class StylesHandler():

    def __init__(self, styles: Styles):
        self.styles = styles


    def handle(self):
        return { "styles": self.styles.STYLES_REPRESENTATIONS }
