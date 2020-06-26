# coding=utf-8
from kivy.uix.screenmanager import Screen
from kivy.properties import ObjectProperty
from declarations import querys, class_declaration, upload_process
from windows import PlanDeImplementacion, InformacionGeneral, DiagnosticoPerfilProductivo, UnidadDeNegocio, \
    IdeaDeNegocio, CaracterizacionAmpliada, Monitoreo, PlanDeFormacion, DiagnosticoEmpresarial, ActividadDeFormacion, ActividadDeImplementacion


class PanelScreen(Screen):
    operator = None
    project = None

    static_titulo = ObjectProperty()
    id_proyecto = ObjectProperty()
    id_payee = ObjectProperty()
    id_newPayee = ObjectProperty()
    id_monitor = ObjectProperty()
    id_trainingPlan = ObjectProperty()
    id_query = ObjectProperty()
    id_inactivate = ObjectProperty()
    id_extendedChar = ObjectProperty()
    id_implementationPlan = ObjectProperty()
    id_followUpPlan = ObjectProperty()
    id_loadData = ObjectProperty()
    id_reload = ObjectProperty()

    def __init__(self, *args, **kwargs):
        super().__init__(**kwargs)
        self.static_titulo.text = "Panel General"
        self.id_newPayee.text = "Nuevo Beneficiario"
        self.id_monitor.text = "Monitoreo"
        self.id_trainingPlan.text = "Plan Formación"
        self.id_query.text = "Consultar"
        self.id_inactivate.text = "Inactivar"
        self.id_extendedChar.text = "C. Ampliada"
        self.id_implementationPlan.text = "Plan Implementación"
        self.id_followUpPlan.text = "Plan Seguimiento"
        self.id_loadData.text = "Cargar Datos"
        self.id_reload.text = "Actualizar"

        self.id_newPayee.bind(on_release=self.newPayee)
        self.id_loadData.bind(on_release=self.loadInformation)

        self.id_extendedChar.bind(on_release=self.extendedChar)
        self.id_monitor.bind(on_release=self.monitor)
        self.id_implementationPlan.bind(on_release=self.implementationPlan)
        self.id_trainingPlan.bind(on_release=self.trainingPlan)
        self.id_followUpPlan.bind(on_release=self.followUpPlan)
        self.id_query.bind(on_release=self.query)
        self.id_inactivate.bind(on_release=self.inactivate)
        self.id_reload.bind(on_release=self.reload)

    def extendedChar(self, *args):
        CaracterizacionAmpliadaButton(self.operator, self.project).open()

    def monitor(self, *args):
        MonitoreoButton(self.operator, self.project).open()

    def implementationPlan(self, *args):
        PlanDeImplementacionButton(self.operator, self.project).open()

    def trainingPlan(self, *args):
        PlanDeFormacionButton(self.operator, self.project).open()

    def followUpPlan(self, *args):
        PlanDeSeguimientoButton(self.operator, self.project).open()

    def query(self, *args):
        ConsultarButton(self.operator, self.project).open()

    def inactivate(self, *args):
        InactivarButton(self.operator, self.project).open()

    def reload(self, *args):
        ActualizarButton(self.operator).open()

    def on_pre_enter(self, *args):
        self.id_proyecto.text = f'ODP {self.operator} está en el proyecto {self.project}'

    def newPayee(self, *args):
        EmergentNuevoBeneficiario(self.operator, self.project).open()

    def loadInformation(self, *args):
        AcceptLoading(self.operator).open()


class EmergentNuevoBeneficiario(class_declaration.PopupFather):
    id_payee = ObjectProperty()

    def __init__(self, *args, **kwargs):
        super().__init__(**kwargs)
        self.operator = args[0]
        self.project = args[1]
        self.id_payee.bind(on_text_validate=self.on_validate)

    def on_pre_open(self):
        self.title = f"ODP {self.operator} ingrese el número de documento del nuevo beneficiario"

    def on_validate(self, *args):
        if not args[0].alertFlag['complete']:
            class_declaration.MessagePopup(args[0].alertFlag['message']).open()
        else:
            projects = querys.payeeProjects(querys.idProject(self.project.lower()))
            if not args[0].text in projects:
                InformacionGeneral.InformacionGeneralScreen.payeeDocument = args[0].text
                DiagnosticoPerfilProductivo.DiagnosticoPerfilProductivoScreen.payeeDocument = args[0].text
                IdeaDeNegocio.IdeaDeNegocioScreen.payeeDocument = args[0].text
                UnidadDeNegocio.UnidadDeNegocioScreen.payeeDocument = args[0].text
                UnidadDeNegocio.UnidadDeNegocioScreen.caracterizacion_ampliada = False
                self.dismiss()
                self.changeWindow()
            else:
                class_declaration.MessagePopup('El beneficiario ya tiene caracterización básica').open()

    def changeWindow(self, *args):
        pass


