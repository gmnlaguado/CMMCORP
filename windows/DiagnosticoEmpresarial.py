# coding=utf-8
from kivy.uix.screenmanager import Screen
from kivy.properties import ObjectProperty
from declarations import querys
from kivy.uix.label import Label

class DiagnosticoEmpresarialScreen(Screen):
    id_container_grid_1: ObjectProperty()

    def __init__(self, *args, **kwargs):
        super().__init__(**kwargs)

        questions = querys.parametricList('businessDiagnosisQuestions')
        categories = querys.parametricList('businessDiagnosisCategories')
        counter = 0
        self.id_container_grid_1.bind(minimum_height=self.id_container_grid_1.setter('height'))
        for idx, quest in enumerate(questions):
            if idx % 5 == 0 and counter < len(categories):
                cat = Label(text=categories[counter], halign="center", valign="middle", size_hint=(None, None),
                        size=(853, 51), color=(0, 0, 0, 0.85), font_size=30, font_name="montserrat",
                        text_size=(853, 51))
                        
                counter += 1
                self.id_container_grid_1.add_widget(cat)

            lab = Label(text=quest, halign="center", valign="middle", size_hint=(None, None),
                        size=(294, 109), color=(0, 0, 0, 0.85), font_size=20, font_name="montserrat",
                        text_size=(294, 109))
            #box_container = BoxLayout(size_hint= (None, None), size =(661, 108), spacing=12)
            self.id_container_grid_1.add_widget(lab)
            #self.id_container_grid_1.add_widget(box_container)