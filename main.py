<<<<<<< HEAD
# coding=utf-8
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window
from kivy.core.text import LabelBase
from kivy.properties import ObjectProperty
from kivy.uix.popup import Popup
import utilidades


# ----------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------


class LoginScreen(Screen):
    # IDS
    id_username = ObjectProperty()
    id_password = ObjectProperty()
    id_mensaje = ObjectProperty()
    id_buttonIngresar = ObjectProperty()

    def check_username(self):
        self.id_mensaje.text = ""
        if utilidades.Comprobaciones.username(self.id_username.text):
            self.id_password.focus = True
        else:
            self.id_mensaje.text = "ODP incorrecto"

    def check_password(self):
        self.id_mensaje.text = ""
        if utilidades.Comprobaciones.password(self.id_password.text):
            if utilidades.Comprobaciones.username(self.id_username.text):
                self.id_mensaje.text = utilidades.Login.checkIfRight(self.id_username.text, self.id_password.text)
                if self.id_mensaje.text == "":
                    LoginProyectoPopup(self.id_username.text).open()
        else:
            self.id_mensaje.text = "Contraseña incorrecta"


class PanelScreen(Screen):
    # Costantes
    informacion = None

    # IDS
    id_proyecto = ObjectProperty()
    id_beneficiario = ObjectProperty()
    id_nuevobeneficiario = ObjectProperty()
    id_monitoreo = ObjectProperty()
    id_planformacion = ObjectProperty()
    id_consultar = ObjectProperty()
    id_inactivar = ObjectProperty()
    id_campliada = ObjectProperty()
    id_planimplementacion = ObjectProperty()
    id_planseguimiento = ObjectProperty()
    id_cargardatos = ObjectProperty()
    id_actualizar = ObjectProperty()

    def on_pre_enter(self):
        self.id_nuevobeneficiario.text = "Nuevo Beneficiario"
        self.id_monitoreo.text = "Monitoreo"
        self.id_planformacion.text = "Plan Formación"
        self.id_consultar.text = "Consultar"
        self.id_inactivar.text = "Inactivar"
        self.id_campliada.text = "C. Ampliada"
        self.id_planimplementacion.text = "Plan Implementación"
        self.id_planseguimiento.text = "Plan Seguimiento"
        self.id_cargardatos.text = "Cargar Datos"
        self.id_actualizar.text = "Actualizar"

    def nuevobeneficiario(self):
        self.id_proyecto.text = f'ODP {self.informacion[1]} Proyecto {self.informacion[0]}'
        EmergentNuevoBeneficiario(self.id_proyecto.text).open()


class InformacionGeneralScreen(Screen):
    id_titulo = ObjectProperty()
    id_nombre = ObjectProperty()
    id_apellido = ObjectProperty()
    id_nacimiento = ObjectProperty()
    id_edad = ObjectProperty()
    id_rangoEdad = ObjectProperty()
    id_tipoDocumento = ObjectProperty()
    id_deptoExpedicion = ObjectProperty()
    id_ciudadExpedicion = ObjectProperty()
    id_sexo = ObjectProperty()
    id_tipo = ObjectProperty()
    id_nacionalidad = ObjectProperty()
    id_pais = ObjectProperty()
    id_departamentos = ObjectProperty()
    id_ciudades = ObjectProperty()
    id_entorno = ObjectProperty()
    id_direccionLabel = ObjectProperty()
    id_rotulo = ObjectProperty()
    id_direccion = ObjectProperty()
    id_barrios = ObjectProperty()
    id_indicador = ObjectProperty()
    id_fijo = ObjectProperty()
    id_genero = ObjectProperty()
    id_celular = ObjectProperty()
    id_celular2 = ObjectProperty()
    id_etnia = ObjectProperty()
    id_discapacidad = ObjectProperty()
    id_email = ObjectProperty()
    id_labelMensajes = ObjectProperty()
    id_botonIngresar = ObjectProperty()

    def on_pre_enter(self):
        self.id_titulo.text = "Caracterización Básica"
        self.id_nombre.text = ""
        self.id_apellido.text = ""
        self.id_nacimiento.text = ""
        self.id_edad.text = "Edad"
        self.id_rangoEdad.text = "Rango"
        self.id_tipoDocumento.text = "Tipo de documento"
        self.id_deptoExpedicion.text = "Depto. Expedición"
        self.id_ciudadExpedicion.text = "Ciudad Expedición"
        self.id_sexo.text = "Sexo"
        self.id_tipo.text = "Tipo"
        self.id_nacionalidad.text = "Nacionalidad"
        self.id_pais.text = "Pais"
        self.id_departamentos.text = "Departamento"
        self.id_ciudades.text = "Ciudad"
        self.id_entorno.text = "Entorno"
        self.id_direccionLabel.text = "Dirección"
        self.id_rotulo.text = "Rótulo"
        self.id_direccion.text = ""
        self.id_barrios.text = "Barrio"
        self.id_indicador.text = "Indicador"
        self.id_fijo.text = ""
        self.id_genero.text = "Género"
        self.id_celular.text = ""
        self.id_celular2.text = ""
        self.id_etnia.text = "Etnia"
        self.id_discapacidad.text = "Cond. Discapacidad"
        self.id_email.text = ""
        self.id_labelMensajes.text = ""

# ----------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------

