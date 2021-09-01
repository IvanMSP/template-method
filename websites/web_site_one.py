# Pattern
from pattern.base import AbstractClass


class WebSiteOne(AbstractClass):
    def __init__(self, url, classes):
        self.url = url
        self.classes = classes
        self.content = None
        self.response = None
        self.data = None

    def make_request(self) -> None:
        print(f"Realizando request a la url: {self.url} con BeatifulSoup")

    def get_content(self) -> None:
        print(f"Obteniendo el contenido de la url en la clase WebSiteOne")

    def get_data_from_classes(self) -> None:
        print(f"Extraer data desde la clase WebSiteOne")
