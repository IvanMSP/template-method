# OS
from __future__ import annotations
from abc import ABC, abstractmethod


class AbstractClass(ABC):
    """
    Clase abstracta para definir nuestro template method para hacer scrapping
    de sitios webs.
    """

    def template_method(self) -> None:
        """
        Estos son los pasos necesarios para scrappear un sitio web.
        """
        self.make_request()
        self.get_content()
        self.get_data_from_classes()
        self.save_to_db()

    # Métodos implementados en la clase abstracta
    # Se aplican para todos los sitios web
    def save_to_db(self):
        """
        Método para guardar la informacion en la base de datos.
        """
        print(f"Guardando la informacion de: {self.url}")

    # Métodos abstractos que deben ser implementados en las subclases
    @abstractmethod
    def make_request(self) -> None:
        """
        Método que realiza la petición a la url del sitio web.
        args: url
        response: response from request to url
        """
        pass

    @abstractmethod
    def get_content(self) -> None:
        """
        Método que obtiene el contenido de la url del sitio web.
        args: response
        response: content from response of url
        """
        pass

    @abstractmethod
    def get_data_from_classes(self) -> None:
        """
        Método que obtiene la información solicitada.
        response: data
        """
        pass
