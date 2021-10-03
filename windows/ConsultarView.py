# coding=utf-8
from kivy.uix.screenmanager import Screen
from kivy.properties import ObjectProperty
from codes import snippets
from declarations import querys, class_declaration, dataFormating
from windows import DiagnosticoPerfilProductivo
from kivy.app import App
import pandas as pd
import os

class ConsultarScreen(Screen):
    project = None
    operator = None
    payeeDocument = None
    home = False
    id_homeButton = ObjectProperty()
    id_title = ObjectProperty()
    id_payeeName = ObjectProperty()
    id_project = ObjectProperty()
    id_departamento = ObjectProperty()
    id_document = ObjectProperty()
    id_cel = ObjectProperty()
    id_message = ObjectProperty()
    to_excel = ObjectProperty()

    def on_pre_enter(self, *args):
        
        self.query_general = querys.consulta_beneficiario_custom(self.payeeDocument, "informacion_general_beneficiario")

        self.query_negocio = querys.consulta_beneficiario_custom(self.payeeDocument, "idea_de_negocio")

        self.id_title.text = "Consulta beneficiario"
        self.id_payeeName.text = f"Beneficiario: {self.query_general[1]}"
        self.id_project.text = f"Proyecto: {self.query_general[0]}"
        self.id_document.text = f"Documento: {self.query_general[4]}"
        self.id_cel.text = f'Celular: {self.query_general[15]}'

        if self.query_negocio:
            self.id_departamento.text = f"Departamento: {self.query_negocio[1]}"

        self.to_excel.bind(on_release=self.save_to_excel)


    def save_to_excel(self, button):
        excel_folder = os.path.join(os.environ["HOMEPATH"], "Desktop")
        file_name = f'{self.query_general[1]}.xlsx'
        full_path = os.path.join(excel_folder, file_name)
        data = []
        cols = []
        tables = querys.lista_de_tablas()

        for table in tables:
            data_temp, cols_temp = self.format_dataframe(table)
            if data_temp is not None:
                data.extend(data_temp)
                cols.extend(cols_temp)

        data = [data,]
        df = pd.DataFrame(data, columns=cols)
        df.to_excel(full_path)

        self.id_message.text = f"Excel Guardado en '{full_path}"

    def format_dataframe(self, table):
        data = querys.consulta_beneficiario_custom(self.payeeDocument, table)
        cols = querys.bringColumns(table)
        return data, cols

    
