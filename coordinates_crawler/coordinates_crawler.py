from bs4 import BeautifulSoup
import requests


class CoordinatesCrawler:
    __LOCATION_ARGS_KEY = "location"
    __URI = "https://www.geodatos.net/coordenadas/buscar?q={}"
    __TABLE_CLASS_IDS = "table table-responsive table-striped table-hover"

    def __init__(self, **kwargs):
        self.__location = kwargs.get(self.__LOCATION_ARGS_KEY)
        self.__formed_uri = self.__URI.format(self.__location)

    def crawl(self):
        code = requests.get(self.__formed_uri)
        plain = code.text
        s = BeautifulSoup(plain, "html.parser")

        table = s.find("table", {'class': self.__TABLE_CLASS_IDS})

        coordinates_info = ""
        for td in table.findAll("td"):
            line = td.text + "\n"
            coordinates_info += line

        decimal_data = coordinates_info.split("Grados decimales (GD)")

        coordinates: {} = dict()

        if decimal_data:
            decimal_info = decimal_data[0]
            decimal_info = decimal_info.split("Estándar decimal simple\n")

            if decimal_info:
                decimal_info = decimal_info[1]
                decimal_info = decimal_info.split("\n")

                if decimal_info:
                    coordinates = {
                        'x': float(decimal_info[0]),
                        'y': float(decimal_info[1])
                    }

        return coordinates
