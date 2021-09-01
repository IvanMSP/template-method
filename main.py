# Pattern
from pattern.client import client_code

# Owner
from websites.web_site_one import WebSiteOne
from websites.web_site_two import WebSiteTwo


if __name__ == "__main__":
    url = input("Ingresa la url: ")
    classes = input("Ingresa las clases a buscar en el sitio(separados por coma): ")
    list_classes = classes.split(", ")
    client_code(WebSiteOne(url, list_classes))
    print("###################\n")
    client_code(WebSiteTwo(url, list_classes))