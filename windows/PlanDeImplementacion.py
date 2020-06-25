# coding=utf-8
from kivy.uix.screenmanager import Screen
from kivy.properties import ObjectProperty
from kivy.uix.textinput import TextInput
from declarations import querys, class_declaration
from kivy.uix.label import Label


class PlanDeImplementacionScreen(Screen):
    form_title = None
    project = None
    operator = None
    payeeDocument = None
    home = False

    id_title = ObjectProperty()
    id_container_grid = ObjectProperty()
    id_lineLabel = ObjectProperty()
    id_finishedDataLabel = ObjectProperty()
    id_message = ObjectProperty()
    id_signInButton = ObjectProperty()
    id_homeButton = ObjectProperty()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.id_title.text = "Plan de Implementación"
        self.id_lineLabel.text = "Línea"
        self.id_finishedDataLabel.text = "Terminación"
        self.id_signInButton.bind(on_release=self.checkAll)

    def checkAll(self, *args):
        AcceptFormPlanDeImplementacion(self.operator).open()

    def on_pre_enter(self, *args):
        if self.form_title is not None:
            self.id_title.text = self.form_title

        self.id_container_grid.clear_widgets()
        self.id_container_grid.bind(minimum_height=self.id_container_grid.setter('height'))
        scores = querys.traer_puntajes_diagnostico(self.payeeDocument, querys.idProject(self.project.lower()))
        lines = querys.parametricList('developingLines')
        for idx, quest in enumerate(lines):
            lab = Label(text=quest, halign="left", valign="middle", size_hint=(None, None),
                        size=(228, 63), color=(0, 0, 0, 0.85), font_size=24, font_name="montserrat",
                        text_size=(228, 63))
            self.id_container_grid.add_widget(lab)
            lab_score = Label(text=str(scores[idx]), halign="center", valign="middle", size_hint=(None, None),
                              size=(28, 63), color=(0, 0, 0, 0.85), font_size=16, font_name="montserrat",
                              text_size=(28, 63))
            self.id_container_grid.add_widget(lab_score)
            goal = TextInputScroll()
            self.id_container_grid.add_widget(goal)
            data_1 = TextInputScrollData()
            self.id_container_grid.add_widget(data_1)
            data_2 = TextInputScrollData()
            self.id_container_grid.add_widget(data_2)


class TextInputScroll(TextInput):
    def __init__(self, *args, **kwargs):
        super().__init__(**kwargs)
        self.size = (402, 40)
        self.font_name = "montserrat"
        self.color = (1, 1, 1, 1)
        self.size_hint = (None, None)
        self.halign="center"
        self.valign="middle"
        self.background_color = (255/ 255, 255/ 255, 255 / 255, 1)
        self.background_normal = ""
        self.complete = False
        self.class_type = "input"
        self.multiline = False


class TextInputScrollData(TextInput):
    def __init__(self, *args, **kwargs):
        super().__init__(**kwargs)
        self.size = (186,40)
        self.font_name = "montserrat"
        self.color = (1, 1, 1, 1)
        self.size_hint = (None, None)
        self.halign="center"
        self.valign="middle"
        self.background_color = (255/255, 255/255, 255/255, 1)
        self.background_normal = ""
        self.complete = False
        self.class_type = "input"
        self.multiline = False
        self.hint_text = "DD/MM/AAAA"


class AcceptFormPlanDeImplementacion(class_declaration.PopupFather):
    id_acceptButton = ObjectProperty()

    def __init__(self, *args, **kwargs):
        super().__init__(**kwargs)
        self.operator = args[0]
        self.id_acceptButton.bind(on_release=self.on_validate)

    def on_pre_open(self):
        self.title = f"ODP {self.operator} verifique que la información es correcta antes de continuar"

    def on_validate(self, *args):
        self.dismiss()
        self.changeWindow()

    def changeWindow(self, *args):
        pass