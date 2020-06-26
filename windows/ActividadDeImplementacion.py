# coding=utf-8
from kivy.uix.screenmanager import Screen
from kivy.properties import ObjectProperty
from declarations import class_declaration, querys
from kivy.uix.spinner import Spinner
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.checkbox import CheckBox
from kivy.uix.button import Button
from windows import Monitoreo


class ActividadDeImplementacionScreen(Screen):
    project = None
    operator = None
    payeeDocument = None
    home = False
    estados_metas = []
    metas_terminadas = False

    id_title = ObjectProperty()
    id_payeeName = ObjectProperty()
    id_payeeDocument = ObjectProperty()
    id_container_grid = ObjectProperty()
    id_signInButton = ObjectProperty()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.id_title.text = "Actividad de Implementación"
        self.id_container_grid.bind(minimum_height=self.id_container_grid.setter('height'))
        button_1 = ButtonScroll(text="Ingresar")
        button_1.bind(on_release=self.estados)
        self.id_container_grid.add_widget(button_1)
        spinner_1 = SpinnerScroll(text="Tipo de visita", values=querys.parametricList('tipo_visita'))
        self.id_container_grid.add_widget(spinner_1)
        label_1 = LabelScroll(text="Si elige otro, indique la dirección")
        self.id_container_grid.add_widget(label_1)
        input_1 = TextInputScroll()
        self.id_container_grid.add_widget(input_1)
        spinner_2 = SpinnerScroll(text="Plan de Inversiones", values=querys.parametricList('plan_de_inversiones'))
        self.id_container_grid.add_widget(spinner_2)
        label_2 = LabelScroll(text="Observaciones")
        self.id_container_grid.add_widget(label_2)
        input_2 = TextInputScroll()
        self.id_container_grid.add_widget(input_2)

        contain = BoxLayout(size_hint=(None, None), size=(673, 40))
        label_3 = LabelScroll(text="Seguimiento al desembolso")
        contain.add_widget(label_3)
        check = CheckBox(group=f"following", color=(0, 1, 0, 1))
        contain.add_widget(check)
        self.id_container_grid.add_widget(contain)

        spinner_3 = SpinnerScroll(text="¿Seguimiento al desembolso?", values=querys.parametricList('seguimiento_desembolso'))
        self.id_container_grid.add_widget(spinner_3)

        spinner_4 = SpinnerScroll(text="En caso de alerta ¿Cuál?", values=querys.parametricList('alerta_seguimiento'))
        self.id_container_grid.add_widget(spinner_4)

        label_4 = LabelScroll(text="Si elige otro, por favor explique")
        self.id_container_grid.add_widget(label_4)

        input_3 = TextInputScroll()
        self.id_container_grid.add_widget(input_3)

        self.id_signInButton.bind(on_release=self.checkAll)

    def estados(self, *args):
        Estado_de_metas().open()

    def checkAll(self, *args):
        AcceptFormActividadDeImplementacion(self.operator, self.payeeDocument, self.project).open()


class SpinnerScroll(Spinner):
    def __init__(self, *args, **kwargs):
        super().__init__(**kwargs)
        self.size = (673, 40)
        self.font_size = 24
        self.font_name = "montserrat"
        self.color = (1, 1, 1, 1)
        self.size_hint = (None, None)
        self.halign = "center"
        self.valign = "middle"
        self.background_color = (61 / 255, 119 / 255, 0 / 255, 0.7)
        self.background_normal = ""
        self.complete = False
        self.class_type = "spinner"


class ButtonScroll(Button):
    def __init__(self, *args, **kwargs):
        super().__init__(**kwargs)
        self.size = (673, 40)
        self.font_size = 24
        self.font_name = "montserrat"
        self.color = (1, 1, 1, 1)
        self.size_hint = (None, None)
        self.halign = "center"
        self.valign = "middle"
        self.background_color = (61 / 255, 119 / 255, 0 / 255, 0.7)
        self.background_normal = ""
        self.complete = False
        self.class_type = "button"


class LabelScroll(Label):
    def __init__(self, *args, **kwargs):
        super().__init__(**kwargs)
        self.size = (633, 40)
        self.text_size = (633, 40)
        self.font_size = 24
        self.font_name = "montserrat"
        self.color = (0, 0, 0, 1)
        self.size_hint = (None, None)
        self.halign = "left"
        self.valign = "middle"
        self.class_type = "label"


