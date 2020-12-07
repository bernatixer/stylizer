class StyleBase:

    def get_representation(self):
        return {
            "name": self.NAME,
            "display_name": self.DISPLAY_NAME,
            "display_image": self.DISPLAY_IMAGE
        }
