# Pattern
from pattern.base import AbstractClass


def client_code(abstract_class: AbstractClass) -> None:
    """
    Cliente encargado de ejecutar nuestro template_method.
    """
    abstract_class.template_method()
