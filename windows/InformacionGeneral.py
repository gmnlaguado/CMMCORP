# coding=utf-8
from kivy.uix.screenmanager import Screen
from kivy.properties import ObjectProperty
from codes import snippets
from declarations import querys, class_declaration, dataFormating
from windows import DiagnosticoPerfilProductivo, IdeaDeNegocio, UnidadDeNegocio


class InformacionGeneralScreen(Screen):
    project = None
    operator = None
    payeeDocument = None
    home = False

    id_title = ObjectProperty()
    id_name = ObjectProperty()
    id_lastName = ObjectProperty()
    id_birthdate = ObjectProperty()
    id_age = ObjectProperty()
    id_ageRange = ObjectProperty()
    id_documentType = ObjectProperty()
    id_expeditionDepto = ObjectProperty()
    id_expeditionCity = ObjectProperty()
    id_sex = ObjectProperty()
    id_payeeType = ObjectProperty()
    id_nationality = ObjectProperty()
    id_country = ObjectProperty()
    id_departments = ObjectProperty()
    id_cities = ObjectProperty()
    id_environment = ObjectProperty()
    id_addressLabel = ObjectProperty()
    id_sign = ObjectProperty()
    id_address = ObjectProperty()
    id_neighborhoods = ObjectProperty()
    id_tier = ObjectProperty()
    id_telephone = ObjectProperty()
    id_gender = ObjectProperty()
    id_cellphone = ObjectProperty()
    id_cellphone2 = ObjectProperty()
    id_ethnicGroup = ObjectProperty()
    id_disability = ObjectProperty()
    id_email = ObjectProperty()
    id_message = ObjectProperty()
    id_signInButton = ObjectProperty()
    homeButton = ObjectProperty()

    def __init__(self, *args, **kwargs):
        super().__init__(**kwargs)
        self.id_title.text = "Información General"
        self.id_name.hint_text = "Nombres del beneficiario"
        self.id_lastName.hint_text = "Apellidos del beneficiario"
        self.id_addressLabel.text = "Dirección"

        self.id_name.bind(on_text_validate=self.signal)
        self.id_lastName.bind(on_text_validate=self.signal)
        self.id_address.bind(on_text_validate=self.signal)
        self.id_telephone.bind(on_text_validate=self.signal)
        self.id_cellphone.bind(on_text_validate=self.signal)
        self.id_cellphone2.bind(on_text_validate=self.signal)
        self.id_email.bind(on_text_validate=self.signal)
        self.id_signInButton.bind(on_release=self.checkAll)

        self.id_birthdate.bind(on_text_validate=self.birthdate)
        self.homeButton.bind(on_press=self.setHome)

        self.id_documentType.values = querys.parametricList('documentType')
        self.id_sex.values = querys.parametricList('sex')
        self.id_payeeType.values = querys.parametricList('payeeType')
        self.id_nationality.values = querys.parametricList('countries')
        self.id_country.values = querys.parametricList('countries')
        self.id_environment.values = querys.parametricList('environment')
        self.id_sign.values = querys.parametricList('sign')
        self.id_gender.values = querys.parametricList('gender')
        self.id_ethnicGroup.values = querys.parametricList('ethnicGroup')
        self.id_disability.values = querys.parametricList('disability')
        self.id_expeditionDepto.values = querys.bringDepartments(169)
        self.id_tier.values = [str(numb) for numb in range(1, 8)]

        self.id_country.bind(text=self.fillDepartments)
        self.id_departments.bind(text=self.fillCities)
        self.id_expeditionDepto.bind(text=self.fillCitiesExpedition)
        self.id_cities.bind(text=self.fillNeighborhoods)

    def setHome(self, *args):
        self.home = True

    def birthdate(self, *args):
        self.id_message.text = args[0].alertFlag['message']
        if args[0].alertFlag['complete']:
            age = snippets.ageCalculation(args[0].text)
            self.id_age.text = f'Edad {age}'
            if age >= 15:
                self.id_ageRange.text = querys.dataParametrics('ageRange', snippets.rangeCalculation(age))
            else:
                self.id_message.text = "El beneficiario debe tener más de 15 años"
                args[0].complete = False

    def fillDepartments(self, *args):
        self.id_message.text = ""
        id_country = querys.idParametrics('countries', args[1])
        if id_country is not None:
            self.id_departments.values = querys.bringDepartments(id_country)

    def fillCities(self, *args):
        self.id_message.text = ""
        id_department = querys.idDepartments(args[1])
        if id_department is not None:
            self.id_cities.values = querys.bringCities(id_department)

    def fillCitiesExpedition(self, *args):
        self.id_message.text = ""
        id_department = querys.idDepartments(args[1])
        if id_department is not None:
            self.id_expeditionCity.values = querys.bringCities(id_department)

    def fillNeighborhoods(self, *args):
        self.id_message.text = ""
        id_city = querys.idCities(args[1])
        if id_city is not None:
            neigh = querys.bringNeighborhoods(id_city)
            self.id_neighborhoods.values = [ne.capitalize() for ne in neigh]

    def on_pre_enter(self, *args):
        self.id_documentType.text = "Tipo de documento"
        self.id_expeditionDepto.text = "Depto. Expedición"
        self.id_expeditionCity.text = "Ciudad Expedición"
        self.id_sex.text = "Sexo"
        self.id_payeeType.text = "Tipo"
        self.id_nationality.text = "Nacionalidad"
        self.id_country.text = "País"
        self.id_departments.text = "Departamento"
        self.id_cities.text = "Ciudad"
        self.id_environment.text = "Entorno"
        self.id_sign.text = "Rótulo"
        self.id_neighborhoods.text = "Barrio"
        self.id_tier.text = "Estrato"
        self.id_gender.text = "Género"
        self.id_ethnicGroup.text = "Etnia"
        self.id_disability.text = "Cond. Discapacidad"

        self.id_name.resetInput()
        self.id_lastName.resetInput()
        self.id_birthdate.resetInput()
        self.id_address.resetInput()
        self.id_telephone.resetInput()
        self.id_cellphone.resetInput()
        self.id_cellphone2.resetInput()
        self.id_email.resetInput()

        self.home = False

    def on_leave(self, *args):
        if not self.home:
            information = self
            DiagnosticoPerfilProductivo.DiagnosticoPerfilProductivoScreen.payeeDocument = self.payeeDocument
            DiagnosticoPerfilProductivo.DiagnosticoPerfilProductivoScreen.payeeType = self.id_payeeType.text
            if self.id_payeeType.text == "Emprendedor":
                IdeaDeNegocio.IdeaDeNegocioScreen.payeeDocument = self.payeeDocument
                IdeaDeNegocio.IdeaDeNegocioScreen.operator = self.operator
                IdeaDeNegocio.IdeaDeNegocioScreen.project = self.project
            else:
                UnidadDeNegocio.UnidadDeNegocioScreen.payeeDocument = self.payeeDocument
                UnidadDeNegocio.UnidadDeNegocioScreen.operator = self.operator
                UnidadDeNegocio.UnidadDeNegocioScreen.project = self.project

            dataFormating.GeneralInformationData(information)

    def signal(self, *args):
        self.id_message.text = args[0].alertFlag['message']

    def checkAll(self, *args):
        self.id_message.text = ""
        children_list = self.children[0].children
        ret = snippets.chekingCompletes(children_list)
        if not ret:
            msg = "Formulario Incompleto"
        else:
            msg = ""
        self.id_message.text = msg
        if msg == "":
            AcceptForm(self.operator).open()


class AcceptForm(class_declaration.PopupFather):
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
