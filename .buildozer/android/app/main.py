# coding=utf-8
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window
from kivy.core.text import LabelBase
from kivy.properties import ObjectProperty
from kivy.uix.popup import Popup
import utilidades
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.checkbox import CheckBox
from kivy.uix.label import Label
from kivy.uix.spinner import Spinner


# ----------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------


class LoginScreen(Screen):
    # IDS
    id_username = ObjectProperty()
    id_password = ObjectProperty()
    id_mensaje = ObjectProperty()
    id_buttonIngresar = ObjectProperty()

    # Referencias estáticas
    static_logo = ObjectProperty()
    static_usuario = ObjectProperty()
    static_contra = ObjectProperty()

    def on_pre_enter(self, *args):
        # Definiciones
        self.static_usuario.text = "ODP Consultor"
        self.static_contra.text = "Contraseña"
        self.id_buttonIngresar.text = "Ingresar"

        # Enlazamientos
        self.id_username.bind(on_text_validate=self.check_username)
        self.id_password.bind(on_text_validate=self.check_password)
        self.id_buttonIngresar.bind(on_release=self.check_password)

    def check_username(self, *args):
        self.id_mensaje.text = ""
        if utilidades.Comprobaciones.username(self.id_username.text):
            self.id_password.focus = True
        else:
            self.id_mensaje.text = "ODP incorrecto"

    def check_password(self, *args):
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

    # Referencias estáticas
    static_titulo = ObjectProperty()

    def on_pre_enter(self):
        # Definiciones
        self.static_titulo.text = "Panel General"
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
        self.id_proyecto.text = f'ODP {self.informacion[1]} Proyecto {self.informacion[0]}'

        # Enlazamientos
        self.id_nuevobeneficiario.bind(on_release=self.nuevobeneficiario)
        self.id_inactivar.bind(on_release=self.on_inactivar)
        self.id_campliada.bind(on_release=self.on_campliada)

    # Métodos de la pantalla

    def nuevobeneficiario(self, *args):
        EmergentNuevoBeneficiario(self.id_proyecto.text).open()

    def on_inactivar(self, *args):
        InactivarBeneficiario(self.informacion[0]).open()

    def on_campliada(self, *args):
        CaracterizaAmpliada(self.informacion[0]).open()


class InformacionGeneralScreen(Screen):
    # Costantes
    informacion = None
    beneficiario = None

    # IDS
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
        # Restricciones
        self.id_fijo.input_type = 'number'
        self.id_celular.input_type = 'number'
        self.id_celular2.input_type = 'number'

        # Inicializando Caracteres
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

        # Iniciar todos los spinners con el color desactivado
        self.id_tipoDocumento.background_color = 61 / 255, 119 / 255, 0 / 255, 0.7
        self.id_sexo.background_color = 61 / 255, 119 / 255, 0 / 255, 0.7
        self.id_tipo.background_color = 61 / 255, 119 / 255, 0 / 255, 0.7
        self.id_entorno.background_color = 61 / 255, 119 / 255, 0 / 255, 0.7
        self.id_rotulo.background_color = 61 / 255, 119 / 255, 0 / 255, 0.7
        self.id_indicador.background_color = 61 / 255, 119 / 255, 0 / 255, 0.7
        self.id_genero.background_color = 61 / 255, 119 / 255, 0 / 255, 0.7
        self.id_etnia.background_color = 61 / 255, 119 / 255, 0 / 255, 0.7
        self.id_discapacidad.background_color = 61 / 255, 119 / 255, 0 / 255, 0.7
        self.id_ciudadExpedicion.background_color = 61 / 255, 119 / 255, 0 / 255, 0.7
        self.id_barrios.background_color = 61 / 255, 119 / 255, 0 / 255, 0.7
        self.id_nacionalidad.background_color = 61 / 255, 119 / 255, 0 / 255, 0.7
        self.id_pais.background_color = 61 / 255, 119 / 255, 0 / 255, 0.7
        self.id_deptoExpedicion.background_color = 61 / 255, 119 / 255, 0 / 255, 0.7
        self.id_departamentos.background_color = 61 / 255, 119 / 255, 0 / 255, 0.7
        self.id_ciudades.background_color = 61 / 255, 119 / 255, 0 / 255, 0.7

        # Iniciar todos los Text Inputs con el color desactivado
        self.id_nombre.background_color = 255 / 255, 255 / 255, 255 / 255, 1
        self.id_apellido.background_color = 255 / 255, 255 / 255, 255 / 255, 1
        self.id_nacimiento.background_color = 255 / 255, 255 / 255, 255 / 255, 1
        self.id_fijo.background_color = 255 / 255, 255 / 255, 255 / 255, 1
        self.id_celular.background_color = 255 / 255, 255 / 255, 255 / 255, 1
        self.id_celular2.background_color = 255 / 255, 255 / 255, 255 / 255, 1
        self.id_direccion.background_color = 255 / 255, 255 / 255, 255 / 255, 1
        self.id_email.background_color = 255 / 255, 255 / 255, 255 / 255, 1

        # Estableciendo el enlace con los spinner cuya selección determina el valor de otros
        self.id_pais.bind(text=self.on_selection_pais)
        self.id_deptoExpedicion.bind(text=self.on_selection_deptoExpedicion)
        self.id_departamentos.bind(text=self.on_selection_departamentos)
        self.id_ciudades.bind(text=self.on_selection_ciudades)

        # Métodos que cambian el color del spinner cuando son seleccionados
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

        # Método que verificará si el formulario fue totalmente diligenciado
        self.id_botonIngresar.bind(on_press=self.verificarTodo)

        # Métodos de verificación individual de cada Text Input
        self.id_nombre.bind(on_text_validate=self.check_name)
        self.id_apellido.bind(on_text_validate=self.check_name)
        self.id_nacimiento.bind(on_text_validate=self.check_data)
        self.id_fijo.bind(on_text_validate=self.check_fijo)
        self.id_celular.bind(on_text_validate=self.check_celular)
        self.id_celular2.bind(on_text_validate=self.check_celular)
        self.id_direccion.bind(on_text_validate=self.check_input)
        self.id_email.bind(on_text_validate=self.check_input)

    def check_name(self, *args):
        self.id_labelMensajes.text = ""
        if utilidades.Comprobaciones.username(args[0].text):
            args[0].background_color = 7 / 255, 7 / 255, 7 / 255, 0.1
        else:
            args[0].background_color = 255 / 255, 255 / 255, 255 / 255, 1
            self.id_labelMensajes.text = "Error en el campo de texto"

    def check_data(self, *args):
        self.id_labelMensajes.text = ""
        if utilidades.Comprobaciones.data(args[0].text):
            args[0].background_color = 7 / 255, 7 / 255, 7 / 255, 0.1
            res = utilidades.InfoGeneral.calcular_edad(args[0].text)
            self.id_edad.text = f'Edad {res[0]}'
            if res[1] == "Más de 60":
                self.id_rangoEdad.text = f'{res[1]}'
            else:
                self.id_rangoEdad.text = f'Rango {res[1]}'
        else:
            args[0].background_color = 255 / 255, 255 / 255, 255 / 255, 1
            self.id_labelMensajes.text = "Error en el campo de fecha"

    def check_fijo(self, *args):
        self.id_labelMensajes.text = ""
        if utilidades.Comprobaciones.fijo(args[0].text):
            args[0].background_color = 7 / 255, 7 / 255, 7 / 255, 0.1
        else:
            args[0].background_color = 255 / 255, 255 / 255, 255 / 255, 1
            self.id_labelMensajes.text = "Error en el teléfono fijo"

    def check_celular(self, *args):
        self.id_labelMensajes.text = ""
        if utilidades.Comprobaciones.celular(args[0].text):
            args[0].background_color = 7 / 255, 7 / 255, 7 / 255, 0.1
        else:
            args[0].background_color = 255 / 255, 255 / 255, 255 / 255, 1
            self.id_labelMensajes.text = "Error en el número celular"

    def check_input(self, *args):
        self.id_labelMensajes.text = ""
        if len(args[0].text.strip()) > 0:
            args[0].background_color = 7 / 255, 7 / 255, 7 / 255, 0.1
        else:
            self.id_labelMensajes.text = "No se permiten campos vacios"

    def verificarTodo(self, *args):
        self.id_labelMensajes.text = ""
        if self.id_nombre.text == "" or self.id_apellido.text == "" or self.id_nacimiento.text == "" or \
                self.id_tipoDocumento.text == "Tipo de documento" or \
                self.id_deptoExpedicion.text == "Depto. Expedición" or \
                self.id_ciudadExpedicion.text == "Ciudad Expedición" or self.id_sexo.text == "Sexo" or \
                self.id_tipo.text == "Tipo" or self.id_nacionalidad.text == "Nacionalidad" or \
                self.id_pais.text == "Pais" or self.id_departamentos.text == "Departamento" or \
                self.id_ciudades.text == "Ciudad" or self.id_entorno.text == "Entorno" or \
                self.id_rotulo.text == "Rótulo" or self.id_direccion.text == "" or self.id_barrios.text == "Barrio" or \
                self.id_indicador.text == "Indicador" or self.id_fijo.text == "" or self.id_genero.text == "Género" or \
                self.id_celular.text == "" or self.id_celular2.text == "" or self.id_etnia.text == "Etnia" or \
                self.id_discapacidad.text == "Cond. Discapacidad" or self.id_email.text == "":
            self.id_labelMensajes.text = "Formulario incompleto"
        else:
            if utilidades.Comprobaciones.name(self.id_nombre.text) and \
                    utilidades.Comprobaciones.name(self.id_apellido.text) and \
                    utilidades.Comprobaciones.data(self.id_nacimiento.text) and \
                    utilidades.Comprobaciones.fijo(self.id_fijo.text) and \
                    utilidades.Comprobaciones.celular(self.id_celular.text) and \
                    utilidades.Comprobaciones.celular(self.id_celular2.text):
                DiagnosticoPerfilProductivoScreen.tipo_beneficiario = self.id_tipo.text
                ConfirmacionInfoGeneral().open()
            else:
                self.id_labelMensajes.text = "Error en algunos campos"

    @staticmethod
    def cambiar_color(*args):
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
        proyecto = utilidades.InfoGeneral.identidadProyecto(self.informacion[0])
        beneficiariosproyectos = [proyecto, self.beneficiario, 1]

        utilidades.InfoGeneral.ingresarInformacion(
            beneficiariosproyectos,
            self.beneficiario,
            self.id_nombre.text,
            self.id_apellido.text,
            self.id_nacimiento.text,
            self.id_nacionalidad.text,
            self.id_tipoDocumento.text,
            self.id_ciudadExpedicion.text,
            self.id_pais.text,
            self.id_departamentos.text,
            self.id_ciudades.text,
            self.id_barrios.text.upper(),
            self.id_entorno.text,
            self.id_direccion.text,
            self.id_sexo.text,
            int(self.id_indicador.text),
            int(self.id_fijo.text),
            self.id_email.text,
            self.id_genero.text,
            self.id_etnia.text,
            self.id_discapacidad.text,
            int(self.id_celular.text),
            int(self.id_celular2.text),
            self.id_tipo.text
        )