class TextInputScroll(TextInput):
    def __init__(self, *args, **kwargs):
        super().__init__(**kwargs)
        self.size = (673, 40)
        self.font_name = "montserrat"
        self.color = (1, 1, 1, 1)
        self.font_size = 24
        self.size_hint = (None, None)
        self.halign = "left"
        self.valign = "middle"
        self.background_color = (255 / 255, 255 / 255, 255 / 255, 1)
        self.background_normal = ""
        self.complete = False
        self.class_type = "input"
        self.multiline = False


class AcceptFormActividadDeImplementacion(class_declaration.PopupFather):
    id_acceptButton = ObjectProperty()

    def __init__(self, *args, **kwargs):
        super().__init__(**kwargs)
        self.operator = args[0]
        self.payee = args[1]
        self.project = querys.idProject(args[2].lower())
        self.id_acceptButton.bind(on_release=self.on_validate)

    def on_pre_open(self):
        self.title = f"ODP {self.operator} verifique que la información es correcta antes de continuar"

    def on_validate(self, *args):
        querys.sumar_una_actividad(self.payee, self.project)
        visitas = list(querys.ver_cuantas_visitas(self.payee, self.project))
        if visitas[1] == visitas[0]:
            querys.dar_terminada_implementacion(self.payee, self.project)
            Monitoreo.MonitoreoScreen.numero_de_monitoreo = 2
            querys.modificar_etapa_del_proceso(self.payee, self.project, 4)
        self.dismiss()
        self.changeWindow()

    def changeWindow(self, *args):
        pass


class Estado_de_metas(class_declaration.PopupFather):
    id_container_grid = ObjectProperty()
    id_botonAceptar = ObjectProperty()

    def __init__(self, *args, **kwargs):
        super().__init__(**kwargs)
        self.title = "Estado de las metas"

    def on_open(self):
        self.id_botonAceptar.bind(on_release=self.accionAceptar)
        self.id_container_grid.bind(minimum_height=self.id_container_grid.setter('height'))
        categories = querys.parametricList('businessDiagnosisCategories')

        for cat in categories:
            lab_1 = Label(text=cat, halign="center", valign="middle", size_hint=(None, None),
                          size=(318, 40), color=(0, 0, 0, 0.85), font_size=20, font_name="montserrat",
                          text_size=(318, 40))
            lab_2 = Label(text='Esto es el ejemplo de una meta, ahora la única meta que tengo es...', halign="center", valign="middle", size_hint=(None, None),
                          size=(400, 40), color=(0, 0, 0, 0.85), font_size=14, font_name="montserrat",
                          text_size=(400, 40))
            spin_gen = SpinnerScroll_short(text='Estado de la meta', values=querys.parametricList('estado_meta'))

            self.id_container_grid.add_widget(lab_1)
            self.id_container_grid.add_widget(lab_2)
            self.id_container_grid.add_widget(spin_gen)

    def accionAceptar(self, *args):
        dili,answ = [], []
        for idx, childs in enumerate(self.id_container_grid.children):
            if idx % 3 == 0:
                dili.append(childs.diligenciado)
                if childs.diligenciado:
                    answ.append(childs.text)
        if False in dili:
            ActividadDeImplementacionScreen.metas_terminadas = False
        else:
            ActividadDeImplementacionScreen.estados_metas = answ
            ActividadDeImplementacionScreen.metas_terminadas = True
            self.dismiss()


class SpinnerScroll_short(Spinner):
    def __init__(self, *args, **kwargs):
        super().__init__(**kwargs)
        self.background_normal = "images/dropdown_scroll.png"
        self.background_color = 61 / 255, 119 / 255, 0 / 255, 0.7
        self.halign = "center"
        self.valign = "middle"
        self.size_hint = (None, None)
        self.size = (318, 40)
        self.color = (1, 1, 1, 1)
        self.font_size = 20
        self.font_name = "montserrat"
        self.text_size = (318, 40)
        self.diligenciado = False
        self.id = 'Spinner'
        self.class_type = "spinner"

    def on_text(self, *args):
        self.background_color = 11 / 255, 69 / 255, 0 / 255, 0.7
        self.diligenciado = True

