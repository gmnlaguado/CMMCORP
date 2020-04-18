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
    # Costantes
    informacion = None
    beneficiario = None

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
    beneficiario = None
    tipo_beneficiario = ""
    creacion = False

    id_container_grid = ObjectProperty()
    id_labelMensajes = ObjectProperty()
    id_botonIngresar = ObjectProperty()

    def on_pre_enter(self):
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
    informacion = None
    beneficiario = None
    lista_productos_servicios = ""
    lista_colaboradores = ""

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
        self.id_inversionActivos.input_type = 'number'
        self.id_ventasPrimerMes.input_type = 'number'
        self.id_inversionInicial.input_type = 'number'
        self.id_invCapitalTrabajo.input_type = 'number'
        self.id_ventasPrimerAno.input_type = 'number'

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

        self.id_departamentos.bind(text=self.on_selection_departamentos)

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

        self.id_botonIngresar.bind(on_press=self.comprobarTodo)

    def cambiar_color(self, *args):
        args[0].background_color = 11 / 255, 69 / 255, 0 / 255, 0.7

    def necesitaCol(self, *args):
        if args[1] == "Si":
            Colaboradores().open()
        args[0].background_color = 11 / 255, 69 / 255, 0 / 255, 0.7

    def productosservs(self, *args):
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
            corporacion.sm.current = "Panel"

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
    informacion = None
    beneficiario = None

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
        self.id_telFijo.input_type = 'number'
        self.id_celular.input_type = 'number'
        self.id_celular2.input_type = 'number'

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

        self.id_departamentos.bind(text=self.on_selection_departamentos)

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

        self.id_botonIngresar.bind(on_press=self.comprobarTodo)

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
            corporacion.sm.current = "Panel"

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

        # TODO Asignación del proyecto y operario que lo está realizando

        PanelScreen.informacion = args[1], self.usuario
        InformacionGeneralScreen.informacion = args[1], self.usuario
        IdeaNegocioScreen.informacion = args[1], self.usuario
        UnidadNegocioScreen.informacion = args[1], self.usuario
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
            # TODO Ingreso del documento de identidad del beneficiario

            InformacionGeneralScreen.beneficiario = self.id_beneficiario.text
            DiagnosticoPerfilProductivoScreen.beneficiario = self.id_beneficiario.text
            IdeaNegocioScreen.beneficiario = self.id_beneficiario.text
            UnidadNegocioScreen.beneficiario = self.id_beneficiario.text
            corporacion.sm.current = "InformacionGeneral"

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
        Builder.load_file("windows/DiagnosticoPerfilProductivo.kv")
        Builder.load_file("windows/IdeaNegocio.kv")
        Builder.load_file("windows/UnidadNegocio.kv")

        # Agregando ventanas al gestor de ventanas
        self.sm.add_widget(LoginScreen(name="Login"))
        self.sm.add_widget(PanelScreen(name="Panel"))
        self.sm.add_widget(InformacionGeneralScreen(name="InformacionGeneral"))
        self.sm.add_widget(DiagnosticoPerfilProductivoScreen(name="DiagnosticoPerfilProductivo"))
        self.sm.add_widget(IdeaNegocioScreen(name="IdeaNegocio"))
        self.sm.add_widget(UnidadNegocioScreen(name="UnidadNegocio"))
        self.sm.current = "Login"
        return self.sm


if __name__ == '__main__':
    Window.size = (1280, 800)
    Window.left = 45
    Window.top = -25
    Window.clearcolor = [1, 1, 1, 1]
    corporacion = MyApp()
    corporacion.run()
