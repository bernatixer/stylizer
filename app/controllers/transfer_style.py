import os
import shutil
import time

import torch
from libs import transformer, utils
from PIL import Image

logger = logging.getLogger(__name__)

class TransferStyleController:
    def __init__(self):
        self.device = "cuda" if torch.cuda.is_available() else "cpu"

    def transfer_style(self, filename: str, filename_result: str, style_path: str):
        net = self.load_model(style_path)

        start_time = time.time()
        content_image = utils.load_image(filename)
        content_tensor = utils.itot(content_image).to(self.device)

        with torch.no_grad():
            torch.cuda.empty_cache()
            generated_tensor = net(content_tensor)
            generated_image = utils.ttoi(generated_tensor.detach())

        formatted_process_time = '{0:.2f}'.format((time.time() - start_time)*1000)
        logger.info("Process time: {}ms".format(formatted_process_time))
        utils.saveimg(generated_image, filename_result)

    def load_model(self, style_path):
        # Pre-init models in memory?
        net = transformer.TransformerNetwork()
        net.load_state_dict(torch.load(style_path))
        net = net.to(self.device)

        return net

    def save_image(self, file, filename):
        with open(filename, "wb") as f_destination:
            shutil.copyfileobj(file.file, f_destination)

    def convert_image(self, filename):
        img = Image.open(filename)
        rgb_img = img.convert("RGB")
        rgb_img.save(filename)

    def remove_file(self, path):
        os.remove(path)