class DiagnosticoPerfilProductivoScreen(Screen):
    # Costants
    beneficiario = None
    tipo_beneficiario = ""
    creacion = False

    # IDS
    id_container_grid = ObjectProperty()
    id_labelMensajes = ObjectProperty()
    id_botonIngresar = ObjectProperty()

    def on_pre_enter(self):
        # Si las preguntas ya fueron creadas, desactive todas las respuestas
        if self.creacion:
            for idx1, grid in enumerate(self.id_container_grid.children):
                if len(grid.children) > 0:
                    for idx2, box in enumerate(grid.children):
                        if box.active:
                            self.id_container_grid.children[idx1].children[idx2].active = False

        if not self.creacion:
            self.id_botonIngresar.bind(on_press=self.verificarTodo)
            preguntas = utilidades.DiagnosticoPerfil.cargarPreguntas()
            self.id_container_grid.bind(minimum_height=self.id_container_grid.setter('height'))
            for idx, pregunta in enumerate(preguntas):
                lab = Label(text=f'{idx + 1}]  ' + pregunta, halign="justify", valign="middle", size_hint=(None, None),
                            size=(815, 51), color=(0, 0, 0, 0.85), font_size=20, font_name="montserrat",
                            text_size=(815, 51), id=f'pregunta_{idx}')
                box_container = BoxLayout()
                for i in ['Si', 'MasMenos', 'No']:
                    check = CheckBox(group=f"pregunta_{idx + 1}", color=(0, 1, 0, 1), id=i)
                    box_container.add_widget(check)
                self.id_container_grid.add_widget(lab)
                self.id_container_grid.add_widget(box_container)
            self.creacion = True

    def verificarTodo(self, *args):
        self.id_labelMensajes.text = ""
        for grid in self.id_container_grid.children:
            if len(grid.children) > 0 and not True in [box.active for box in grid.children]:
                self.id_labelMensajes.text = "Faltan preguntas por responder"

        if self.id_labelMensajes.text == "":
            diagnostico_perfil_productivo = []
            count = 0
            for grid in self.id_container_grid.children:
                if len(grid.children) > 0:
                    repp = [box.active for box in grid.children][::-1].index(True)
                    diagnostico_perfil_productivo.append([self.beneficiario, 70 - count, repp])
                    count += 1

            diagnostico_perfil_productivo = diagnostico_perfil_productivo[::-1]
            utilidades.DiagnosticoPerfil.subirBase(diagnostico_perfil_productivo)
            if self.tipo_beneficiario == "Emprendedor":
                corporacion.sm.current = "IdeaNegocio"
            else:
                corporacion.sm.current = "UnidadNegocio"


