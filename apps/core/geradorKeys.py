import string
import random
from datetime import date


class GeradorKeys:
    def __init__(self):
        self.escolhas_possiveis = string.ascii_letters + string.digits
        self.data = date.today()

    def __key_ano_gerador(self):
        resultado = f"{self.data.strftime('%Y-%m')}-"
        for _ in range(5):
            resultado += random.choice(self.escolhas_possiveis)
        return resultado

    def key(self):
        return self.__key_ano_gerador()

    def key_proposta(self, proposta_id):
        codigo = f"#{date.today()}-{proposta_id}"
        return codigo
    