class AcceptLoading(class_declaration.PopupFather):
    id_acceptButton = ObjectProperty()

    def __init__(self, *args, **kwargs):
        super().__init__(**kwargs)
        self.operator = args[0]
        self.id_acceptButton.bind(on_release=self.on_validate)

    def on_pre_open(self):
        self.title = f"ODP {self.operator} esta acción requiere conexión a internet. ¿Desea continuar?"

    def on_validate(self, *args):
        class_declaration.MessagePopup(f'Starting sending POST requests').open()
        # upload_process.uploadInformation()
        self.dismiss()


class CaracterizacionAmpliadaButton(class_declaration.PopupFather):
    id_payee = ObjectProperty()

    def __init__(self, *args, **kwargs):
        super().__init__(**kwargs)
        self.operator = args[0]
        self.project = args[1]
        self.id_payee.bind(on_text_validate=self.on_validate)

    def on_pre_open(self):
        self.title = f"ODP {self.operator} ingrese el número de documento del beneficiario"

    def on_validate(self, *args):
        if not args[0].alertFlag['complete']:
            class_declaration.MessagePopup(args[0].alertFlag['message']).open()
        else:
            projects = querys.payeeProjects(querys.idProject(self.project.lower()))
            if not args[0].text in projects:
                class_declaration.MessagePopup('El beneficiario no tiene caracterización básica').open()
            else:
                if args[0].text in querys.lista_de_caracterizaciones(querys.idProject(self.project.lower())):
                    class_declaration.MessagePopup('El beneficiario ya tiene caracterización Ampliada').open()
                else:
                    if querys.obtener_estado(args[0].text) == 2:
                        class_declaration.MessagePopup('El beneficiario se encuentra inactivo').open()
                    else:
                        CaracterizacionAmpliada.CaracterizacionAmpliadaScreen.payeeDocument = args[0].text
                        Monitoreo.MonitoreoScreen.payeeDocument = args[0].text
                        UnidadDeNegocio.UnidadDeNegocioScreen.payeeDocument = args[0].text
                        DiagnosticoEmpresarial.DiagnosticoEmpresarialScreen.payeeDocument = args[0].text
                        self.dismiss()
                        self.changeWindow()

    def changeWindow(self, *args):
        pass


class MonitoreoButton(class_declaration.PopupFather):
    id_payee = ObjectProperty()

    def __init__(self, *args, **kwargs):
        super().__init__(**kwargs)
        self.operator = args[0]
        self.project = args[1]
        self.id_payee.bind(on_text_validate=self.on_validate)

    def on_pre_open(self):
        self.title = f"ODP {self.operator} ingrese el número de documento del beneficiario"

    def on_validate(self, *args):
        if not args[0].alertFlag['complete']:
            class_declaration.MessagePopup(args[0].alertFlag['message']).open()
        else:
            projects = querys.payeeProjects(querys.idProject(self.project.lower()))
            if not args[0].text in projects:
                class_declaration.MessagePopup('El beneficiario no tiene caracterización básica').open()
            else:
                if querys.obtener_estado(args[0].text) == 2:
                    class_declaration.MessagePopup('El beneficiario se encuentra inactivo').open()
                else:
                    if args[0].text in querys.lista_de_caracterizaciones(querys.idProject(self.project.lower())):
                        if querys.numero_de_monitoreo(args[0].text) == 1:
                            if querys.comprobar_plan_de_formacion(args[0].text, querys.idProject(self.project.lower())) == 1:
                                Monitoreo.MonitoreoScreen.numero_de_monitoreo = 2
                                Monitoreo.MonitoreoScreen.payeeDocument = args[0].text
                                DiagnosticoEmpresarial.DiagnosticoEmpresarialScreen.payeeDocument = args[0].text
                                self.changeWindow()
                                self.dismiss()
                            else:
                                class_declaration.MessagePopup('El beneficiario no ha terminado la formación').open()
                        else:
                            class_declaration.MessagePopup('El Beneficiario no tiene los monitoreos necesarios').open()
                    else:
                        class_declaration.MessagePopup('El beneficiario no tiene caracterización Ampliada').open()

    def changeWindow(self, *args):
        pass


