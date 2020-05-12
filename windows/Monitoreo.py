# coding=utf-8
from kivy.uix.screenmanager import Screen
from kivy.properties import ObjectProperty


class MonitoreoScreen(Screen):

    id_title = ObjectProperty()
    id_ciiu = ObjectProperty()
    id_womenAssosiation = ObjectProperty()
    id_houseMaterial = ObjectProperty()
    id_houseType = ObjectProperty()
    id_tier = ObjectProperty()
    id_houseAge = ObjectProperty()
    id_bedrooms = ObjectProperty()
    id_kitchenFuel = ObjectProperty()
    id_incomeSource = ObjectProperty()
    id_dependants = ObjectProperty()
    id_whoDefineIncome = ObjectProperty()
    id_quantityAndExpenses = ObjectProperty()
    id_ExpensesResume = ObjectProperty()
    id_belongsToAssosiation = ObjectProperty()
    id_bussinesSector = ObjectProperty()
    id_container_grid_1 = ObjectProperty()
    id_container_grid_2 = ObjectProperty()

    def __init__(self, *args, **kwargs):
        super().__init__(**kwargs)
        self.id_title.text = "Monitoreo"
        self.id_ciiu.text = "CIIU"
        self.id_womenAssosiation.text = "¿Es una asociación de mujeres?"
        self.id_houseMaterial.text = "Material predominante"
        self.id_houseType.text = "Tipo de vivienda"
        self.id_tier.text = "Estrato"
        self.id_houseAge.text = "Antiguedad"
        self.id_bedrooms.text = "Número de dormitorios"
        self.id_kitchenFuel.text = "Combustible usado en cocina"
        self.id_incomeSource.text = "Sujeto y fuentes de ingreso"
        self.id_dependants.text = "Personas que dependen economicamente de usted"
        self.id_whoDefineIncome.text = "¿Quién define la distribución de dinero en el hogar"
        self.id_quantityAndExpenses.text = "Gastos y cantidad"
        self.id_ExpensesResume.text = "Total Gastos"
        self.id_belongsToAssosiation.text = "¿Pertenece a asociación"
        self.id_bussinesSector.text = "Sector Empresarial"