class IdeaNegocioScreen(Screen):
    # Costantes
    informacion = None
    beneficiario = None
    lista_productos_servicios = ""
    lista_colaboradores = ""

    # IDS
    id_emprendimiento = ObjectProperty()
    id_sectorEmpresarial = ObjectProperty()
    id_ciudades = ObjectProperty()
    id_estudios = ObjectProperty()
    id_esAgropecuario = ObjectProperty()
    id_necesitaColaboradores = ObjectProperty()
    id_tiempoSemanal = ObjectProperty()
    id_porqueNo = ObjectProperty()
    id_mesesQueLleva = ObjectProperty()
    id_ciiu = ObjectProperty()
    id_comoSurge = ObjectProperty()
    id_tieneExperiencia = ObjectProperty()
    id_departamentos = ObjectProperty()
    id_tiempoADedicar = ObjectProperty()
    id_productoServicio = ObjectProperty()
    id_portafolio = ObjectProperty()
    id_inversionActivos = ObjectProperty()
    id_porcentajeInversion = ObjectProperty()
    id_ventasPrimerMes = ObjectProperty()
    id_inversionInicial = ObjectProperty()
    id_invCapitalTrabajo = ObjectProperty()
    id_ventasPrimerAno = ObjectProperty()
    id_imagine = ObjectProperty()
    id_labelMensajes = ObjectProperty()
    id_botonIngresar = ObjectProperty()

    def on_pre_enter(self):
        # Restricciones
        self.id_inversionActivos.input_type = 'number'
        self.id_ventasPrimerMes.input_type = 'number'
        self.id_inversionInicial.input_type = 'number'
        self.id_invCapitalTrabajo.input_type = 'number'
        self.id_ventasPrimerAno.input_type = 'number'

        # Inicializando Caracteres
        self.id_emprendimiento.text = ""
        self.id_sectorEmpresarial.text = "Sector Empresarial"
        self.id_ciudades.text = "Ciudad"
        self.id_estudios.text = "Estudios sobre el tema"
        self.id_esAgropecuario.text = "¿Agropecuario?"
        self.id_necesitaColaboradores.text = "Necesita colaboradores"
        self.id_tiempoSemanal.text = "Tiempo semanal a dedicar"
        self.id_porqueNo.text = "¿Por qué no empezaba?"
        self.id_mesesQueLleva.text = "Meses que lleva el negocio"
        self.id_ciiu.text = "CIIU"
        self.id_comoSurge.text = "¿Cómo surge la idea?"
        self.id_tieneExperiencia.text = "¿Experiencia?"
        self.id_departamentos.text = "Departamento"
        self.id_tiempoADedicar.text = "Tiempo a dedicar"
        self.id_productoServicio.text = "Producto / Servicio"
        self.id_portafolio.text = ""
        self.id_inversionActivos.text = ""
        self.id_porcentajeInversion.text = "% Inversión"
        self.id_ventasPrimerMes.text = ""
        self.id_inversionInicial.text = ""
        self.id_invCapitalTrabajo.text = ""
        self.id_ventasPrimerAno.text = ""
        self.id_imagine.text = ""
        self.id_labelMensajes.text = ""
        self.id_botonIngresar.text = "Ingresar"

        # Cargando los valores de las listas deplegables
        info = utilidades.IdeaNegocio.cargarDatos()
        self.id_sectorEmpresarial.values = info[0]
        self.id_estudios.values = info[1]
        self.id_esAgropecuario.values = info[2]
        self.id_necesitaColaboradores.values = info[3]
        self.id_tiempoSemanal.values = info[4]
        self.id_porqueNo.values = info[5]
        self.id_mesesQueLleva.values = info[6]
        self.id_ciiu.values = info[12]
        self.id_comoSurge.values = info[7]
        self.id_tieneExperiencia.values = info[8]
        self.id_departamentos.values = info[13]
        self.id_tiempoADedicar.values = info[9]
        self.id_productoServicio.values = info[10]
        self.id_portafolio.hint_text = "Portafolio"
        self.id_inversionActivos.hint_text = "Inv. Activos"
        self.id_porcentajeInversion.values = info[11]
        self.id_ventasPrimerMes.hint_text = "Ventas primer mes"
        self.id_inversionInicial.hint_text = "Inv. Inicial"
        self.id_invCapitalTrabajo.hint_text = "Inv. Capital Trabajo"
        self.id_ventasPrimerAno.hint_text = "Ventas Primer año"
        self.id_imagine.hint_text = "Imagine su negocio"

        # Iniciar todos los spinners con el color desactivado
        self.id_sectorEmpresarial.background_color = 61 / 255, 119 / 255, 0 / 255, 0.7
        self.id_estudios.background_color = 61 / 255, 119 / 255, 0 / 255, 0.7
        self.id_esAgropecuario.background_color = 61 / 255, 119 / 255, 0 / 255, 0.7
        self.id_necesitaColaboradores.background_color = 61 / 255, 119 / 255, 0 / 255, 0.7
        self.id_tiempoSemanal.background_color = 61 / 255, 119 / 255, 0 / 255, 0.7
        self.id_porqueNo.background_color = 61 / 255, 119 / 255, 0 / 255, 0.7
        self.id_mesesQueLleva.background_color = 61 / 255, 119 / 255, 0 / 255, 0.7
        self.id_ciiu.background_color = 61 / 255, 119 / 255, 0 / 255, 0.7
        self.id_comoSurge.background_color = 61 / 255, 119 / 255, 0 / 255, 0.7
        self.id_tieneExperiencia.background_color = 61 / 255, 119 / 255, 0 / 255, 0.7
        self.id_departamentos.background_color = 61 / 255, 119 / 255, 0 / 255, 0.7
        self.id_tiempoADedicar.background_color = 61 / 255, 119 / 255, 0 / 255, 0.7
        self.id_productoServicio.background_color = 61 / 255, 119 / 255, 0 / 255, 0.7
        self.id_porcentajeInversion.background_color = 61 / 255, 119 / 255, 0 / 255, 0.7
        self.id_ciudades.background_color = 61 / 255, 119 / 255, 0 / 255, 0.7

        # Iniciar todos los Text Inputs con el color desactivado
        self.id_emprendimiento.background_color = 255 / 255, 255 / 255, 255 / 255, 1
        self.id_portafolio.background_color = 255 / 255, 255 / 255, 255 / 255, 1
        self.id_inversionActivos.background_color = 255 / 255, 255 / 255, 255 / 255, 1
        self.id_ventasPrimerMes.background_color = 255 / 255, 255 / 255, 255 / 255, 1
        self.id_inversionInicial.background_color = 255 / 255, 255 / 255, 255 / 255, 1
        self.id_invCapitalTrabajo.background_color = 255 / 255, 255 / 255, 255 / 255, 1
        self.id_ventasPrimerAno.background_color = 255 / 255, 255 / 255, 255 / 255, 1
        self.id_imagine.background_color = 255 / 255, 255 / 255, 255 / 255, 1

        # Estableciendo el enlace con los spinner cuya selección determina el valor de otros
        self.id_departamentos.bind(text=self.on_selection_departamentos)

        # Métodos que cambian el color del spinner cuando son seleccionados
        self.id_sectorEmpresarial.bind(text=self.cambiar_color)
        self.id_ciudades.bind(text=self.cambiar_color)
        self.id_estudios.bind(text=self.cambiar_color)
        self.id_esAgropecuario.bind(text=self.cambiar_color)
        self.id_necesitaColaboradores.bind(text=self.necesitaCol)
        self.id_tiempoSemanal.bind(text=self.cambiar_color)
        self.id_porqueNo.bind(text=self.cambiar_color)
        self.id_mesesQueLleva.bind(text=self.cambiar_color)
        self.id_ciiu.bind(text=self.cambiar_color)
        self.id_comoSurge.bind(text=self.cambiar_color)
        self.id_tieneExperiencia.bind(text=self.cambiar_color)
        self.id_tiempoADedicar.bind(text=self.cambiar_color)
        self.id_productoServicio.bind(text=self.productosservs)
        self.id_porcentajeInversion.bind(text=self.cambiar_color)

        # Método que verificará si el formulario fue totalmente diligenciado
        self.id_botonIngresar.bind(on_press=self.comprobarTodo)

        # Métodos de verificación individual de cada Text Input
        self.id_emprendimiento.bind(on_text_validate=self.check_name)
        self.id_portafolio.bind(on_text_validate=self.check_name)
        self.id_inversionActivos.bind(on_text_validate=self.check_dinero)
        self.id_ventasPrimerMes.bind(on_text_validate=self.check_dinero)
        self.id_inversionInicial.bind(on_text_validate=self.check_dinero)
        self.id_invCapitalTrabajo.bind(on_text_validate=self.check_dinero)
        self.id_ventasPrimerAno.bind(on_text_validate=self.check_dinero)
        self.id_imagine.bind(on_text_validate=self.check_name)

    def check_name(self, *args):
        self.id_labelMensajes.text = ""
        if utilidades.Comprobaciones.name(args[0].text):
            args[0].background_color = 7 / 255, 7 / 255, 7 / 255, 0.1
        else:
            args[0].background_color = 255 / 255, 255 / 255, 255 / 255, 1
            self.id_labelMensajes.text = "Error en el campo de texto"

    def check_dinero(self, *args):
        self.id_labelMensajes.text = ""
        if utilidades.Comprobaciones.dinero(args[0].text):
            args[0].background_color = 7 / 255, 7 / 255, 7 / 255, 0.1
        else:
            args[0].background_color = 255 / 255, 255 / 255, 255 / 255, 1
            self.id_labelMensajes.text = "Error en el campo de texto"

    def cambiar_color(self, *args):
        args[0].background_color = 11 / 255, 69 / 255, 0 / 255, 0.7

    def necesitaCol(self, *args):
        if args[1] == "Si":
            Colaboradores().open()
        args[0].background_color = 11 / 255, 69 / 255, 0 / 255, 0.7

    def productosservs(self, *args):
        if args[1] != "Producto / Servicio":
            ProductosServicios().open()
        args[0].background_color = 11 / 255, 69 / 255, 0 / 255, 0.7

    def on_selection_departamentos(self, *args):
        self.id_ciudades.values = utilidades.IdeaNegocio.cargarCiudades(args[1])
        self.id_departamentos.background_color = 11 / 255, 69 / 255, 0 / 255, 0.7

    def comprobarTodo(self, *args):
        self.id_labelMensajes.text = ""
        if (
                self.id_emprendimiento.text == "" or self.id_sectorEmpresarial.text == "Sector Empresarial" or
                self.id_ciudades.text == "Ciudad" or self.id_estudios.text == "Estudios sobre el tema" or
                self.id_esAgropecuario.text == "¿Agropecuario?" or
                self.id_necesitaColaboradores.text == "Necesita colaboradores" or
                self.id_tiempoSemanal.text == "Tiempo semanal a dedicar" or
                self.id_porqueNo.text == "¿Por qué no empezaba?" or
                self.id_mesesQueLleva.text == "Meses que lleva el negocio" or self.id_ciiu.text == "CIIU" or
                self.id_comoSurge.text == "¿Cómo surge la idea?" or self.id_tieneExperiencia.text == "¿Experiencia?" or
                self.id_departamentos.text == "Departamento" or self.id_tiempoADedicar.text == "Tiempo a dedicar" or
                self.id_productoServicio.text == "Producto / Servicio" or self.id_portafolio.text == "" or
                self.id_inversionActivos.text == "" or self.id_porcentajeInversion.text == "% Inversión" or
                self.id_ventasPrimerMes.text == "" or self.id_inversionInicial.text == "" or
                self.id_invCapitalTrabajo.text == "" or self.id_ventasPrimerAno.text == "" or
                self.id_imagine.text == "" or self.lista_productos_servicios == ""):
            self.id_labelMensajes.text = "Formulario incompleto"
        if self.id_labelMensajes.text == "":
            if (utilidades.Comprobaciones.name(self.id_emprendimiento.text) and
                    utilidades.Comprobaciones.name(self.id_portafolio.text) and
                    utilidades.Comprobaciones.name(self.id_imagine.text) and
                    utilidades.Comprobaciones.dinero(self.id_inversionActivos.text) and
                    utilidades.Comprobaciones.dinero(self.id_ventasPrimerMes.text) and
                    utilidades.Comprobaciones.dinero(self.id_inversionInicial.text) and
                    utilidades.Comprobaciones.dinero(self.id_invCapitalTrabajo.text) and
                    utilidades.Comprobaciones.dinero(self.id_ventasPrimerAno.text)):
                corporacion.sm.current = "Panel"
            else:
                self.id_labelMensajes.text = "Error en algún campo de texto"

    def on_pre_leave(self, *args):
        proyecto = utilidades.InfoGeneral.identidadProyecto(self.informacion[0])
        utilidades.IdeaNegocio.ingresarInformacion(
            proyecto,
            self.beneficiario,
            self.id_emprendimiento.text,
            self.id_sectorEmpresarial.text,
            int(self.id_ciiu.text),
            self.id_departamentos.text,
            self.id_ciudades.text,
            self.id_comoSurge.text,
            self.id_tiempoADedicar.text,
            self.id_estudios.text,
            self.id_tieneExperiencia.text,
            self.id_productoServicio.text,
            self.lista_productos_servicios,
            self.id_esAgropecuario.text,
            self.id_portafolio.text,
            int(self.id_inversionActivos.text),
            int(self.id_inversionInicial.text),
            self.id_porcentajeInversion.text,
            int(self.id_invCapitalTrabajo.text),
            int(self.id_ventasPrimerMes.text),
            int(self.id_ventasPrimerAno.text),
            self.id_necesitaColaboradores.text,
            self.lista_colaboradores,
            self.id_tiempoSemanal.text,
            self.id_porqueNo.text,
            int(self.id_mesesQueLleva.text),
            self.id_imagine.text
        )


