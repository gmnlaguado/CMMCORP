# coding=utf-8
from kivy.uix.screenmanager import Screen
from kivy.properties import ObjectProperty
from declarations import querys, class_declaration, upload_process
from windows import PlanDeImplementacion, InformacionGeneral, DiagnosticoPerfilProductivo, UnidadDeNegocio, \
    IdeaDeNegocio, CaracterizacionAmpliada, Monitoreo, PlanDeFormacion


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
                CaracterizacionAmpliada.CaracterizacionAmpliadaScreen.payeeDocument = args[0].text
                Monitoreo.MonitoreoScreen.payeeDocument = args[0].text
                UnidadDeNegocio.UnidadDeNegocioScreen.payeeDocument = args[0].text
                PlanDeFormacion.PlanDeFormacionScreen.payeeDocument = args[0].text
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
            self.dismiss()
            self.changeWindow()

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
            PlanDeImplementacion.PlanDeImplementacionScreen.form_title = "Plan de Implementación"
            self.dismiss()
            self.changeWindow()

    def changeWindow(self, *args):
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
            self.dismiss()
            self.changeWindow()

    def changeWindow(self, *args):
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
            PlanDeImplementacion.PlanDeImplementacionScreen.form_title = "Plan de Seguimiento"
            self.dismiss()
            self.changeWindow()

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
            self.dismiss()
            self.changeWindow()

    def changeWindow(self, *args):
        pass


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
