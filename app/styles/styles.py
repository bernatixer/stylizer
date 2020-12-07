from styles.mosaic.mosaic import Mosaic
from styles.wave.wave import Wave
from styles.starry.starry import Starry
from styles.lazy.lazy import Lazy
from styles.bayanihan.bayanihan import Bayanihan

class Styles:

    def __init__(self):
        self.STYLES = [
            Mosaic(),
            Wave(),
            Starry(),
            Lazy(),
            Bayanihan()
        ]
        self.STYLES_MODELS = self.get_styles_models()
        self.STYLES_REPRESENTATIONS = self.get_styles_representations()


    def get_styles_representations(self):
        representations = [style.get_representation() for style in self.STYLES]
        return representations


    def get_styles_models(self):
        styles_map = {style.NAME: style.MODEL_PATH for style in self.STYLES}
        return styles_map
