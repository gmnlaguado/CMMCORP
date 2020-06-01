# coding=utf-8
from os import listdir
from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.core.text import LabelBase
from kivy.uix.screenmanager import ScreenManager
from windows import Login, Panel, InformacionGeneral, DiagnosticoPerfilProductivo, IdeaDeNegocio, UnidadDeNegocio, CaracterizacionAmpliada, Monitoreo, DiagnosticoEmpresarial, PlanDeFormacion, ActividadDeFormacion, PlanDeImplementacion


class MyApp(App):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.sm = ScreenManager()

    def build(self):
        LabelBase.register(name='montserrat', fn_regular='fonts/Montserrat-Regular.ttf',
                           fn_bold='fonts/Montserrat-SemiBold.ttf')

        Builder.load_file(f"windows/Login.kv")
        Builder.load_file(f"windows/Panel.kv")
        Builder.load_file(f"windows/InformacionGeneral.kv")
        Builder.load_file(f"windows/DiagnosticoPerfilProductivo.kv")
        Builder.load_file(f"windows/IdeaDeNegocio.kv")
        Builder.load_file(f"windows/UnidadDeNegocio.kv")
        Builder.load_file(f"windows/CaracterizacionAmpliada.kv")
        Builder.load_file(f"windows/Monitoreo.kv")
        Builder.load_file(f"windows/DiagnosticoEmpresarial.kv")
        Builder.load_file(f"windows/PlanDeFormacion.kv")
        Builder.load_file(f"windows/ActividadDeFormacion.kv")
        Builder.load_file(f"windows/PlanDeImplementacion.kv")

        Builder.load_file('declarations/templates_declaration.kv')

        self.sm.add_widget(Login.LoginScreen(name='Login'))
        self.sm.add_widget(Panel.PanelScreen(name="Panel"))
        self.sm.add_widget(InformacionGeneral.InformacionGeneralScreen(name="InformacionGeneral"))
        self.sm.add_widget(DiagnosticoPerfilProductivo.DiagnosticoPerfilProductivoScreen(name="DiagnosticoPerfilProductivo"))
        self.sm.add_widget(IdeaDeNegocio.IdeaDeNegocioScreen(name="IdeaDeNegocio"))
        self.sm.add_widget(UnidadDeNegocio.UnidadDeNegocioScreen(name="UnidadDeNegocio"))
        self.sm.add_widget(CaracterizacionAmpliada.CaracterizacionAmpliadaScreen(name="CaracterizacionAmpliada"))
        self.sm.add_widget(Monitoreo.MonitoreoScreen(name="Monitoreo"))
        self.sm.add_widget(DiagnosticoEmpresarial.DiagnosticoEmpresarialScreen(name="DiagnosticoEmpresarial"))
        self.sm.add_widget(PlanDeFormacion.PlanDeFormacionScreen(name="PlanDeFormacion"))
        self.sm.add_widget(ActividadDeFormacion.ActividadDeFormacionScreen(name="ActividadDeFormacion"))
        self.sm.add_widget(PlanDeImplementacion.PlanDeImplementacionScreen(name="PlanDeImplementacion"))
        self.sm.current = 'PlanDeImplementacion'

        return self.sm


if __name__ == '__main__':
    Window.size = (1280, 800)
    Window.left = 45
    Window.top = -25
    Window.clearcolor = [1, 1, 1, 1]
    corporation = MyApp()
    corporation.run()
