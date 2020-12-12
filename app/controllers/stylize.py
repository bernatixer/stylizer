import time

import torch
from libs import transformer, utils


class StylizeController:
    def __init__(self):
        self.device = "cuda" if torch.cuda.is_available() else "cpu"

    def stylize(self, filename: str, filename_result: str, style_path: str):
        net = transformer.TransformerNetwork()
        net.load_state_dict(torch.load(style_path))
        net = net.to(self.device)

        with torch.no_grad():
            torch.cuda.empty_cache()

            content_image = utils.load_image(filename)

            starttime = time.time()

            content_tensor = utils.itot(content_image).to(self.device)
            generated_tensor = net(content_tensor)
            generated_image = utils.ttoi(generated_tensor.detach())
            print("Elapsed time: {}".format(time.time() - starttime))
            utils.saveimg(generated_image, filename_result)
