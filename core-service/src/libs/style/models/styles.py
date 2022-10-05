from src.libs.style.models.bayanihan.bayanihan import Bayanihan
from src.libs.style.models.lazy.lazy import Lazy
from src.libs.style.models.mosaic.mosaic import Mosaic
from src.libs.style.models.ross.ross import Ross
from src.libs.style.models.starry.starry import Starry
from src.libs.style.models.testmodel.testmodel import Testmodel
from src.libs.style.models.trippy2.trippy2 import Trippy2
from src.libs.style.models.trippy.trippy import Trippy
from src.libs.style.models.wanderer.wanderer import Wanderer
from src.libs.style.models.wave.wave import Wave


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
