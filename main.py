# importar o App, Builder (GUI)
# # criar todo o aplicativo
# # criar a funcao de build

# inicializando o projeto
from kivy.app import App
from kivy.lang import Builder

# se estiver em pastas, colocar o path/nome do arquivo
GUI = Builder.load_file('screen.kv')

class MyApp(App):
    def build(self):
        return GUI
        