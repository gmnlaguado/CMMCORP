# coding=utf-8
from kivy.uix.screenmanager import Screen
from kivy.properties import ObjectProperty
from declarations import querys, class_declaration
from kivy.uix.label import Label
from kivy.uix.checkbox import CheckBox
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.spinner import Spinner
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

class MonitoreoScreen(Screen):
    id_belongToAssosiation = ObjectProperty()
    id_ciiu = ObjectProperty()
    id_pension = ObjectProperty()
    id_bussinesSector = ObjectProperty()
    id_householdExpenses = ObjectProperty()
    id_totalExpenses = ObjectProperty()
    id_householdIncomes = ObjectProperty()
    id_totalIncomes = ObjectProperty()
    id_totalDependants = ObjectProperty()
    id_whoDefineIncome = ObjectProperty()
    id_houseType = ObjectProperty()
    id_houseMaterial = ObjectProperty()
    id_bedroomsNumber = ObjectProperty()
    id_kitchenFuel = ObjectProperty()
    id_tier = ObjectProperty()
    id_houseAge = ObjectProperty()
    id_container_grid_1 = ObjectProperty()
    id_container_grid_2 = ObjectProperty()
    id_message = ObjectProperty()
    id_signInButton = ObjectProperty()

    def __init__(self, *args, **kwargs):
        super().__init__(**kwargs)
        self.id_belongToAssosiation.values = querys.parametricList('yesNo')
        self.id_ciiu.values = querys.parametricList('ciiu')
        self.id_pension.values = querys.parametricList('yesNo')
        self.id_bussinesSector.values = querys.parametricList('businessSector')
        self.id_totalDependants.values = [str(numb) for numb in range(1, 30)]
        self.id_whoDefineIncome.values = querys.parametricList('whoDefineIncome')
        self.id_houseType.values = querys.parametricList('houseType')
        self.id_houseMaterial.values = querys.parametricList('houseMaterial')
        self.id_bedroomsNumber.values = [str(numb) for numb in range(1, 30)]
        self.id_kitchenFuel.values = querys.parametricList('kitchenFuel')
        self.id_tier.values = [str(numb) for numb in range(1, 8)]
        self.id_houseAge.values = querys.parametricList('houseAge')

        questions = querys.parametricList('homeCharacteristics')
        self.id_container_grid_1.bind(minimum_height=self.id_container_grid_1.setter('height'))
        for idx, quest in enumerate(questions):
            lab = Label(text=f'{idx + 1}]  ' + quest, halign="left", valign="middle", size_hint=(None, None),
                        size=(235, 18), color=(0, 0, 0, 0.85), font_size=14, font_name="montserrat",
                        text_size=(235, 18))
            box_container = BoxLayout()
            for i in ['Si', 'No']:
                check = CheckBox(group=f"pregunta_{idx + 1}", color=(0, 1, 0, 1))
                box_container.add_widget(check)
            self.id_container_grid_1.add_widget(lab)
            self.id_container_grid_1.add_widget(box_container)
        
        self.id_container_grid_2.bind(minimum_height=self.id_container_grid_2.setter('height'))
        grid = SpinnerScroll(text="Cuenta corriente", values = ["si", "no"])
        self.id_container_grid_2.add_widget(grid)

        grid = SpinnerScroll(text="Créditos", values = ["si", "no"])
        self.id_container_grid_2.add_widget(grid)

        grid = SpinnerScroll(text="Pensiones", values = ["si", "no"])
        self.id_container_grid_2.add_widget(grid)

        grid = SpinnerScroll(text="Seguros", values = ["si", "no"])
        self.id_container_grid_2.add_widget(grid)

        box_container = BoxLayout(size_hint= (None, None), size =(673, 40))
        lab1 = Label(text="Monte del crédito", halign="left", valign="middle", size_hint=(None, None),
                        size=(275, 40), color=(0, 0, 0, 0.85), font_size=24, font_name="montserrat",
                        text_size=(275, 40))
        text1 = TextInputScroll()
        box_container.add_widget(lab1)
        box_container.add_widget(text1)
        self.id_container_grid_2.add_widget(box_container)

        grid = SpinnerScroll(text="Número de cuotas", values=[str(numb) for numb in range(1, 65)])
        self.id_container_grid_2.add_widget(grid)

        grid = SpinnerScroll(text="¿Alguno de estos servicios los tiene con Bancamía?", values = ["si", "no"])
        self.id_container_grid_2.add_widget(grid)

        grid = SpinnerScroll(text="¿Cuál servicio tiene con Bancamía?", values = querys.parametricList('bancamia'))
        self.id_container_grid_2.add_widget(grid)

        box_container = BoxLayout(size_hint= (None, None), size =(673, 40))
        lab1 = Label(text="¿Cuál programa?", halign="left", valign="middle", size_hint=(None, None),
                        size=(275, 40), color=(0, 0, 0, 0.85), font_size=24, font_name="montserrat",
                        text_size=(275, 40))
        text1 = TextInputScroll()
        box_container.add_widget(lab1)
        box_container.add_widget(text1)
        self.id_container_grid_2.add_widget(box_container)

        grid = SpinnerScroll(text="¿Depende económicamente de alguién?", values = ["si", "no"])
        self.id_container_grid_2.add_widget(grid)

        box_container = BoxLayout(size_hint= (None, None), size =(673, 40))
        lab1 = Label(text="¿De quién depende?", halign="left", valign="middle", size_hint=(None, None),
                        size=(275, 40), color=(0, 0, 0, 0.85), font_size=24, font_name="montserrat",
                        text_size=(275, 40))
        text1 = TextInputScroll()
        box_container.add_widget(lab1)
        box_container.add_widget(text1)
        self.id_container_grid_2.add_widget(box_container)

        grid = SpinnerScroll(text="¿Cuántas horas a la semana dedica al cuidado de personas a cargo?",
        values=[str(numb) for numb in range(1, 165)])
        self.id_container_grid_2.add_widget(grid)

        grid = SpinnerScroll(text="¿Cuántas horas a la semana dedica a la recreación?", 
        values=[str(numb) for numb in range(1, 165)])
        self.id_container_grid_2.add_widget(grid)

        grid = SpinnerScroll(text="¿El negocio tiene RUT?", values = ["si", "no"])
        self.id_container_grid_2.add_widget(grid)

        grid = SpinnerScroll(text="¿Tiene registro de cámara de comercio?", values = ["si", "no"])
        self.id_container_grid_2.add_widget(grid)

        grid = SpinnerScroll(text="¿Tiene NIT el negocio?", values = ["si", "no"])
        self.id_container_grid_2.add_widget(grid)

        grid = SpinnerScroll(text="¿Dónde opera su unidad productivo?", values = ["si", "no"])
        self.id_container_grid_2.add_widget(grid)

        input_list_labels = ["Ingreso del negocio", "Gastos Directos", "Gastos Indirectos", "Total de gastos", "Excedentes", 
        "Activo Fijo", "Activo No Fijo", "Total Actvios", "Pasivo Corto", "Pasivo Largo", "Deudas", "Patrimonio"]

        for input_label_value in input_list_labels:
            box_container = BoxLayout(size_hint= (None, None), size =(673, 40))
            lab1 = Label(text=input_label_value, halign="left", valign="middle", size_hint=(None, None),
                            size=(275, 40), color=(0, 0, 0, 0.85), font_size=24, font_name="montserrat",
                            text_size=(275, 40))
            text1 = TextInputScroll()
            box_container.add_widget(lab1)
            box_container.add_widget(text1)
            self.id_container_grid_2.add_widget(box_container)
        
        grid = SpinnerScroll(text="Total de trabajadores", values=[str(numb) for numb in range(1, 60)])
        self.id_container_grid_2.add_widget(grid)

        grid = SpinnerScroll(text="Tipo de local", values = ["si", "no"])
        self.id_container_grid_2.add_widget(grid)
        self.id_householdExpenses.bind(on_release=self.openPopupGastos)
        self.id_householdIncomes.bind(on_release=self.openPopupIngresos)

    def on_pre_enter(self, *args):
        self.id_belongToAssosiation.text = "¿Pertenece a alguna asociación?"
        self.id_ciiu.text = "CIIU"
        self.id_pension.text = "Pensión"
        self.id_bussinesSector.text = "Sector Empresarial"
        self.id_householdExpenses.text = "Gastos del grupo familiar"
        self.id_totalExpenses.text = "Total de gastos mensuales"
        self.id_householdIncomes.text = "Fuente de ingresos del grupo familiar"
        self.id_totalIncomes.text = "Total de ingresos mensuales"
        self.id_totalDependants.text = "Total de personas que dependen de este ingreso"
        self.id_whoDefineIncome.text = "¿Quién define la distribución de ingresos?"
        self.id_houseType.text = "Tipo de vivienda"
        self.id_houseMaterial.text = "Material predominante de la vivienda"
        self.id_bedroomsNumber.text = "Número de dormitorios"
        self.id_kitchenFuel.text = "Combustible de cocina"
        self.id_tier.text = "Estrato"
        self.id_houseAge.text = "Antiguedad"

    def openPopupGastos(self, *args):
        GastosDelGrupoFamiliarPopup().open()

    def openPopupIngresos(self, *args):
        IngresosDelGrupoFamiliarPopup().open()



