# coding=utf-8
from kivy.uix.screenmanager import Screen
from kivy.properties import ObjectProperty
from codes import snippets
from declarations import querys, class_declaration, dataFormating
from windows import DiagnosticoPerfilProductivo
from kivy.app import App
import pandas as pd

class ConsultarScreen(Screen):
    project = None
    operator = None
    payeeDocument = None
    home = False
    id_homeButton = ObjectProperty()
    id_title = ObjectProperty()
    slug = ObjectProperty()
    id_project = ObjectProperty()
    id_departamento = ObjectProperty()
    id_document = ObjectProperty()
    id_cel = ObjectProperty()
    id_message = ObjectProperty()
    to_excel = ObjectProperty()

    def on_pre_enter(self, *args):
        
        query_general = querys.consulta_beneficiario(self.slug, querys.idProject(
            self.project.lower()), "informacion_general_beneficiario")
        
        query_negocio = querys.consulta_beneficiario(self.slug, querys.idProject(
            self.project.lower()), "idea_de_negocio")

        self.id_title.text = f"Consulta del beneficiario: {query_general[1]} {query_general[2]}"
        self.id_project.text = f"Proyecto: {query_general[0]}"
        self.id_document.text = f"Documento: {query_general[4]}"
        self.id_cel.text = f'Celular: {query_general[15]}'

        if query_negocio:
            self.id_departamento.text = f"Departamento {query_negocio[1]}"

        self.to_excel.bind(on_release=self.save_to_excel)


    def save_to_excel(self, button):
        general = querys.consulta_beneficiario(self.slug, querys.idProject(
            self.project.lower()), "informacion_general_beneficiario")
        columns = ['Proyecto', 'Nombre', 'Apellido', 'Tipo Doc', 'Documento', 'Expedida en', 'Nacimiento', 'Ciudad',
        'Departamento', 'Pais',	'Sign', 'Dirección', 'Vecindario', 'Indicativo', 'Telefono', 'Celular', 'Email',
        'Operador',	'Cel 2', 'PayeeType', 'Fecha', 'Rango edad', 'Nacionalidad', 'Entorno', 'Tier', 'Sexo',
        'Genero', 'Grupo Etnico', 'Discapacidad']
        
        columns_original = ["project", "names", "lastNames", "docType", "document", "expeditionCity", "birthdate", "city", 
        "department", "country", "sign", "address", "neighborhood", "indicative","telephone", "cellphone", "email",
        "operator", "cellphone2", "payeeType", "date", "ageRange", "nationality", "environment", "tier", "sex", 
        "gender", "ethnicGroup", "disability"]

        general = [general,]
        df = pd.DataFrame(general, columns=columns)
        file_name = f'{self.id_title.text}.xlsx'
        self.id_message.text = "Excel Guardado"
        df.to_excel(file_name)
