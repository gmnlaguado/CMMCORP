# coding=utf-8
from kivy.uix.screenmanager import Screen
from kivy.properties import ObjectProperty
from declarations import querys, class_declaration, upload_process
from windows import InformacionGeneral


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
            if self.id_payee.text not in querys.payeeProjects(querys.idProject(self.project.lower())):
                InformacionGeneral.InformacionGeneralScreen.project = self.project
                InformacionGeneral.InformacionGeneralScreen.operator = self.operator
                InformacionGeneral.InformacionGeneralScreen.payeeDocument = self.id_payee.text
                self.dismiss()
                self.changeWindow()
            else:
                class_declaration.MessagePopup('Beneficiario ya tiene C. Básica').open()

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
        upload_process.uploadInformation()
        self.dismiss()

