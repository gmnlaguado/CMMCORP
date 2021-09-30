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
    id_title = ObjectProperty()
    slug = ObjectProperty()
    id_project = ObjectProperty()
    id_departamento = ObjectProperty()
    back = ObjectProperty()

    def on_pre_enter(self, *args):
        
        query_general = querys.consulta_beneficiario(self.slug, querys.idProject(
            self.project.lower()), "informacion_general_beneficiario")
        
        query_negocio = querys.consulta_beneficiario(self.slug, querys.idProject(
            self.project.lower()), "idea_de_negocio")

        self.id_title.text = f"Consulta del beneficiario {query_general[1]} {query_general[2]}"
        self.id_project.text = f"Proyecto{query_general[0]}"

        if query_negocio:
            self.id_departamento.text = f"Departamento {query_negocio[1]}"

        self.back.bind(on_release=self.save_to_excel)

    def change_screen(self, button):
        app = App.get_running_app()
        app.change_screen('Panel')

    def save_to_excel(self, button):
        general = querys.consulta_beneficiario(self.slug, querys.idProject(
            self.project.lower()), "informacion_general_beneficiario")
        data = [
            {
                'Empresa': general[0],
                'Nombre': general[1],
            }
        ]
        df = pd.DataFrame(data)
        file_name = f'{self.id_title.text}.xlsx'

        df.to_excel(file_name)
