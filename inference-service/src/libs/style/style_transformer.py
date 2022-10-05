import time

import torch
from src.libs.style.network import TransformerNetwork
from src.libs.style.utils import load_image, itot, ttoi, saveimg
from src.core.logger import LOG


class StyleTransformer:
    def __init__(self):
        self.device = "cuda" if torch.cuda.is_available() else "cpu"

    def apply(self, filename: str, filename_result: str, style_path: str):
        net = self.load_model(style_path)

        start_time = time.time()
        content_image = load_image(filename)
        content_tensor = itot(content_image).to(self.device)

        with torch.no_grad():
            torch.cuda.empty_cache()
            generated_tensor = net(content_tensor)
            generated_image = ttoi(generated_tensor.detach())

        formatted_process_time = "{0:.2f}".format((time.time() - start_time) * 1000)
        LOG.info("Process time: {}ms".format(formatted_process_time))
        saveimg(generated_image, filename_result)

    def load_model(self, style_path):
        # Pre-init models in memory?
        net = TransformerNetwork()
        net.load_state_dict(torch.load(style_path))
        net = net.to(self.device)

        return net

style_transformer = StyleTransformer()
