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
    listaIdsInputs = []
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
        self.id_fijo.input_type = 'number'
        self.id_celular.input_type = 'number'
        self.id_celular2.input_type = 'number'

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

        # Cargando los valores de las listas deplegables
        datos = utilidades.InfoGeneral.cargarDatos()
        self.id_tipoDocumento.values = datos[0]
        self.id_sexo.values = datos[1]
        self.id_tipo.values = datos[2]
        self.id_entorno.values = datos[3]
        self.id_rotulo.values = datos[4]
        self.id_indicador.values = datos[5]
        self.id_genero.values = datos[6]
        self.id_etnia.values = datos[7]
        self.id_discapacidad.values = datos[8]
        self.id_nacionalidad.values = datos[9]
        self.id_pais.values = datos[9]
        self.id_deptoExpedicion.values = datos[10]

        self.id_pais.bind(text=self.on_selection_pais)
        self.id_deptoExpedicion.bind(text=self.on_selection_deptoExpedicion)
        self.id_departamentos.bind(text=self.on_selection_departamentos)
        self.id_ciudades.bind(text=self.on_selection_ciudades)

        self.id_tipoDocumento.bind(text=self.cambiar_color)
        self.id_sexo.bind(text=self.cambiar_color)
        self.id_tipo.bind(text=self.cambiar_color)
        self.id_entorno.bind(text=self.cambiar_color)
        self.id_rotulo.bind(text=self.cambiar_color)
        self.id_indicador.bind(text=self.cambiar_color)
        self.id_genero.bind(text=self.cambiar_color)
        self.id_etnia.bind(text=self.cambiar_color)
        self.id_discapacidad.bind(text=self.cambiar_color)
        self.id_ciudadExpedicion.bind(text=self.cambiar_color)
        self.id_barrios.bind(text=self.cambiar_color)
        self.id_nacionalidad.bind(text=self.cambiar_color)

        self.id_botonIngresar.bind(on_press=self.verificarTodo)

    def verificarTodo(self, *args):
        self.id_labelMensajes.text = ""
        if self.id_nombre.text == "" or self.id_apellido.text == "" or self.id_nacimiento.text == "" or\
        self.id_tipoDocumento.text == "Tipo de documento" or self.id_deptoExpedicion.text == "Depto. Expedición" or\
        self.id_ciudadExpedicion.text == "Ciudad Expedición" or self.id_sexo.text == "Sexo" or\
        self.id_tipo.text == "Tipo" or self.id_nacionalidad.text == "Nacionalidad" or self.id_pais.text == "Pais" or\
        self.id_departamentos.text == "Departamento" or self.id_ciudades.text == "Ciudad" or\
        self.id_entorno.text == "Entorno" or\
        self.id_rotulo.text == "Rótulo" or self.id_direccion.text == "" or self.id_barrios.text == "Barrio" or\
        self.id_indicador.text == "Indicador" or self.id_fijo.text == "" or self.id_genero.text == "Género" or\
        self.id_celular.text == "" or self.id_celular2.text == "" or self.id_etnia.text == "Etnia" or\
        self.id_discapacidad.text == "Cond. Discapacidad" or self.id_email.text == "":
            self.id_labelMensajes.text = "Formulario incompleto"

    def cambiar_color(self, *args):
        args[0].background_color = 11 / 255, 69 / 255, 0 / 255, 0.7

    def on_selection_pais(self, *args):
        self.id_departamentos.values = utilidades.InfoGeneral.cargarDepartamentos(args[1])
        self.id_pais.background_color = 11 / 255, 69 / 255, 0 / 255, 0.7

    def on_selection_deptoExpedicion(self, *args):
        self.id_ciudadExpedicion.values = utilidades.InfoGeneral.cargarCiudades(args[1])
        self.id_deptoExpedicion.background_color = 11 / 255, 69 / 255, 0 / 255, 0.7

    def on_selection_departamentos(self, *args):
        self.id_ciudades.values = utilidades.InfoGeneral.cargarCiudades(args[1])
        self.id_departamentos.background_color = 11 / 255, 69 / 255, 0 / 255, 0.7

    def on_selection_ciudades(self, *args):
        self.id_barrios.values = utilidades.InfoGeneral.cargarBarrios(args[1])
        self.id_ciudades.background_color = 11 / 255, 69 / 255, 0 / 255, 0.7

    def on_pre_leave(self, *args):
        pass




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
    corporacion.run()
