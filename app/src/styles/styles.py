from src.styles.bayanihan.bayanihan import Bayanihan
from src.styles.lazy.lazy import Lazy
from src.styles.mosaic.mosaic import Mosaic
from src.styles.ross.ross import Ross
from src.styles.starry.starry import Starry
from src.styles.testmodel.testmodel import Testmodel
from src.styles.trippy2.trippy2 import Trippy2
from src.styles.trippy.trippy import Trippy
from src.styles.wanderer.wanderer import Wanderer
from src.styles.wave.wave import Wave


class Styles:
    def __init__(self):
        self.STYLES = [
            Mosaic(),
            Wave(),
            Starry(),
            Lazy(),
            Bayanihan(),
            Testmodel(),
            Wanderer(),
            Ross(),
            Trippy(),
            Trippy2(),
        ]
        self.STYLES_MODELS = self.get_styles_models()
        self.STYLES_REPRESENTATIONS = self.get_styles_representations()

    def get_styles_representations(self):
        representations = [style.get_representation() for style in self.STYLES]
        return representations

    def get_styles_models(self):
        styles_map = {style.NAME: style.MODEL_PATH for style in self.STYLES}
        return styles_map


styles_class = Styles()
