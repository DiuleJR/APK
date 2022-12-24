# importar o app, Builder (GUI)
# criar o nosso aplicativo
# criar a função build do aplicativo

from kivymd.app import MDApp
from kivy.lang import Builder
import requests


class DolarJunin(MDApp):
    def build(self):
        return Builder.load_file("main.kv")

    def on_start(self):
        self.root.text = f" Dólar \nR${self.pegar_cotacao('USD'):.2f}"

    def pegar_cotacao(self, moeda):
        link = f"https://economia.awesomeapi.com.br/last/{moeda}-BRL"
        response = requests.get(link)
        dic_response = response.json()
        cotacao = dic_response[f'{moeda}BRL']['bid']
        return float(cotacao)


DolarJunin().run()
