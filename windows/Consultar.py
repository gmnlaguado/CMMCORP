# coding=utf-8
from kivy.properties import ObjectProperty
from pywin.mfc.object import Object
from kivy.metrics import dp
from kivy.app import App
from kivymd.uix.datatables import MDDataTable
import sqlite3
import pandas as pd
import pymssql
from flask import Flask, request
from declarations import class_declaration, querys, dataFormating
from kivy.uix.spinner import Spinner
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.checkbox import CheckBox
from kivy.uix.button import Button
from kivy.uix.screenmanager import Screen
from declarations.querys import MyDB
from windows import Monitoreo


class ConsultarScreen(Screen):
            project = None
            operator = None
            payeeDocument = None
            home = False
            fecha = None

            id_title = ObjectProperty()
            id_document = ObjectProperty()
            id_FechaDiagnostico = ObjectProperty()
            id_operator = ObjectProperty()
            id_Project = ObjectProperty()
            id_Names = ObjectProperty()
            id_lastNames = ObjectProperty()
            id_docType = ObjectProperty()
            id_expeditionCity = ObjectProperty()
            id_city = ObjectProperty()
            id_birthdate = Object()
            id_address = ObjectProperty()
            id_country = ObjectProperty()
            id_department = ObjectProperty()
            id_sign = ObjectProperty()
            id_ageRange = ObjectProperty()
            id_environment = ObjectProperty()
            id_indicative = ObjectProperty()
            id_telephone = ObjectProperty()
            id_cellphone = ObjectProperty()
            id_email = ObjectProperty()
            id_sex = ObjectProperty()
            id_gender = ObjectProperty()
            id_tier = ObjectProperty()
            id_disability = ObjectProperty()
            id_ethnicGroup = ObjectProperty()

            def build(self):
                db = MyDB('register')
                cols = db.Column.values
                values = db.values

                self.datatables = MyDB(
                    size_hint =(0.9, 0.6),
                    use_pagination = True,
                    column_data =[
                        (col, dp(30))
                        for col in cols
                    ],
                    row_data = values
                )
                self.datatables.bind(on_row_press=self.on_row_press)
                self.datatables.bind(on_check_press=self.on_check_press)

            def on_start(self):
                self.datatables.open()

            def on_row_press(self,instance_table, instance_row):
                print(instance_table,instance_row)

            def on_check_press(self, instance_table, current_row):
                print(instance_table,current_row)
