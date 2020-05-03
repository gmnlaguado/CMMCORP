# coding=utf-8
from os import listdir
from kivy.app import App
from kivy.lang import Builder
from kivy.factory import Factory
from kivy.core.window import Window
from kivy.core.text import LabelBase
from kivy.uix.screenmanager import ScreenManager
from windows import Login, Panel, InformacionGeneral, DiagnosticoPerfilProductivo, IdeaDeNegocio, UnidadDeNegocio, \
    CaracterizacionAmpliada, Monitoreo


class MyApp(App):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.sm = ScreenManager()

    def build(self):
        self.title = "Corporación Mundial De La Mujer"
        self.icon = r'images/colflag.png'
        LabelBase.register(name='montserrat', fn_regular='fonts/Montserrat-Regular.ttf',
                           fn_bold='fonts/Montserrat-SemiBold.ttf')

        for f in listdir("windows"):
            if f.endswith('.kv'):
                Builder.load_file(f"windows/{f}")
        Builder.load_file('declarations/templates_declaration.kv')

        self.sm.add_widget(Login.LoginScreen(name='Login'))
        self.sm.add_widget(Panel.PanelScreen(name="Panel"))
        self.sm.add_widget(InformacionGeneral.InformacionGeneralScreen(name="InformacionGeneral"))
        self.sm.add_widget(
            DiagnosticoPerfilProductivo.DiagnosticoPerfilProductivoScreen(name="DiagnosticoPerfilProductivo"))
        self.sm.add_widget(IdeaDeNegocio.IdeaDeNegocioScreen(name="IdeaDeNegocio"))
        self.sm.add_widget(UnidadDeNegocio.UnidadDeNegocioScreen(name="UnidadDeNegocio"))
        self.sm.add_widget(CaracterizacionAmpliada.CaracterizacionAmpliadaScreen(name="CaracterizacionAmpliada"))
        self.sm.add_widget(Monitoreo.MonitoreoScreen(name="Monitoreo"))
        self.sm.current = 'Login'

        Factory.LoginProjectPopup.changeWindow = self.changeToPanel
        Factory.EmergentNuevoBeneficiario.changeWindow = self.changeToInformacionGeneral
        Factory.AcceptForm.changeWindow = self.changeToDiagnosticoPerfilProductivo

        return self.sm

    def changeToPanel(self, *args):
        self.sm.current = 'Panel'

    def changeToInformacionGeneral(self, *args):
        self.sm.current = 'InformacionGeneral'

    def changeToDiagnosticoPerfilProductivo(self, *args):
        self.sm.current = 'DiagnosticoPerfilProductivo'


if __name__ == '__main__':
    Window.size = (1280, 800)
    Window.left = 45
    Window.top = -25
    Window.clearcolor = [1, 1, 1, 1]
    Window.softinput_mode = "below_target"
    corporation = MyApp()
    corporation.run()
