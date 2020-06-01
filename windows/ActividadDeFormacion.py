# coding=utf-8
from kivy.uix.screenmanager import Screen
from kivy.properties import ObjectProperty
from declarations import class_declaration


class ActividadDeFormacionScreen(Screen):
    id_title = ObjectProperty()
    id_payee = ObjectProperty()
    id_payeeDocument = ObjectProperty()
    id_done = ObjectProperty()
    id_pending = ObjectProperty()
    id_percentage = ObjectProperty()
    id_activities = ObjectProperty()
    id_message = ObjectProperty()
    id_signInButton = ObjectProperty()
    id_homeButton = ObjectProperty()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.id_title.text = "Actvidad de Formación"
        self.id_activities.bind(text=self.selectActivity)

    def on_pre_enter(self, *args):
        self.id_activities.text = "Actividad De Formación"

    def selectActivity(self, *args):
        if args[1] != "Actividad De Formación":
            SeleccionarActividad().open()


class SeleccionarActividad(class_declaration.PopupFather):
    id_date = ObjectProperty()

    def __init__(self, *args, **kwargs):
        super().__init__(**kwargs)
        self.id_date.bind(on_text_validate=self.on_validate)

    def on_pre_open(self):
        self.title = f"Ingrese la fecha a realizar la actividad"

    def on_validate(self, *args):
        self.dismiss()