class UnidadNegocioScreen(Screen):
    # Costante
    informacion = None
    beneficiario = None

    # IDS
    id_unidad = ObjectProperty()
    id_existe = ObjectProperty()
    id_cuantosSocios = ObjectProperty()
    id_ciiu = ObjectProperty()
    id_email = ObjectProperty()
    id_paginaWeb = ObjectProperty()
    id_sector = ObjectProperty()
    id_regCamara = ObjectProperty()
    id_conContrato = ObjectProperty()
    id_sinContrato = ObjectProperty()
    id_departamentos = ObjectProperty()
    id_ciudades = ObjectProperty()
    id_direccion = ObjectProperty()
    id_telFijo = ObjectProperty()
    id_celular = ObjectProperty()
    id_rotulo = ObjectProperty()
    id_indicador = ObjectProperty()
    id_celular2 = ObjectProperty()
    id_descripcionLabel = ObjectProperty()
    id_descripcion = ObjectProperty()
    id_portafolio = ObjectProperty()
    id_creacionLabel = ObjectProperty()
    id_creacion = ObjectProperty()
    id_nit = ObjectProperty()
    id_descripcionPasivosLabel = ObjectProperty()
    id_descripcionPasivos = ObjectProperty()
    id_labelMensajes = ObjectProperty()
    id_botonIngresar = ObjectProperty()

    def on_pre_enter(self):
        # Restricciones
        self.id_telFijo.input_type = 'number'
        self.id_celular.input_type = 'number'
        self.id_celular2.input_type = 'number'

        # Inicializando Caracteres
        self.id_unidad.text = ""
        self.id_existe.text = "Si existe seleccione"
        self.id_cuantosSocios.text = "¿Cuantos socios?"
        self.id_ciiu.text = "CIIU"
        self.id_email.text = ""
        self.id_paginaWeb.text = ""
        self.id_sector.text = "Sector empresarial"
        self.id_regCamara.text = "Reg. Cámara comercio"
        self.id_conContrato.text = "Colab. con contrato"
        self.id_sinContrato.text = "Colab. sin contrato"
        self.id_departamentos.text = "Departamento"
        self.id_ciudades.text = "Ciudad"
        self.id_direccion.text = ""
        self.id_telFijo.text = ""
        self.id_celular.text = ""
        self.id_rotulo.text = "Rótulo"
        self.id_indicador.text = "Indicador"
        self.id_celular2.text = ""
        self.id_descripcionLabel.text = "Descripción"
        self.id_descripcion.text = ""
        self.id_portafolio.text = ""
        self.id_creacionLabel.text = "Creación"
        self.id_creacion.text = ""
        self.id_nit.text = ""
        self.id_descripcionPasivosLabel.text = "Descripción pasivos"
        self.id_descripcionPasivos.text = ""
        self.id_botonIngresar.text = "Ingresar"

        self.id_celular.hint_text = "Celular 2"
        self.id_celular2.hint_text = "Celular"
        self.id_telFijo.hint_text = "Tel. Fijo"
        self.id_email.hint_text = "Email"
        self.id_paginaWeb.hint_text = "Página Web"

        # Cargando los valores de las listas deplegables
        info = utilidades.UnidadNegocio.cargarDatos()
        self.id_cuantosSocios.values = info[0]
        self.id_ciiu.values = info[7]
        self.id_sector.values = info[1]
        self.id_regCamara.values = info[2]
        self.id_conContrato.values = info[3]
        self.id_sinContrato.values = info[4]
        self.id_departamentos.values = info[8]
        self.id_rotulo.values = info[5]
        self.id_indicador.values = info[6]

        self.id_existe.values = ["No"]

        # Iniciar todos los spinners con el color desactivado
        self.id_cuantosSocios.background_color = 61 / 255, 119 / 255, 0 / 255, 0.7
        self.id_ciiu.background_color = 61 / 255, 119 / 255, 0 / 255, 0.7
        self.id_sector.background_color = 61 / 255, 119 / 255, 0 / 255, 0.7
        self.id_regCamara.background_color = 61 / 255, 119 / 255, 0 / 255, 0.7
        self.id_conContrato.background_color = 61 / 255, 119 / 255, 0 / 255, 0.7
        self.id_sinContrato.background_color = 61 / 255, 119 / 255, 0 / 255, 0.7
        self.id_departamentos.background_color = 61 / 255, 119 / 255, 0 / 255, 0.7
        self.id_rotulo.background_color = 61 / 255, 119 / 255, 0 / 255, 0.7
        self.id_indicador.background_color = 61 / 255, 119 / 255, 0 / 255, 0.7
        self.id_existe.background_color = 61 / 255, 119 / 255, 0 / 255, 0.7
        self.id_ciudades.background_color = 61 / 255, 119 / 255, 0 / 255, 0.7

        # Iniciar todos los Text Inputs con el color desactivado
        self.id_unidad.background_color = 255 / 255, 255 / 255, 255 / 255, 1
        self.id_email.background_color = 255 / 255, 255 / 255, 255 / 255, 1
        self.id_paginaWeb.background_color = 255 / 255, 255 / 255, 255 / 255, 1
        self.id_direccion.background_color = 255 / 255, 255 / 255, 255 / 255, 1
        self.id_telFijo.background_color = 255 / 255, 255 / 255, 255 / 255, 1
        self.id_celular.background_color = 255 / 255, 255 / 255, 255 / 255, 1
        self.id_celular2.background_color = 255 / 255, 255 / 255, 255 / 255, 1
        self.id_descripcion.background_color = 255 / 255, 255 / 255, 255 / 255, 1
        self.id_portafolio.background_color = 255 / 255, 255 / 255, 255 / 255, 1
        self.id_creacion.background_color = 255 / 255, 255 / 255, 255 / 255, 1
        self.id_nit.background_color = 255 / 255, 255 / 255, 255 / 255, 1
        self.id_descripcionPasivos.background_color = 255 / 255, 255 / 255, 255 / 255, 1

        # Estableciendo el enlace con los spinner cuya selección determina el valor de otros
        self.id_departamentos.bind(text=self.on_selection_departamentos)

        # Métodos que cambian el color del spinner cuando son seleccionados
        self.id_existe.bind(text=self.cambiar_color)
        self.id_cuantosSocios.bind(text=self.cambiar_color)
        self.id_ciiu.bind(text=self.cambiar_color)
        self.id_sector.bind(text=self.cambiar_color)
        self.id_regCamara.bind(text=self.cambiar_color)
        self.id_conContrato.bind(text=self.cambiar_color)
        self.id_sinContrato.bind(text=self.cambiar_color)
        self.id_rotulo.bind(text=self.cambiar_color)
        self.id_indicador.bind(text=self.cambiar_color)
        self.id_ciudades.bind(text=self.cambiar_color)

        # Método que verificará si el formulario fue totalmente diligenciado
        self.id_botonIngresar.bind(on_press=self.comprobarTodo)

        # Métodos de verificación individual de cada Text Input
        self.id_unidad.bind(on_text_validate=self.check_name)
        self.id_telFijo.bind(on_text_validate=self.check_fijo)
        self.id_celular.bind(on_text_validate=self.check_celular)
        self.id_celular2.bind(on_text_validate=self.check_celular)
        self.id_descripcion.bind(on_text_validate=self.check_name)
        self.id_portafolio.bind(on_text_validate=self.check_name)
        self.id_creacion.bind(on_text_validate=self.check_data)
        self.id_descripcionPasivos.bind(on_text_validate=self.check_name)

        self.id_email.bind(on_text_validate=self.check_input)
        self.id_paginaWeb.bind(on_text_validate=self.check_input)
        self.id_direccion.bind(on_text_validate=self.check_input)
        self.id_nit.bind(on_text_validate=self.check_input)

    def check_name(self, *args):
        self.id_labelMensajes.text = ""
        if utilidades.Comprobaciones.name(args[0].text):
            args[0].background_color = 7 / 255, 7 / 255, 7 / 255, 0.1
        else:
            args[0].background_color = 255 / 255, 255 / 255, 255 / 255, 1
            self.id_labelMensajes.text = "Error en el campo de texto"

    def check_data(self, *args):
        if utilidades.Comprobaciones.data(args[0].text):
            args[0].background_color = 7 / 255, 7 / 255, 7 / 255, 0.1
        else:
            args[0].background_color = 255 / 255, 255 / 255, 255 / 255, 1
            self.id_labelMensajes.text = "Error en el campo de fecha"

    def check_fijo(self, *args):
        self.id_labelMensajes.text = ""
        if utilidades.Comprobaciones.fijo(args[0].text):
            args[0].background_color = 7 / 255, 7 / 255, 7 / 255, 0.1
        else:
            args[0].background_color = 255 / 255, 255 / 255, 255 / 255, 1
            self.id_labelMensajes.text = "Error en el teléfono fijo"

    def check_celular(self, *args):
        self.id_labelMensajes.text = ""
        if utilidades.Comprobaciones.celular(args[0].text):
            args[0].background_color = 7 / 255, 7 / 255, 7 / 255, 0.1
        else:
            args[0].background_color = 255 / 255, 255 / 255, 255 / 255, 1
            self.id_labelMensajes.text = "Error en el número celular"

    def check_input(self, *args):
        self.id_labelMensajes.text = ""
        if len(args[0].text.strip()) > 0:
            args[0].background_color = 7 / 255, 7 / 255, 7 / 255, 0.1
        else:
            self.id_labelMensajes.text = "No se permiten campos vacios"

    def cambiar_color(self, *args):
        args[0].background_color = 11 / 255, 69 / 255, 0 / 255, 0.7

    def on_selection_departamentos(self, *args):
        self.id_ciudades.values = utilidades.IdeaNegocio.cargarCiudades(args[1])
        self.id_departamentos.background_color = 11 / 255, 69 / 255, 0 / 255, 0.7

    def comprobarTodo(self, *args):
        self.id_labelMensajes.text = ""
        if (
                self.id_unidad.text == "" or
                self.id_existe.text == "Si existe seleccione" or
                self.id_cuantosSocios.text == "¿Cuantos socios?" or
                self.id_ciiu.text == "CIIU" or
                self.id_email.text == "" or
                self.id_paginaWeb.text == "" or
                self.id_sector.text == "Sector empresarial" or
                self.id_regCamara.text == "Reg. Cámara comercio" or
                self.id_conContrato.text == "Colab. con contrato" or
                self.id_sinContrato.text == "Colab. sin contrato" or
                self.id_departamentos.text == "Departamento" or
                self.id_ciudades.text == "Ciudad" or
                self.id_direccion.text == "" or
                self.id_telFijo.text == "" or
                self.id_celular.text == "" or
                self.id_rotulo.text == "Rótulo" or
                self.id_indicador.text == "Indicador" or
                self.id_celular2.text == "" or
                self.id_descripcion.text == "" or
                self.id_portafolio.text == "" or
                self.id_creacion.text == "" or
                self.id_nit.text == "" or
                self.id_descripcionPasivos.text == ""
        ):
            self.id_labelMensajes.text = "Formulario Incompleto"
        if self.id_labelMensajes.text == "":
            if (utilidades.Comprobaciones.name(self.id_unidad.text) and
                    utilidades.Comprobaciones.name(self.id_descripcion.text) and
                    utilidades.Comprobaciones.name(self.id_portafolio.text) and
                    utilidades.Comprobaciones.name(self.id_descripcionPasivos.text) and
                    utilidades.Comprobaciones.fijo(self.id_telFijo.text) and
                    utilidades.Comprobaciones.celular(self.id_celular.text) and
                    utilidades.Comprobaciones.celular(self.id_celular2.text) and
                    utilidades.Comprobaciones.data(self.id_creacion.text)):
                corporacion.sm.current = "Panel"
            else:
                self.id_labelMensajes.text = "Error en algunos campos de texto"

    def on_pre_leave(self, *args):
        proyecto = utilidades.InfoGeneral.identidadProyecto(self.informacion[0])
        utilidades.UnidadNegocio.ingresarInformacion(
            proyecto,
            self.beneficiario,
            self.id_unidad.text,
            self.id_departamentos.text,
            self.id_ciudades.text,
            int(self.id_cuantosSocios.text),
            self.id_direccion.text,
            int(self.id_ciiu.text),
            int(self.id_indicador.text),
            int(self.id_telFijo.text),
            self.id_email.text,
            self.id_paginaWeb.text,
            self.id_descripcion.text,
            self.id_portafolio.text,
            self.id_creacion.text,
            self.id_nit.text,
            self.id_descripcionPasivos.text,
            self.id_regCamara.text,
            int(self.id_conContrato.text),
            int(self.id_sinContrato.text),
            int(self.id_celular.text),
            int(self.id_celular2.text)
        )


