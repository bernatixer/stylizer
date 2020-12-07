from fastapi import FastAPI, File, UploadFile, Form
from fastapi.staticfiles import StaticFiles

from handlers.root import RootHandler
from handlers.stylize import StylizeHandler
from handlers.styles import StylesHandler
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
async def root():
    return styles_handler.handle()


@app.post("/api/stylize/")
async def stylize_image(file: UploadFile = File(...), style: str = Form(...)):
    return stylize_handler.handle(file, style)
