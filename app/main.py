from fastapi import BackgroundTasks, FastAPI, File, Form, UploadFile
from fastapi.staticfiles import StaticFiles
from handlers.root import RootHandler
from handlers.styles import StylesHandler
from handlers.stylize import StylizeHandler
from styles.styles import Styles

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")

styles = Styles()
root_handler = RootHandler()
styles_handler = StylesHandler(styles)
stylize_handler = StylizeHandler(styles)


@app.get("/")
async def root():
    return root_handler.handle()


@app.get("/api/styles")
async def get_styles():
    return styles_handler.handle()


@app.post("/api/stylize/")
async def stylize_image(
    background_tasks: BackgroundTasks,
    file: UploadFile = File(...),
    style: str = Form(...),
):
    return stylize_handler.handle(file, style, background_tasks)