class CaracterizacionAmpliadaScreen(Screen):
    # Costantes
    informacion = None
    listado_hijos = False
    listado_cargo = False
    beneficiario = None

    # IDS
    id_title = ObjectProperty()
    id_formacionSuperior = ObjectProperty()
    id_nivelEscolaridad = ObjectProperty()
    id_vinculacionLaboral = ObjectProperty()
    id_independiente = ObjectProperty()
    id_cabezaFamilia = ObjectProperty()
    id_integrantesHogar = ObjectProperty()
    id_regimenSalud = ObjectProperty()
    id_estadoCivil = ObjectProperty()
    id_tipoContrato = ObjectProperty()
    id_rut = ObjectProperty()
    id_numeroHijos = ObjectProperty()
    id_aCargo = ObjectProperty()
    id_cubreFamilia = ObjectProperty()
    id_promedioIngresosContrato = ObjectProperty()
    id_promedioIngresosActividad = ObjectProperty()
    id_informacionHijos = ObjectProperty()
    id_informacionPersonasCargo = ObjectProperty()
    id_pension = ObjectProperty()
    id_arl = ObjectProperty()
    id_factoresQueImpiden = ObjectProperty()
    id_observaciones = ObjectProperty()
    id_labelMensajes = ObjectProperty()
    id_botonIngresar = ObjectProperty()

    def on_pre_enter(self, *args):
        # Inicializando Caracteres
        self.id_title.text = "Caracterización Ampliada"
        self.id_formacionSuperior.text = ''
        self.id_nivelEscolaridad.text = 'Nivel de escolaridad'
        self.id_vinculacionLaboral.text = '¿Tiene vinculación laboral con contrato?'
        self.id_independiente.text = '¿Independiente?'
        self.id_cabezaFamilia.text = '¿Es cabeza de familia?'
        self.id_integrantesHogar.text = 'Número de integrantes en el hogar'
        self.id_regimenSalud.text = 'Régimen de salud'
        self.id_estadoCivil.text = 'Estado Civil'
        self.id_tipoContrato.text = 'Tipo de contrato'
        self.id_rut.text = '¿Tiene RUT?'
        self.id_numeroHijos.text = '¿Número de hijos?'
        self.id_aCargo.text = '¿Cuántas personas tiene a cargo?'
        self.id_cubreFamilia.text = '¿Cubre su familia?'
        self.id_promedioIngresosContrato.text = 'Promedio de ingresos por contrato'
        self.id_promedioIngresosActividad.text = 'Promedio de ingresos en esta actividad'
        self.id_informacionHijos.text = 'Información de hijos'
        self.id_informacionPersonasCargo.text = 'Info. personas a cargo'
        self.id_pension.text = 'Pensión'
        self.id_arl.text = 'ARL'
        self.id_factoresQueImpiden.text = ''
        self.id_observaciones.text = ''
        self.id_labelMensajes.text = ''
        self.id_botonIngresar.text = 'Ingresar'

        self.id_formacionSuperior.hint_text = "Formación superior o cursos complementarios"
        self.id_factoresQueImpiden.hint_text = "Factores que le impiden participar en este proyecto"
        self.id_observaciones.hint_text = "Observaciones / aclaraciones"

        # Cargando los valores de las listas deplegables
        datos = utilidades.CarAmpliada.cargarDatos()
        self.id_nivelEscolaridad.values = datos[0]
        self.id_vinculacionLaboral.values = datos[1]
        self.id_independiente.values = datos[2]
        self.id_cabezaFamilia.values = datos[3]
        self.id_integrantesHogar.values = datos[4]
        self.id_regimenSalud.values = datos[5]
        self.id_estadoCivil.values = datos[6]
        self.id_tipoContrato.values = datos[7]
        self.id_rut.values = datos[8]
        self.id_numeroHijos.values = datos[9]
        self.id_aCargo.values = datos[10]
        self.id_cubreFamilia.values = datos[11]
        self.id_promedioIngresosContrato.values = datos[12]
        self.id_promedioIngresosActividad.values = datos[13]
        self.id_pension.values = datos[14]
        self.id_arl.values = datos[15]

        # Iniciar todos los spinners con el color desactivado
        self.id_nivelEscolaridad.background_color = 61 / 255, 119 / 255, 0 / 255, 0.7
        self.id_vinculacionLaboral.background_color = 61 / 255, 119 / 255, 0 / 255, 0.7
        self.id_independiente.background_color = 61 / 255, 119 / 255, 0 / 255, 0.7
        self.id_cabezaFamilia.background_color = 61 / 255, 119 / 255, 0 / 255, 0.7
        self.id_integrantesHogar.background_color = 61 / 255, 119 / 255, 0 / 255, 0.7
        self.id_regimenSalud.background_color = 61 / 255, 119 / 255, 0 / 255, 0.7
        self.id_estadoCivil.background_color = 61 / 255, 119 / 255, 0 / 255, 0.7
        self.id_tipoContrato.background_color = 61 / 255, 119 / 255, 0 / 255, 0.7
        self.id_rut.background_color = 61 / 255, 119 / 255, 0 / 255, 0.7
        self.id_numeroHijos.background_color = 61 / 255, 119 / 255, 0 / 255, 0.7
        self.id_aCargo.background_color = 61 / 255, 119 / 255, 0 / 255, 0.7
        self.id_cubreFamilia.background_color = 61 / 255, 119 / 255, 0 / 255, 0.7
        self.id_promedioIngresosContrato.background_color = 61 / 255, 119 / 255, 0 / 255, 0.7
        self.id_promedioIngresosActividad.background_color = 61 / 255, 119 / 255, 0 / 255, 0.7
        self.id_pension.background_color = 61 / 255, 119 / 255, 0 / 255, 0.7
        self.id_arl.background_color = 61 / 255, 119 / 255, 0 / 255, 0.7

        # Iniciar todos los Text Inputs con el color desactivado
        self.id_formacionSuperior.background_color = 255 / 255, 255 / 255, 255 / 255, 1
        self.id_factoresQueImpiden.background_color = 255 / 255, 255 / 255, 255 / 255, 1
        self.id_observaciones.background_color = 255 / 255, 255 / 255, 255 / 255, 1

        # Métodos que cambian el color del spinner cuando son seleccionados
        self.id_nivelEscolaridad.bind(text=self.cambiar_color)
        self.id_vinculacionLaboral.bind(text=self.cambiar_color)
        self.id_independiente.bind(text=self.cambiar_color)
        self.id_cabezaFamilia.bind(text=self.cambiar_color)
        self.id_integrantesHogar.bind(text=self.cambiar_color)
        self.id_regimenSalud.bind(text=self.cambiar_color)
        self.id_estadoCivil.bind(text=self.cambiar_color)
        self.id_tipoContrato.bind(text=self.cambiar_color)
        self.id_rut.bind(text=self.cambiar_color)
        self.id_numeroHijos.bind(text=self.cambiar_color)
        self.id_aCargo.bind(text=self.cambiar_color)
        self.id_cubreFamilia.bind(text=self.cambiar_color)
        self.id_promedioIngresosContrato.bind(text=self.cambiar_color)
        self.id_promedioIngresosActividad.bind(text=self.cambiar_color)
        self.id_pension.bind(text=self.cambiar_color)
        self.id_arl.bind(text=self.cambiar_color)

        self.id_formacionSuperior.bind(on_text_validate=self.check_name)
        self.id_factoresQueImpiden.bind(on_text_validate=self.check_name)
        self.id_observaciones.bind(on_text_validate=self.check_name)

        self.id_informacionHijos.bind(on_release=self.infoHijos)
        self.id_informacionPersonasCargo.bind(on_release=self.infoACargo)

        self.id_botonIngresar.bind(on_release=self.verficarTodo)

    def verficarTodo(self, *args):
        self.id_labelMensajes.text = ""
        if (
                self.id_formacionSuperior.text == '' or
                self.id_nivelEscolaridad.text == 'Nivel de escolaridad' or
                self.id_vinculacionLaboral.text == '¿Tiene vinculación laboral con contrato?' or
                self.id_independiente.text == '¿Independiente?' or
                self.id_cabezaFamilia.text == '¿Es cabeza de familia?' or
                self.id_integrantesHogar.text == 'Número de integrantes en el hogar' or
                self.id_regimenSalud.text == 'Régimen de salud' or
                self.id_estadoCivil.text == 'Estado Civil' or
                self.id_tipoContrato.text == 'Tipo de contrato' or
                self.id_rut.text == '¿Tiene RUT?' or
                self.id_numeroHijos.text == '¿Número de hijos?' or
                self.id_aCargo.text == '¿Cuántas personas tiene a cargo?' or
                self.id_cubreFamilia.text == '¿Cubre su familia?' or
                self.id_promedioIngresosContrato.text == 'Promedio de ingresos por contrato' or
                self.id_promedioIngresosActividad.text == 'Promedio de ingresos en esta actividad' or
                self.id_pension.text == 'Pensión' or
                self.id_arl.text == 'ARL' or
                self.id_factoresQueImpiden.text == '' or
                self.id_observaciones.text == '' or
                self.listado_hijos == False or
                self.listado_cargo == False
        ):
            self.id_labelMensajes.text = "Formulario Incompleto"
        else:
            corporacion.sm.current = "Panel"

    def infoHijos(self, *args):
        self.id_labelMensajes.text = ""
        if self.id_numeroHijos.text == '¿Número de hijos?':
            self.id_labelMensajes.text = "Seleccione primero un número de hijos"
        else:
            if self.id_numeroHijos.text != "0":
                InformacionHijos(int(self.id_numeroHijos.text)).open()
            else:
                self.listado_hijos = True

    def infoACargo(self, *args):
        self.id_labelMensajes.text = ""
        if self.id_aCargo.text == '¿Cuántas personas tiene a cargo?':
            self.id_labelMensajes.text = "Seleccione número de personas a cargo"
        else:
            if self.id_aCargo.text != "0":
                InformacionPersonasACargo(int(self.id_aCargo.text)).open()
            else:
                self.listado_cargo = True

    def check_name(self, *args):
        self.id_labelMensajes.text = ""
        if utilidades.Comprobaciones.name(args[0].text):
            args[0].background_color = 7 / 255, 7 / 255, 7 / 255, 0.1
        else:
            args[0].background_color = 255 / 255, 255 / 255, 255 / 255, 1
            self.id_labelMensajes.text = "Error en el campo de texto"

    def cambiar_color(self, *args):
        args[0].background_color = 11 / 255, 69 / 255, 0 / 255, 0.7

    def on_pre_leave(self, *args):
        proyecto = utilidades.InfoGeneral.identidadProyecto(self.informacion[0])
        operario = utilidades.CarAmpliada.buscarOperario(self.informacion[1])
        utilidades.CarAmpliada.subirDatos(
            proyecto,
            operario,
            self.beneficiario,
            self.id_formacionSuperior.text,
            self.id_nivelEscolaridad.text,
            self.id_vinculacionLaboral.text,
            self.id_independiente.text,
            self.id_cabezaFamilia.text,
            int(self.id_integrantesHogar.text),
            self.id_regimenSalud.text,
            self.id_estadoCivil.text,
            self.id_tipoContrato.text,
            self.id_rut.text,
            int(self.id_numeroHijos.text),
            int(self.id_aCargo.text),
            self.id_cubreFamilia.text,
            self.id_promedioIngresosContrato.text,
            self.id_promedioIngresosActividad.text,
            self.id_pension.text,
            self.id_arl.text,
            self.id_factoresQueImpiden.text,
            self.id_observaciones.text
        )


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
        # TODO Asignación del proyecto y operario que lo está realizando

        PanelScreen.informacion = args[1], self.usuario
        InformacionGeneralScreen.informacion = args[1], self.usuario
        IdeaNegocioScreen.informacion = args[1], self.usuario
        UnidadNegocioScreen.informacion = args[1], self.usuario
        CaracterizacionAmpliadaScreen.informacion = args[1], self.usuario

        corporacion.sm.current = "Panel"
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
        if utilidades.Comprobaciones.password(self.id_beneficiario.text):
            if utilidades.Panel.buscarBeneficiario(self.id_beneficiario.text, self.string) == "No existe":
                # TODO Ingreso del documento de identidad del beneficiario
                InformacionGeneralScreen.beneficiario = self.id_beneficiario.text
                DiagnosticoPerfilProductivoScreen.beneficiario = self.id_beneficiario.text
                IdeaNegocioScreen.beneficiario = self.id_beneficiario.text
                UnidadNegocioScreen.beneficiario = self.id_beneficiario.text
                corporacion.sm.current = "InformacionGeneral"
                self.dismiss()

            elif utilidades.Panel.buscarBeneficiario(self.id_beneficiario.text, self.string) == "Ya tiene C. Básica":

                if utilidades.Panel.comprobarEstado(self.id_beneficiario.text, self.string.split()[-1]) == 1:
                    UsuarioYaExisteEnEsteProyecto(self.id_beneficiario.text, True, False).open()
                    self.dismiss()

                else:
                    UsuarioYaExisteEnEsteProyecto(self.id_beneficiario.text, False, True).open()
                    self.dismiss()
            else:
                proyectos = utilidades.Panel.buscarBeneficiario(self.id_beneficiario.text, self.string).split()
                BeneficiarioProyecto(self.id_beneficiario.text, proyectos, self.string).open()
                self.dismiss()
        else:
            UsuarioYaExisteEnEsteProyecto(self.id_beneficiario.text, False, False).open()
            self.dismiss()


