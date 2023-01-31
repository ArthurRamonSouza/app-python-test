# importar o App, Builder (GUI)
# # criar todo o aplicativo
# # criar a funcao de build

# inicializando o projeto
from kivy.app import App
from kivy.lang import Builder
import requests

# se estiver em pastas, colocar o path/nome do arquivo
GUI = Builder.load_file('screen.kv')

class MyApp(App):

    def build(self):
        return GUI

    def getQuotations(self, coin):
        coinToDolar = requests.get(f'http://economia.awesomeapi.com.br/json/last/{coin}-USD').json()[f'{coin}USD']['bid']
        coinToReal = requests.get(f'http://economia.awesomeapi.com.br/json/last/{coin}-BRL').json()[f'{coin}BRL']['bid']
        return coinToDolar, coinToReal

    def on_start(self):
        ids = self.root.ids

        values = self.getQuotations('BTC')
        ids['btc'].text = f'Bitcoin - Dólar: ${values[0]} - Real: R${values[1]}'

        values = self.getQuotations('EUR')
        ids['euro'].text = f'Euro - Dólar: ${values[0]} - Real: R${values[1]}'
        return 

MyApp().run()