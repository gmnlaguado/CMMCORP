# coding=utf-8
from kivy.uix.screenmanager import Screen
from kivy.properties import ObjectProperty
from declarations import querys
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout


class PlanDeFormacionScreen(Screen):
    id_selectedActivities = ObjectProperty()
    id_program = ObjectProperty()
    id_line = ObjectProperty()
    id_level = ObjectProperty()
    id_container_grid = ObjectProperty()
    id_title = ObjectProperty()

    def __init__(self, *args, **kwargs):
        super().__init__(**kwargs)
        self.id_title.text = "Plan de Formación"
        self.id_program.values = querys.bringProgramFromEducationPlan()
        self.id_program.bind(text=self.loadLines)
        self.id_line.bind(text=self.loadLevels)
        self.id_level.bind(text=self.loadDescriptions)
        self.id_container_grid.bind(minimum_height=self.id_container_grid.setter('height'))

    def on_pre_enter(self, *args):
        self.id_program.text = "Programa"
        self.id_line.text = "Linea"
        self.id_level.text = "Nivel"

    def loadLines(self, *args):
        if args[1] != "Programa":
            self.id_line.values = querys.bringLineFromEducationPlan(args[1])

    def loadLevels(self, *args):
        if args[1] != "Linea":
            self.id_level.values = querys.bringLevelFromEducationPlan(self.id_program.text, args[1])

    def loadDescriptions(self, *args):
        if args[1] != "Nivel":
            self.id_container_grid.clear_widgets()
            questions = querys.bringDescriptionsFromEducationPlan(self.id_program.text, self.id_line.text, args[1])
            for idx, quest in enumerate(questions):
                box_layout = BoxLayout(size_hint=(None, None), size=(1040, 40))
                lab = Label(text=f'{idx + 1}]      ' + quest, halign="left", valign="middle", size_hint=(None, None),
                            size=(840, 40), color=(0, 0, 0, 0.85), font_size=24, font_name="montserrat",
                            text_size=(840, 40))
                textInputData = TextInputScrollData()
                box_layout.add_widget(lab)
                box_layout.add_widget(textInputData)
                self.id_container_grid.add_widget(box_layout)


class TextInputScrollData(TextInput):
    def __init__(self, *args, **kwargs):
        super().__init__(**kwargs)
        self.size = (186, 40)
        self.font_name = "montserrat"
        self.color = (1, 1, 1, 1)
        self.size_hint = (None, None)
        self.halign = "left"
        self.valign = "middle"
        self.background_color = (255 / 255, 255 / 255, 255 / 255, 1)
        self.background_normal = ""
        self.complete = False
        self.class_type = "input"
        self.multiline = False
        self.hint_text = "DD/MM/AAAA"

    def on_text_validate(self, *args):
        self.background_color = 7 / 255, 7 / 255, 7 / 255, 0.1