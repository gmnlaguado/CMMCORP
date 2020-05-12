# coding=utf-8
from kivy.uix.screenmanager import Screen
<<<<<<< HEAD
from kivy.properties import ObjectProperty
from declarations import querys, class_declaration, dataFormating


class CaracterizacionAmpliadaScreen(Screen):

    id_title = ObjectProperty()
    id_adittionalStudies = ObjectProperty()
    id_studies = ObjectProperty()
    id_workingRelationship = ObjectProperty()
    id_freelance = ObjectProperty()
    id_householdHead = ObjectProperty()
    id_householdMembers = ObjectProperty()
    id_healthRegime = ObjectProperty()
    id_maritalStatus = ObjectProperty()
    id_agreementType = ObjectProperty()
    id_rut = ObjectProperty()
    id_childrenNumber = ObjectProperty()
    id_dependants = ObjectProperty()
    id_coverTheFamily = ObjectProperty()
    id_averageIncomeContract = ObjectProperty()
    id_averageIncomeActivity = ObjectProperty()
    id_childrenInformation = ObjectProperty()
    id_dependantsInformation = ObjectProperty()
    id_pension = ObjectProperty()
    id_arl = ObjectProperty()
    id_factorsThatPreventYou = ObjectProperty()
    id_observations = ObjectProperty()
    id_message = ObjectProperty()
    id_signInButton = ObjectProperty()

    def __init__(self, *args, **kwargs):
        super().__init__(**kwargs)
        self.id_title.text = "Caracterización Ampliada"
        self.id_adittionalStudies.hint_text = "Formación superior o cursos complementarios"
        self.id_factorsThatPreventYou.hint_text = "Factores que le impiden participar en este proyecto"
        self.id_observations.hint_text = "Observaciones / aclaraciones"

        self.id_studies.values = querys.parametricList('studies')
        self.id_workingRelationship.values = querys.parametricList('yesNo')
        self.id_freelance.values = querys.parametricList('yesNo')
        self.id_householdHead.values = querys.parametricList('yesNo')
        self.id_householdHead.values = [str(numb) for numb in range(1, 30)]
        self.id_healthRegime.values = querys.parametricList('healthRegime')
        self.id_maritalStatus.values = querys.parametricList('maritalStatus')
        self.id_agreementType.values = querys.parametricList('agreementType')
        self.id_rut.values = querys.parametricList('yesNo')
        self.id_childrenNumber.values = [str(numb) for numb in range(1, 30)]
        self.id_dependants.values = [str(numb) for numb in range(1, 30)]
        self.id_coverTheFamily.values = querys.parametricList('yesNo')
        self.id_averageIncomeContract.values = querys.parametricList('averageIncome')
        self.id_averageIncomeActivity.values = querys.parametricList('averageIncome')
        self.id_pension.values = querys.parametricList('yesNo')
        self.id_arl.values = querys.parametricList('yesNo')
        self.id_householdMembers.values = [str(numb) for numb in range(1, 30)]


    def on_pre_enter(self, *args):
        self.id_studies.text = 'Nivel de escolaridad'
        self.id_workingRelationship.text = '¿Tiene vinculación laboral con contrato?'
        self.id_freelance.text = '¿Independiente?'
        self.id_householdHead.text = '¿Es cabeza de familia?'
        self.id_householdMembers.text = 'Número de integrantes en el hogar'
        self.id_healthRegime.text = 'Régimen de salud'
        self.id_maritalStatus.text = 'Estado Civil'
        self.id_agreementType.text = 'Tipo de contrato'
        self.id_rut.text = '¿Tiene RUT?'
        self.id_childrenNumber.text = '¿Número de hijos?'
        self.id_dependants.text = '¿Cuántas personas tiene a cargo?'
        self.id_coverTheFamily.text = '¿Cubre su familia?'
        self.id_averageIncomeContract.text = 'Promedio de ingresos por contrato'
        self.id_averageIncomeActivity.text = 'Promedio de ingresos en esta actividad'
        self.id_childrenInformation.text = 'Información de hijos'
        self.id_dependantsInformation.text = 'Info. personas a cargo'
        self.id_pension.text = 'Pensión'
        self.id_arl.text = 'ARL'
        self.id_message.text = ''
        self.id_signInButton.text = 'Ingresar'


        self.id_observations.resetInput()
        self.id_factorsThatPreventYou.resetInput()
        self.id_adittionalStudies.resetInput()
=======


class CaracterizacionAmpliadaScreen(Screen):
    pass
>>>>>>> ccb016423d2345f00d66a88de97a7d5fc627caea
