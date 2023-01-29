import string
import random
from datetime import date
import datetime


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


class Datas:
    def __init__(self, data_inicial=datetime.date.today(), quantidade_dias=15):
        self.data_inicial = data_inicial
        self.quantidade_dias = quantidade_dias

    def vencimento(self):
        data = self.data_inicial + datetime.timedelta(days=self.quantidade_dias)
        print(f"Data:{data}")
        return self.verificar_fim_de_semana(data)

    def verificar_fim_de_semana(self, data_vencimento):
        dia = data_vencimento.weekday()
        if dia == 5:
            return data_vencimento + datetime.timedelta(days=2)
        if dia == 6:
            return data_vencimento + datetime.timedelta(days=1)
        return data_vencimento
