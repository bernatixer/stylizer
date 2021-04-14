from fastapi import BackgroundTasks, FastAPI, File, Form, UploadFile
from fastapi.staticfiles import StaticFiles
from handlers.index import IndexHandler
from handlers.styles_list import StylesListHandler
from handlers.transfer_style import TransferStyleHandler
from styles.styles import Styles

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")

styles = Styles()
index_handler = IndexHandler()
styles_list_handler = StylesListHandler(styles)
transfer_style_handler = TransferStyleHandler(styles)


@app.get("/")
async def index():
    return index_handler.handle()


@app.get("/api/styles/")
async def get_styles():
    return styles_list_handler.handle()


@app.post("/api/stylize/")
async def stylize_image(
    background_tasks: BackgroundTasks,
    file: UploadFile = File(...),
    style: str = Form(...),
):
    return transfer_style_handler.handle(file, style, background_tasks)