class PlanDeImplementacionButton(class_declaration.PopupFather):
    id_payee = ObjectProperty()

    def __init__(self, *args, **kwargs):
        super().__init__(**kwargs)
        self.operator = args[0]
        self.project = args[1]
        self.id_payee.bind(on_text_validate=self.on_validate)

    def on_pre_open(self):
        self.title = f"ODP {self.operator} ingrese el número de documento del beneficiario"

    def on_validate(self, *args):
        if not args[0].alertFlag['complete']:
            class_declaration.MessagePopup(args[0].alertFlag['message']).open()
        else:
            projects = querys.payeeProjects(querys.idProject(self.project.lower()))
            if not args[0].text in projects:
                class_declaration.MessagePopup('El beneficiario no tiene caracterización básica').open()
            else:
                if querys.obtener_estado(args[0].text) == 2:
                    class_declaration.MessagePopup('El beneficiario se encuentra inactivo').open()
                else:
                    if args[0].text in querys.lista_de_caracterizaciones(querys.idProject(self.project.lower())):
                        if querys.numero_de_monitoreo(args[0].text) == 2:
                            if querys.plan_de_implementacion_habilitado(args[0].text) == 2:
                                ActividadDeImplementacion.ActividadDeImplementacionScreen.payeeDocument = args[0].text
                                visitas = list(querys.ver_cuantas_visitas(args[0].text, querys.idProject(self.project.lower())))
                                if visitas[1] < visitas[0]:
                                    self.dismiss()
                                    self.changeWindow()
                                else:
                                    class_declaration.MessagePopup('El beneficiario ya completó el seguimiento').open()
                            else:
                                PlanDeImplementacion.PlanDeImplementacionScreen.payeeDocument = args[0].text
                                self.dismiss()
                                self.changeToPlan()
                        else:
                            class_declaration.MessagePopup('El Beneficiario no tiene los monitoreos necesarios').open()
                    else:
                        class_declaration.MessagePopup('El beneficiario no tiene caracterización Ampliada').open()

    def changeWindow(self, *args):
        pass

    def changeToPlan(self, *args):
        pass


class PlanDeFormacionButton(class_declaration.PopupFather):
    id_payee = ObjectProperty()

    def __init__(self, *args, **kwargs):
        super().__init__(**kwargs)
        self.operator = args[0]
        self.project = args[1]
        self.id_payee.bind(on_text_validate=self.on_validate)

    def on_pre_open(self):
        self.title = f"ODP {self.operator} ingrese el número de documento del beneficiario"

    def on_validate(self, *args):
        if not args[0].alertFlag['complete']:
            class_declaration.MessagePopup(args[0].alertFlag['message']).open()
        else:
            projects = querys.payeeProjects(querys.idProject(self.project.lower()))
            if not args[0].text in projects:
                class_declaration.MessagePopup('El beneficiario no existe').open()
            else:
                if querys.obtener_estado(args[0].text) == 2:
                    class_declaration.MessagePopup('El beneficiario se encuentra inactivo').open()
                else:
                    if args[0].text in querys.lista_de_caracterizaciones(querys.idProject(self.project.lower())):
                        if querys.numero_de_monitoreo(args[0].text) == 1:
                            if querys.plan_de_formacion_habilitado(args[0].text) == 2:
                                actividades = querys.traer_actividades_formacion(args[0].text, querys.idProject(self.project.lower()))
                                actividades_string = []
                                completados, faltantes = 0, 0
                                for activ in actividades:
                                    num, fecha, completada = activ
                                    if completada == 2:
                                        faltantes += 1
                                        num = querys.traer_descripcion_actividad_formacion(num)
                                        string_mostrar = num + ' ' + fecha
                                        actividades_string.append(string_mostrar)

                                    elif completada == 1:
                                        completados += 1
                                ActividadDeFormacion.ActividadDeFormacionScreen.actividades = actividades_string
                                ActividadDeFormacion.ActividadDeFormacionScreen.payeeDocument = args[0].text
                                ActividadDeFormacion.ActividadDeFormacionScreen.project = self.project
                                ActividadDeFormacion.ActividadDeFormacionScreen.actividades_faltantes = faltantes
                                ActividadDeFormacion.ActividadDeFormacionScreen.actividades_realizadas = completados
                                if faltantes == 0:
                                    class_declaration.MessagePopup('El beneficiario ya realizó todas las actividades').open()
                                else:
                                    self.dismiss()
                                    self.changeWindow()

                            else:
                                PlanDeFormacion.PlanDeFormacionScreen.payeeDocument = args[0].text
                                self.dismiss()
                                self.changeToPlan()
                        else:
                            class_declaration.MessagePopup('El Beneficiario no tiene los monitoreos necesarios').open()
                    else:
                        class_declaration.MessagePopup('El beneficiario no tiene caracterización Ampliada').open()

    def changeWindow(self, *args):
        pass

    def changeToPlan(self, *args):
        pass