# Generado en la ventana PANEL GENERAL
class BeneficiarioProyecto(Popup):
    id_proyectos = ObjectProperty()

    def __init__(self, *args, **kwargs):
        super().__init__(**kwargs)
        self.beneficiario = args[0]
        self.proyectos = args[1]
        self.proyectos.insert(0, "Emprendedor")
        self.proyectos.insert(0, "Microempresario")
        self.string = args[2].split()[-1]

    def on_open(self):
        self.title = f"Seleccione el proyecto del cual desea copiar la C. Básica del benficiario {self.beneficiario}"
        self.id_proyectos.values = self.proyectos
        self.id_proyectos.bind(text=self.on_selection)

    def on_selection(self, *args):
        if not args[1] == "Emprendedor" or args[1] == "Microempresario":
            utilidades.Panel.copiarCBasica(self.beneficiario, self.string, args[1])
            self.dismiss()
        else:
            InformacionGeneralScreen.beneficiario = self.beneficiario
            DiagnosticoPerfilProductivoScreen.beneficiario = self.beneficiario
            IdeaNegocioScreen.beneficiario = self.beneficiario
            UnidadNegocioScreen.beneficiario = self.beneficiario

            if args[1] == "Emprendedor":
                corporacion.sm.current = "IdeaNegocio"
            else:
                corporacion.sm.current = "UnidadNegocio"
            self.dismiss()


