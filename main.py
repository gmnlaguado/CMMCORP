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