# Generado en la ventana LOGIN
class LoginProyectoPopup(Popup):
    # IDS
    id_proyectos = ObjectProperty()

    def __init__(self, *args, **kwargs):
        super().__init__(**kwargs)
        self.usuario = args[0]

    def on_open(self):
        self.title = f"ODP consultor {self.usuario} seleccione el proyecto en el que va a trabajar ahora"
        self.id_proyectos.values = utilidades.Login.proyectos(self.usuario)
        self.id_proyectos.bind(text=self.on_selection)

    def on_selection(self, *args):
        corporacion.sm.current = "Panel"
        PanelScreen.informacion = args[1], self.usuario
        self.dismiss()


# Generado en la ventana PANEL GENERAL
class EmergentNuevoBeneficiario(Popup):
    # IDS
    id_beneficiario = ObjectProperty()

    def __init__(self, *args, **kwargs):
        super().__init__(**kwargs)
        self.string = args[0]

    def on_open(self):
        self.title = f"Ingrese el documento correspondiente al beneficiario que va agregar"
        self.id_beneficiario.hint_text = "Documento"
        self.id_beneficiario.bind(on_text_validate=self.on_selection)

    def on_selection(self, *args):
        if utilidades.Panel.buscarBeneficiario(self.id_beneficiario.text, self.string) == "No existe":
            corporacion.sm.current = "InformacionGeneral"
        self.dismiss()


# ----------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------

class MyApp(App):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.sm = ScreenManager()

    def build(self):
        self.title = "Corporación Mundial De La Mujer"
        self.icon = r'images/colflag.png'
        LabelBase.register(name='montserrat', fn_regular='fonts/Montserrat-Regular.ttf',
                           fn_bold='fonts/Montserrat-SemiBold.ttf')

        # Archivos KV
        Builder.load_file("windows/Login.kv")
        Builder.load_file("windows/Panel.kv")
        Builder.load_file("windows/InformacionGeneral.kv")

        # Agregando ventanas al gestor de ventanas
        self.sm.add_widget(LoginScreen(name="Login"))
        self.sm.add_widget(PanelScreen(name="Panel"))
        self.sm.add_widget(InformacionGeneralScreen(name="InformacionGeneral"))

        self.sm.current = "Login"
        return self.sm


if __name__ == '__main__':
    Window.size = (1280, 800)
    Window.left = 45
    Window.top = -25
    Window.clearcolor = [1, 1, 1, 1]
    corporacion = MyApp()
=======
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
from assets.utilidades import Login, InfoGeneral, DiagnosticoPerfilP, IdeaNegocio, UnidadNegocio, CBasica

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
        self.screens[4].ids.ciiu.values = info[12]

        conn = sqlite3.connect('assets/dbs/base.db')
        c = conn.cursor()
        pais = "colombia"
        c.execute("SELECT departamentos.nombre FROM departamentos INNER JOIN paises ON paises.idPais = "
                  "departamentos.fkPais WHERE paises.nombre = :pais", {'pais': pais})
        deptos = [li[0] for li in c.fetchall()]
        self.screens[4].ids.departamentos.values = deptos


    def ciudadesIdeaNegocio(self, departamento):
        conn = sqlite3.connect('assets/dbs/base.db')
        c = conn.cursor()
        c.execute("SELECT ciudades.nombre FROM ciudades INNER JOIN departamentos ON departamentos.idDepartamento = "
                  "ciudades.fkDepartamento WHERE departamentos.nombre = :departamento", {'departamento': departamento})
        ciudades = [li[0] for li in c.fetchall()]
        self.screens[4].ids.ciudades.text = "Ciudad"
        self.screens[4].ids.ciudades.values = ciudades

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

    def ideaNegocio(self):
        if IdeaNegocio.comprobarTodo(self.screens[4].ids):
            return True
        return False

    def cargarUnidadNegocio(self):
        info = UnidadNegocio.cargarDatos()
        self.screens[5].ids.cuantosSocios.values = info[0]
        self.screens[5].ids.rotulo.values = info[1]
        self.screens[5].ids.indicador.values = info[2]
        self.screens[5].ids.sector.values = info[3]
        self.screens[5].ids.regCamara.values = info[4]
        self.screens[5].ids.conContrato.values = info[5]
        self.screens[5].ids.sinContrato.values = info[6]
        self.screens[5].ids.ciiu.values = info[7]
        self.screens[5].ids.departamentos.values = info[9]

    def ciudadesUnidadNegocio(self, departamento):
        conn = sqlite3.connect('assets/dbs/base.db')
        c = conn.cursor()
        c.execute("SELECT ciudades.nombre FROM ciudades INNER JOIN departamentos ON departamentos.idDepartamento = "
                  "ciudades.fkDepartamento WHERE departamentos.nombre = :departamento", {'departamento': departamento})
        ciudades = [li[0] for li in c.fetchall()]
        self.screens[5].ids.ciudades.text = "Ciudad"
        self.screens[5].ids.ciudades.values = ciudades

    def unidadNegocio(self):
        if UnidadNegocio.comprobarTodo(self.screens[5].ids):
            return True
        return False

    def caracterizacionBasica(self):
        CBasica.organizar(self.screens[1].ids, self.screens[2].ids, self.screens[3].ids.container_grid,
                          self.screens[4].ids, self.screens[5].ids)




if __name__ == "__main__":
    corporacion = MyProgram()
    corporacion.title = "Corporación Mundial De La Mujer"
    Window.size = (1280, 800)
    Window.left = 45
    # Window.top = 30
    Window.top = -25
    Window.clearcolor = [1, 1, 1, 1]
    # Window.borderless = str(0)
>>>>>>> 4bc45ba17b83da591ca351ac0867cdd31a67dd83
    corporacion.run()