# Generado en la ventana PANEL GENERAL
class InactivarBeneficiario(Popup):
    id_beneficiarios = ObjectProperty()

    def __init__(self, *args, **kwargs):
        super().__init__(**kwargs)
        self.proyecto = args[0]

    def on_open(self):
        self.title = f"Seleccione el beneficiario a inactivar. ¡Cuidado! Esta acción no puede ser anulada."
        self.id_beneficiarios.values = utilidades.Panel.lista_beneficiarios(self.proyecto)
        self.id_beneficiarios.bind(text=self.on_selection)

    def on_selection(self, *args):
        utilidades.Panel.inactivar_beneficiario(args[1], self.proyecto)
        self.dismiss()


# Generado en la ventana PANEL GENERAL
class UsuarioYaExisteEnEsteProyecto(Popup):
    id_botonaceptar = ObjectProperty()

    def __init__(self, *args, **kwargs):
        super().__init__(**kwargs)
        self.beneficiario = args[0]
        self.indicacion = args[1]
        self.estado = args[2]

    def on_open(self):
        if self.estado:
            self.title = f"{self.beneficiario} está inactivado en este proyecto. Contacte la central para cambiarlo."
        else:
            if self.indicacion:
                self.title = f"Beneficiario {self.beneficiario} ya tiene Caracterización básica en este proyecto"
            else:
                self.title = f"{self.beneficiario} no es un formato de documento permitido"
        self.id_botonaceptar.bind(on_release=self.on_selection)

    def on_selection(self, *args):
        self.dismiss()


# Generado en la ventana PANEL GENERAL
class YatieneCAmpliada(Popup):
    id_botonaceptar = ObjectProperty()

    def __init__(self, *args, **kwargs):
        super().__init__(**kwargs)
        self.beneficiario = args[0]

    def on_open(self):
        self.title = f"Al Beneficiario {self.beneficiario} ya se le realizó la caracterización ampliada"
        self.id_botonaceptar.bind(on_release=self.on_selection)

    def on_selection(self, *args):
        self.dismiss()


# Generado en la ventana INFORMACIÓN GENERAL
class ConfirmacionInfoGeneral(Popup):
    # IDS
    id_botonaceptar = ObjectProperty()

    def on_open(self):
        self.title = "Confirme que la información es correcta antes de continuar"
        self.id_botonaceptar.bind(on_release=self.on_selection)

    def on_selection(self, *args):
        corporacion.sm.current = "DiagnosticoPerfilProductivo"
        self.dismiss()


# Generado en la ventana IDEA DE NEGOCIO
class ProductosServicios(Popup):
    id_porductservs = ObjectProperty()

    def on_open(self):
        self.title = "Ingrese los productos o servicios de su idea separados por comas"
        self.id_porductservs.bind(on_text_validate=self.on_selection)

    def on_selection(self, *args):
        IdeaNegocioScreen.lista_productos_servicios = args[0].text
        self.dismiss()


# Generado en la ventana IDEA DE NEGOCIO
class Colaboradores(Popup):
    id_listacolaboradores = ObjectProperty()

    def on_open(self):
        self.title = "Ingrese la lista de sus colaboradores separada por comas"
        self.id_listacolaboradores.bind(on_text_validate=self.on_selection)

    def on_selection(self, *args):
        IdeaNegocioScreen.lista_colaboradores = args[0].text
        self.dismiss()


class CaracterizaAmpliada(Popup):
    id_beneficiarios = ObjectProperty()

    def __init__(self, *args, **kwargs):
        super().__init__(**kwargs)
        self.proyecto = args[0]

    def on_open(self):
        self.title = f"Seleccione el beneficiario para realizar Caracterización Ampliada"
        self.id_beneficiarios.values = utilidades.Panel.lista_beneficiarios(self.proyecto)
        self.id_beneficiarios.bind(text=self.on_selection)

    def on_selection(self, *args):
        if utilidades.Panel.comprobarEstado(args[1], self.proyecto) == 1:
            if utilidades.CarAmpliada.comprobarBeneficiario(args[1], self.proyecto):
                YatieneCAmpliada(args[1]).open()
                self.dismiss()
            else:
                CaracterizacionAmpliadaScreen.beneficiario = args[1]
                corporacion.sm.current = "CaracterizacionAmpliada"
            self.dismiss()
        else:
            UsuarioYaExisteEnEsteProyecto(args[1], False, True).open()
            self.dismiss()


