# coding=utf-8
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
import utilidades
from kivy.uix.spinner import Spinner


class Label_352_40(Label):
    def __init__(self, *args, **kwargs):
        super().__init__(**kwargs)
        self.font_size = 30
        self.font_name = "montserrat"
        self.color = 0, 0, 0, 1
        self.size_hint = None, None
        self.size = 352, 40
        self.text_size = 352, 40
        self.halign = "left"
        self.valign = "middle"
        self.class_type = "label"


class Input_352_64(TextInput):
    def __init__(self, *args, **kwargs):
        super().__init__(**kwargs)
        self.padding = 10
        self.font_size = 24
        self.font_name = "montserrat"
        self.color = 0, 0, 0, 1
        self.size_hint = None, None
        self.size = 352, 64
        self.halign = "center"
        self.valign = "middle"
        self.background_color = 1, 1, 1, 1
        self.background_normal = ''
        self.multiline = False
        self.password = False
        self.complete = False
        self.class_type = "input"
        self.text_type = "usuario"

    def on_text_validate(self):
        if self.text_type == "usuario" or self.text_type == "contrasena":
            if utilidades.Comprobaciones.password(self.text):
                self.background_color = 7 / 255, 7 / 255, 7 / 255, 0.1
                self.complete = True


class Spinner_352_40(Spinner):
    def __init__(self, *args, **kwargs):
        super().__init__(**kwargs)
        self.font_size = 24
        self.font_name = "montserrat"
        self.color = 1, 1, 1, 1
        self.text_size = 352, 40
        self.size_hint = None, None
        self.size = 352, 40
        self.halign = "center"
        self.valign = "middle"
        self.background_color = 61 / 255, 119 / 255, 0 / 255, 0.7
        self.background_normal = 'images/dropdown.png'
        self.complete = False
        self.class_type = "spinner"

    def on_text(self):
        pass