class TextInputScroll(TextInput):
    def __init__(self, *args, **kwargs):
        super().__init__(**kwargs)
        self.size = (352, 40)
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

    def on_text_validate(self, *args):
        self.background_color = 7 / 255, 7 / 255, 7 / 255, 0.1

class SpinnerScroll(Spinner):
    def __init__(self, *args, **kwargs):
        super().__init__(**kwargs)
        self.size = (673, 40)
        self.font_name = "montserrat"
        self.color = (1, 1, 1, 1)
        self.size_hint = (None, None)
        self.halign="center"
        self.valign="middle"
        self.background_color = (61 / 255, 119 / 255, 0 / 255, 0.7)
        self.background_normal = ""
        self.complete = False
        self.class_type = "spinner"

    def on_text(self, *args):
        self.background_color = 11 / 255, 69 / 255, 0 / 255, 0.7
        self.complete = True


class GastosDelGrupoFamiliarPopup(class_declaration.PopupFather):
    id_rentAndServices = ObjectProperty()
    id_runningCosts = ObjectProperty()
    id_education = ObjectProperty()
    id_casualCosts = ObjectProperty()
    id_obligations = ObjectProperty()
    id_message = ObjectProperty()
    id_acceptButton = ObjectProperty()

    def __init__(self, *args, **kwargs):
        super().__init__(**kwargs)
        self.title = f"Gastos del grupo familiar"
        self.id_acceptButton.bind(on_release=self.on_validate)
    
    def on_validate(self, *args):
        self.dismiss()

class IngresosDelGrupoFamiliarPopup(class_declaration.PopupFather):
    id_employees = ObjectProperty()
    id_othersRelatives = ObjectProperty()
    id_freelanceJobs = ObjectProperty()
    id_pension = ObjectProperty()
    id_entrepreneurship = ObjectProperty()
    id_otherIncomes = ObjectProperty()
    id_message = ObjectProperty()
    id_acceptButton = ObjectProperty()

    def __init__(self, *args, **kwargs):
        super().__init__(**kwargs)
        self.title = f"Ingresos del grupo familiar"
        self.id_acceptButton.bind(on_release=self.on_validate)
    
    def on_validate(self, *args):
        self.dismiss()

        









