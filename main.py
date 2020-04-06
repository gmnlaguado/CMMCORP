from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
from os import listdir, path
from kivy.core.text import LabelBase
from kivy.core.window import Window
import sqlite3
from kivy.uix.label import Label
from kivy.uix.checkbox import CheckBox
from kivy.uix.boxlayout import BoxLayout
from assets.utilidades import Login

# from kivy.config import Config
# Config.set('graphics', 'width', '1280')
# Config.set('graphics', 'height', '800')
# Config.set('graphics', 'resizable', 0)
# Config.set('graphics', 'top', 115)
# Config.write()


class MyProgram(App):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.screens = []
        self.clases = []
        self.screenManager = None
        self.ventanas = ['Login', 'Panel', 'InformacionGeneral', 'DiagnosticoPerfil', 'IdeaNegocio', 'UnidadNegocio']
        self.dir_path = path.dirname(path.realpath(__file__))
        LabelBase.register(name='montserrat', fn_regular=self.dir_path + r"\assets\fonts\Montserrat-Regular.ttf",
                           fn_bold=self.dir_path + r"\assets\fonts\Montserrat-SemiBold.ttf")
        [Builder.load_file(f"windows/{f}") for f in listdir("windows")]

    def build(self):
        self.icon = self.dir_path + r'\assets\images\colflag.png'
        self.screenManager = ScreenManager()
        for idx, ventana in enumerate(self.ventanas):
            self.clases.append(type(ventana, (Screen,), {}))
            screen = self.clases[idx](name=ventana)
            self.screens.append(screen)
            self.screenManager.add_widget(self.screens[idx])
        self.screenManager.current = self.ventanas[0]
        self.diagnostico()
        return self.screenManager

    @staticmethod
    def LoginCheckMsg(username, password):
        return Login.checkIfRight(username, password)


    def diagnostico(self):
        conn = sqlite3.connect('assets/dbs/base.db')
        c = conn.cursor()
        c.execute("SELECT pregunta FROM preguntasDiagnostico")
        preguntas = [li[0] for li in c.fetchall()]

        container_id = self.screens[3].ids.container_grid
        container_id.bind(minimum_height=container_id.setter('height'))

        for idx, pregunta in enumerate(preguntas):

            lab = Label(text=f'{idx + 1}]  ' + pregunta, halign="justify", valign="middle", size_hint=(None, None),
                        size=(815, 51), color=(0, 0, 0, 0.85), font_size=20, font_name="montserrat",
                        text_size=(815, 51), id=f'pregunta_{idx}')

            BoxContainer = BoxLayout()
            for i in ['Si', 'MasMenos', 'No']:
                check = CheckBox(group=f"pregunta_{idx + 1}", color=(0, 1, 0, 1), id=i)
                BoxContainer.add_widget(check)

            container_id.add_widget(lab)
            container_id.add_widget(BoxContainer)


if __name__ == "__main__":
    corporacion = MyProgram()
    corporacion.title = "Corporación Mundial De La Mujer"
    Window.size = (1280, 800)
    Window.left = 45
    # Window.top = 30
    Window.top = -25
    Window.clearcolor = [1, 1, 1, 1]
    # Window.borderless = str(0)
    corporacion.run()
