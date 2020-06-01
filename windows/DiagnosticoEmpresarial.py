# coding=utf-8
from kivy.uix.screenmanager import Screen
from kivy.properties import ObjectProperty
from declarations import querys, class_declaration
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.checkbox import CheckBox


class DiagnosticoEmpresarialScreen(Screen):
    project = None
    operator = None
    payeeDocument = None
    home = False

    id_container_grid_1 = ObjectProperty()
    id_message = ObjectProperty()
    id_signInButton = ObjectProperty()

    def __init__(self, *args, **kwargs):
        super().__init__(**kwargs)

        questions = querys.parametricList('businessDiagnosisQuestions')
        categories = querys.parametricList('businessDiagnosisCategories')
        answers = querys.parametricList('businessDiagnosisAnswers')
        counter = 0
        totalAnswers = 0
        self.id_container_grid_1.bind(minimum_height=self.id_container_grid_1.setter('height'))
        for idx, quest in enumerate(questions):
            # Question Category
            if idx % 5 == 0 and counter < len(categories):
                cat = Label(text=categories[counter], halign="center", valign="middle", size_hint=(None, None),
                            size=(853, 51), color=(0, 0, 0, 0.85), font_size=30, font_name="montserrat",
                            text_size=(853, 51))

                counter += 1
                self.id_container_grid_1.add_widget(cat)

            # Questions Statement
            box_container = BoxLayout(size_hint=(None, None), size=(1035, 110))
            lab = Label(text=quest, halign="center", valign="middle", size_hint=(None, None),
                        size=(294, 109), color=(0, 0, 0, 0.85), font_size=20, font_name="montserrat",
                        text_size=(294, 109))
            box_container.add_widget(lab)

            # Options to Answer with its checboxes
            answers_container = BoxLayout(size_hint=(None, None), size=(696, 110), spacing=12, orientation="vertical")
            for i in range(4):
                # Single Option
                line_container = BoxLayout(size_hint=(None, None), size=(696, 20))
                ans = Label(text=answers[totalAnswers], halign="center", valign="middle", size_hint=(None, None),
                            size=(661, 18), color=(0, 0, 0, 0.85), font_size=14, font_name="montserrat",
                            text_size=(661, 18))
                check = CheckBox(group=f"pregunta_{counter}_opcion{idx}", color=(0, 1, 0, 1))
                totalAnswers += 1
                line_container.add_widget(ans)
                line_container.add_widget(check)
                answers_container.add_widget(line_container)
            box_container.add_widget(answers_container)

            self.id_container_grid_1.add_widget(box_container)

        self.id_signInButton.bind(on_release=self.checkAll)

    def checkAll(self, *args):
        AcceptFormDiagnosticoEmpresarial(self.operator).open()


class AcceptFormDiagnosticoEmpresarial(class_declaration.PopupFather):
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