class InformacionHijos(Popup):
    id_container_grid = ObjectProperty()
    id_botonAceptar = ObjectProperty()

    def __init__(self, *args, **kwargs):
        super().__init__(**kwargs)
        self.cantidad = args[0]

    def on_open(self):
        self.id_botonAceptar.bind(on_release=self.accionAceptar)
        self.id_container_grid.rows = int(self.cantidad) + 1
        self.title = "Información sobre hijos e hijas"
        self.id_container_grid.bind(minimum_height=self.id_container_grid.setter('height'))

        lab_1 = Label(text='Hijo', halign="center", valign="middle", size_hint=(None, None),
                      size=(40, 40), color=(0, 0, 0, 0.85), font_size=20, font_name="montserrat",
                      text_size=(40, 40))
        lab_2 = Label(text='Género', halign="center", valign="middle", size_hint=(None, None),
                      size=(318, 40), color=(0, 0, 0, 0.85), font_size=20, font_name="montserrat",
                      text_size=(318, 40))
        lab_3 = Label(text='Mayor de edad', halign="center", valign="middle", size_hint=(None, None),
                      size=(318, 40), color=(0, 0, 0, 0.85), font_size=20, font_name="montserrat",
                      text_size=(318, 40))
        lab_4 = Label(text='Cond. Discapacidad', halign="center", valign="middle", size_hint=(None, None),
                      size=(318, 40), color=(0, 0, 0, 0.85), font_size=20, font_name="montserrat",
                      text_size=(318, 40))

        self.id_container_grid.add_widget(lab_1)
        self.id_container_grid.add_widget(lab_2)
        self.id_container_grid.add_widget(lab_3)
        self.id_container_grid.add_widget(lab_4)

        for idx in range(int(self.cantidad)):
            lab = Label(text=str(idx + 1), halign="center", valign="middle", size_hint=(None, None),
                        size=(77, 40), color=(0, 0, 0, 0.85), font_size=20, font_name="montserrat",
                        text_size=(77, 40), id=f'{idx + 1}')
            spin_gen = SpinnerScroll(text='Género', id=f'genero_{idx}', values=["Masculino", "Femenino",
                                                                                "Transgenerista", " No informa"])
            spin_mayor = SpinnerScroll(text='Mayoría', id=f'mayoria_{idx}', values=["Si", "No"])
            spin_disc = SpinnerScroll(text='Discapacidad', id=f'discapacidad_{idx}', values=["Física", "Cognitiva",
                                                                                             "Sensorial", "Intelectual",
                                                                                             "Psicosocial", "Múltiple",
                                                                                             "Ninguna", "ND"])

            self.id_container_grid.add_widget(lab)
            self.id_container_grid.add_widget(spin_gen)
            self.id_container_grid.add_widget(spin_mayor)
            self.id_container_grid.add_widget(spin_disc)

    def accionAceptar(self, *args):
        res = []
        for idx, childs in enumerate(self.id_container_grid.children):
            if idx < len(self.id_container_grid.children) - 4:
                res.append(childs.text)
        res = res[::-1]
        if 'Género' in res or 'Mayoría' in res or 'Discapacidad' in res:
            pass
        else:
            CaracterizacionAmpliadaScreen.listado_hijos = True
            self.dismiss()


class InformacionPersonasACargo(Popup):
    id_container_grid = ObjectProperty()
    id_botonAceptar = ObjectProperty()

    def __init__(self, *args, **kwargs):
        super().__init__(**kwargs)
        self.cantidad = args[0]

    def on_open(self):
        self.id_botonAceptar.bind(on_release=self.accionAceptar)
        self.id_container_grid.rows = int(self.cantidad) + 1
        self.title = "Información sobre las personas que tiene a cargo"
        self.id_container_grid.bind(minimum_height=self.id_container_grid.setter('height'))

        lab_1 = Label(text='#', halign="center", valign="middle", size_hint=(None, None),
                      size=(40, 40), color=(0, 0, 0, 0.85), font_size=20, font_name="montserrat",
                      text_size=(40, 40))
        lab_2 = Label(text='Género', halign="center", valign="middle", size_hint=(None, None),
                      size=(318, 40), color=(0, 0, 0, 0.85), font_size=20, font_name="montserrat",
                      text_size=(318, 40))
        lab_3 = Label(text='Mayor de edad', halign="center", valign="middle", size_hint=(None, None),
                      size=(318, 40), color=(0, 0, 0, 0.85), font_size=20, font_name="montserrat",
                      text_size=(318, 40))
        lab_4 = Label(text='Cond. Discapacidad', halign="center", valign="middle", size_hint=(None, None),
                      size=(318, 40), color=(0, 0, 0, 0.85), font_size=20, font_name="montserrat",
                      text_size=(318, 40))

        self.id_container_grid.add_widget(lab_1)
        self.id_container_grid.add_widget(lab_2)
        self.id_container_grid.add_widget(lab_3)
        self.id_container_grid.add_widget(lab_4)

        for idx in range(int(self.cantidad)):
            lab = Label(text=str(idx + 1), halign="center", valign="middle", size_hint=(None, None),
                        size=(77, 40), color=(0, 0, 0, 0.85), font_size=20, font_name="montserrat",
                        text_size=(77, 40), id=f'{idx + 1}')
            spin_gen = SpinnerScroll(text='Género', id=f'genero_{idx}', values=["Masculino", "Femenino",
                                                                                "Transgenerista", " No informa"])
            spin_mayor = SpinnerScroll(text='Mayoría', id=f'mayoria_{idx}', values=["Si", "No"])
            spin_disc = SpinnerScroll(text='Discapacidad', id=f'discapacidad_{idx}', values=["Física", "Cognitiva",
                                                                                             "Sensorial", "Intelectual",
                                                                                             "Psicosocial", "Múltiple",
                                                                                             "Ninguna", "ND"])

            self.id_container_grid.add_widget(lab)
            self.id_container_grid.add_widget(spin_gen)
            self.id_container_grid.add_widget(spin_mayor)
            self.id_container_grid.add_widget(spin_disc)

    def accionAceptar(self, *args):
        res = []
        for idx, childs in enumerate(self.id_container_grid.children):
            if idx < len(self.id_container_grid.children) - 4:
                res.append(childs.text)
        res = res[::-1]
        if 'Género' in res or 'Mayoría' in res or 'Discapacidad' in res:
            pass
        else:
            CaracterizacionAmpliadaScreen.listado_cargo = True
            self.dismiss()


# ----------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------

class SpinnerScroll(Spinner):
    def __init__(self, *args, **kwargs):
        super().__init__(**kwargs)
        self.background_normal = "images/dropdown_scroll.png"
        self.background_color = 61 / 255, 119 / 255, 0 / 255, 0.7
        self.halign = "center"
        self.valign = "middle"
        self.size_hint = (None, None)
        self.size = (318, 40)
        self.color = (1, 1, 1, 1)
        self.font_size = 20
        self.font_name = "montserrat"
        self.text_size = (318, 40)
        self.diligenciado = False
        self.id = 'Spinner'

    def on_text(self, *args):
        self.background_color = 11 / 255, 69 / 255, 0 / 255, 0.7
        self.diligenciado = True


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
        Builder.load_file("windows/DiagnosticoPerfilProductivo.kv")
        Builder.load_file("windows/IdeaNegocio.kv")
        Builder.load_file("windows/UnidadNegocio.kv")
        Builder.load_file("windows/CaracterizacionAmpliada.kv")
        Builder.load_file("windows/templates.kv")

        # Agregando ventanas al gestor de ventanas
        self.sm.add_widget(LoginScreen(name="Login"))
        self.sm.add_widget(PanelScreen(name="Panel"))
        self.sm.add_widget(InformacionGeneralScreen(name="InformacionGeneral"))
        self.sm.add_widget(DiagnosticoPerfilProductivoScreen(name="DiagnosticoPerfilProductivo"))
        self.sm.add_widget(IdeaNegocioScreen(name="IdeaNegocio"))
        self.sm.add_widget(UnidadNegocioScreen(name="UnidadNegocio"))
        self.sm.add_widget(CaracterizacionAmpliadaScreen(name="CaracterizacionAmpliada"))
        self.sm.current = "Login"
        return self.sm


if __name__ == '__main__':
    Window.size = (1280, 800)
    Window.left = 45
    Window.top = -25
    Window.clearcolor = [1, 1, 1, 1]
    corporacion = MyApp()
    corporacion.run()
