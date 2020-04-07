# Icons made by www.flaticon.com

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
from assets.utilidades import Login, InfoGeneral, DiagnosticoPerfilP, IdeaNegocio

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

    def cargarInfoGeneral(self):
        info = InfoGeneral.cargarDatos()
        self.screens[2].ids.tipoDocumento.values = info[0]
        self.screens[2].ids.sexo.values = info[1]
        self.screens[2].ids.tipo.values = info[2]
        self.screens[2].ids.entorno.values = info[3]
        self.screens[2].ids.rotulo.values = info[4]
        self.screens[2].ids.indicador.values = info[5]
        self.screens[2].ids.genero.values = info[6]
        self.screens[2].ids.etnia.values = info[7]
        self.screens[2].ids.discapacidad.values = info[8]
        self.screens[2].ids.pais.values = info[9]
        self.screens[2].ids.nacionalidad.values = info[9]

        conn = sqlite3.connect('assets/dbs/base.db')
        c = conn.cursor()
        pais = "colombia"
        c.execute("SELECT departamentos.nombre FROM departamentos INNER JOIN paises ON paises.idPais = "
                  "departamentos.fkPais WHERE paises.nombre = :pais", {'pais': pais})
        deptos = [li[0] for li in c.fetchall()]
        self.screens[2].ids.deptoExpedicion.values = deptos

    def ciudadesExp(self, departamento):
        conn = sqlite3.connect('assets/dbs/base.db')
        c = conn.cursor()
        c.execute("SELECT ciudades.nombre FROM ciudades INNER JOIN departamentos ON departamentos.idDepartamento = "
                  "ciudades.fkDepartamento WHERE departamentos.nombre = :departamento", {'departamento': departamento})
        ciudades = [li[0] for li in c.fetchall()]
        self.screens[2].ids.ciudadExpedicion.text = "Ciudad Expedición"
        self.screens[2].ids.ciudadExpedicion.values = ciudades

    def departamentos(self, pais):
        conn = sqlite3.connect('assets/dbs/base.db')
        c = conn.cursor()
        c.execute("SELECT departamentos.nombre FROM departamentos INNER JOIN paises ON paises.idPais = "
                  "departamentos.fkPais WHERE paises.nombre = :pais", {'pais': pais})
        deptos = [li[0] for li in c.fetchall()]
        self.screens[2].ids.departamentos.text = "Departamento"
        self.screens[2].ids.departamentos.values = deptos

    def ciudades(self, departamento):
        conn = sqlite3.connect('assets/dbs/base.db')
        c = conn.cursor()
        c.execute("SELECT ciudades.nombre FROM ciudades INNER JOIN departamentos ON departamentos.idDepartamento = "
                  "ciudades.fkDepartamento WHERE departamentos.nombre = :departamento", {'departamento': departamento})
        ciudades = [li[0] for li in c.fetchall()]
        self.screens[2].ids.ciudades.text = "Ciudad"
        self.screens[2].ids.ciudades.values = ciudades

    def barrios(self, ciudad):
        conn = sqlite3.connect('assets/dbs/base.db')
        c = conn.cursor()
        c.execute("SELECT barrios.nombre FROM barrios INNER JOIN ciudades ON ciudades.idCiudad = "
                  "barrios.fkCiudad WHERE ciudades.nombre = :ciudad", {'ciudad': ciudad})
        barrios = [li[0] for li in c.fetchall()]
        self.screens[2].ids.barrios.text = "Barrio"
        self.screens[2].ids.barrios.values = barrios

    def informacionGeneral(self):
        if InfoGeneral.comprobarTodo(self.screens[2].ids):
            return True
        return False

    def diagnosticoPerfilProductivo(self):
        if DiagnosticoPerfilP.comprobarTodo(self.screens[3].ids.container_grid):
            return self.screens[2].ids.tipo.text
        return "no"

    def cargarIdeaNegocio(self):
        info = IdeaNegocio.cargarDatos()
        self.screens[4].ids.sectorEmpresarial.values = info[0]
        self.screens[4].ids.comoSurge.values = info[1]
        self.screens[4].ids.tiempoSemanal.values = info[2]
        self.screens[4].ids.estudios.values = info[3]
        self.screens[4].ids.tieneExperiencia.values = info[4]
        self.screens[4].ids.productoServicio.values = info[5]
        self.screens[4].ids.esAgropecuario.values = info[6]
        self.screens[4].ids.necesitaColaboradores.values = info[7]
        self.screens[4].ids.mesesQueLleva.values = info[8]
        self.screens[4].ids.tiempoADedicar.values = info[9]
        self.screens[4].ids.porqueNo.values = info[10]
        self.screens[4].ids.porcentajeInversion.values = info[11]

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
