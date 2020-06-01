# coding=utf-8
from kivy.uix.screenmanager import Screen
from kivy.properties import ObjectProperty
from declarations import querys, class_declaration


class LoginScreen(Screen):
    id_username = ObjectProperty()
    static_password = ObjectProperty()
    id_password = ObjectProperty()
    id_message = ObjectProperty()
    id_signInButton = ObjectProperty()

    def __init__(self, *args, **kwargs):
        super().__init__(**kwargs)

        self.static_password.text = "Contraseña"

        self.elements = []
        self.elements.append(self.id_username)
        self.elements.append(self.id_password)

        self.id_username.bind(on_text_validate=self.signal)
        self.id_password.bind(on_text_validate=self.signal)
        self.id_signInButton.bind(on_release=self.checkAll)

    def signal(self, *args):
        self.id_message.text = args[0].alertFlag['message']

    def checkAll(self, *args):
        if False in [element.complete for element in self.elements]:
            self.id_message.text = "Ingrese los datos"
        else:
            op = querys.idOperator(self.id_username.text)
            if op is not None:
                ps = querys.passwordOperator(op)
                if self.id_password.text == ps:
                    LoginProjectPopup(self.id_username.text, op).open()
                else:
                    self.id_message.text = "Contraseña no coincide"
            else:
                self.id_message.text = "ODP no existe"


class LoginProjectPopup(class_declaration.PopupFather):

    id_projects = ObjectProperty()

    def __init__(self, *args, **kwargs):
        super().__init__(**kwargs)
        self.operator = args[0]
        self.document = args[1]

    def on_pre_open(self):
        self.title = f"ODP consultor {self.operator} seleccione el proyecto en el que va a trabajar ahora"
        projects = [querys.nameProject(proj).capitalize() for proj in querys.projectsOperator(self.document)]
        self.id_projects.values = projects
        self.id_projects.bind(text=self.on_selection)

    def on_selection(self, *args):
        self.dismiss()
        self.changeWindow()

    def changeWindow(self, *args):
        pass










