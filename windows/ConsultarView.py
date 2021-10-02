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

        self.id_title.text = f"Consulta del beneficiario: {query_general[1]}"
        self.id_project.text = f"Proyecto: {query_general[0]}"
        self.id_document.text = f"Documento: {query_general[4]}"
        self.id_cel.text = f'Celular: {query_general[15]}'

        if query_negocio:
            self.id_departamento.text = f"Departamento {query_negocio[1]}"

        self.to_excel.bind(on_release=self.save_to_excel)


    def save_to_excel(self, button):
        data = []
        cols = []
        tables = ['informacion_general_beneficiario', 'unidad_de_negocio', '']
        tipo_beneficiario = querys.consulta_tipo_beneficiario(self.slug, querys.idProject(
            self.project.lower()))
        if tipo_beneficiario == 1:
            # Idea para emprendedor
            tables = ['informacion_general_beneficiario',
                      'idea_de_negocio', 'diagnostico_de_perfil_productivo',
                      'caracterizacion_ampliada',
                      'caracterizacion_ampliada_informacion_hijos', 'monitoreo',
                      'plan_de_formacion', 'plan_de_implementacion', 'actividad_implementacion',
                      'plan_de_seguimiento', 'actividad_seguimiento']
        else:
            # Unidad para microEmpresario
            tables = ['informacion_general_beneficiario',
                      'unidad_de_negocio', 'diagnostico_de_perfil_productivo',
                      'caracterizacion_ampliada',
                      'caracterizacion_ampliada_informacion_hijos', 'monitoreo',
                      'plan_de_formacion', 'plan_de_implementacion', 'actividad_implementacion',
                      'plan_de_seguimiento', 'actividad_seguimiento']

        for table in tables:
            print(table)

            data_temp = self.format_dataframe(table)[0]
            if data_temp is not None:
                data.extend(data_temp)
                cols_temp = self.format_dataframe(table)[1]
                if cols_temp is not None:
                    cols.extend(cols_temp)

        data = [data,]

        df = pd.DataFrame(data, columns=cols)

        file_name = f'{self.operator}.xlsx'
        df.to_excel(file_name)
        self.id_message.text = "Excel Guardado"


    def format_dataframe(self, table):
        data = querys.consulta_beneficiario_custom(self.slug, table)
        cols = querys.bringColumns(table)
        return data, cols

    
