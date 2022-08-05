from styles.bayanihan.bayanihan import Bayanihan
from styles.lazy.lazy import Lazy
from styles.mosaic.mosaic import Mosaic
from styles.ross.ross import Ross
from styles.starry.starry import Starry
from styles.testmodel.testmodel import Testmodel
from styles.trippy2.trippy2 import Trippy2
from styles.trippy.trippy import Trippy
from styles.wanderer.wanderer import Wanderer
from styles.wave.wave import Wave


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