class PlanDeSeguimientoButton(class_declaration.PopupFather):
    id_payee = ObjectProperty()

    def __init__(self, *args, **kwargs):
        super().__init__(**kwargs)
        self.operator = args[0]
        self.project = args[1]
        self.id_payee.bind(on_text_validate=self.on_validate)

    def on_pre_open(self):
        self.title = f"ODP {self.operator} ingrese el número de documento del beneficiario"

    def on_validate(self, *args):
        if not args[0].alertFlag['complete']:
            class_declaration.MessagePopup(args[0].alertFlag['message']).open()
        else:
            projects = querys.payeeProjects(querys.idProject(self.project.lower()))
            if not args[0].text in projects:
                class_declaration.MessagePopup('El beneficiario no tiene caracterización básica').open()
            else:
                if querys.obtener_estado(args[0].text) == 3:
                    class_declaration.MessagePopup('El beneficiario se encuentra inactivo').open()
                else:
                    if args[0].text in querys.lista_de_caracterizaciones(querys.idProject(self.project.lower())):
                        if querys.numero_de_monitoreo(args[0].text) == 3:
                            self.changeWindow()
                            self.dismiss()
                        else:
                            class_declaration.MessagePopup('El Beneficiario no tiene los monitoreos necesarios').open()
                    else:
                        class_declaration.MessagePopup('El beneficiario no tiene caracterización Ampliada').open()

    def changeWindow(self, *args):
        pass


class ConsultarButton(class_declaration.PopupFather):
    id_payee = ObjectProperty()

    def __init__(self, *args, **kwargs):
        super().__init__(**kwargs)
        self.operator = args[0]
        self.project = args[1]
        self.id_payee.bind(on_text_validate=self.on_validate)

    def on_pre_open(self):
        self.title = f"ODP {self.operator} ingrese el número de documento del beneficiario"

    def on_validate(self, *args):
        if not args[0].alertFlag['complete']:
            class_declaration.MessagePopup(args[0].alertFlag['message']).open()
        else:
            self.dismiss()


class InactivarButton(class_declaration.PopupFather):
    id_payee = ObjectProperty()

    def __init__(self, *args, **kwargs):
        super().__init__(**kwargs)
        self.operator = args[0]
        self.project = args[1]
        self.id_payee.bind(on_text_validate=self.on_validate)

    def on_pre_open(self):
        self.title = f"ODP {self.operator} ingrese el número de documento del beneficiario"

    def on_validate(self, *args):
        if not args[0].alertFlag['complete']:
            class_declaration.MessagePopup(args[0].alertFlag['message']).open()
        else:
            projects = querys.payeeProjects(querys.idProject(self.project.lower()))
            if not args[0].text in projects:
                class_declaration.MessagePopup('El beneficiario no existe').open()
            else:
                if querys.obtener_estado(args[0].text) == 2:
                    class_declaration.MessagePopup('El beneficiario se encuentra inactivo').open()
                elif querys.obtener_estado(args[0].text) == 3:
                    class_declaration.MessagePopup('El beneficiario ya terminó todo su proceso').open()
                else:
                    class_declaration.MessagePopup(f'El beneficiario {args[0].text} fue inactivado').open()
                    querys.inactivar_beneficiario(args[0].text, querys.idProject(self.project.lower()))
                    self.dismiss()


class ActualizarButton(class_declaration.PopupFather):
    id_acceptButton = ObjectProperty()

    def __init__(self, *args, **kwargs):
        super().__init__(**kwargs)
        self.operator = args[0]
        self.id_acceptButton.bind(on_release=self.on_validate)

    def on_pre_open(self):
        self.title = f"ODP {self.operator} esta acción requiere conexión a internet. ¿Desea continuar?"

    def on_validate(self, *args):
        class_declaration.MessagePopup(f'Starting sending POST requests').open()
        upload_process.uploadInformation()
        self.dismiss()
