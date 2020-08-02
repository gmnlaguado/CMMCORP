# coding=utf-8
from flask import Flask, request
import os

app = Flask(__name__)


@app.route('/')
def index():
    return '<h1>Aplicación de la corporación mundial de la mujer en línea</h1>'


@app.route('/actividad_implementacion', methods=['POST'])
def actividad_implementacion():
    informacion = request.json
    return f'actividad_implementacion\n\n{informacion}'


@app.route('/actividad_seguimiento', methods=['POST'])
def actividad_seguimiento():
    informacion = request.json
    return f'actividad_seguimiento\n\n{informacion}'


@app.route('/beneficiario_proyectos', methods=['POST'])
def beneficiario_proyectos():
    informacion = request.json
    return f'beneficiario_proyectos\n\n{informacion}'


@app.route('/caracterizacion_ampliada', methods=['POST'])
def caracterizacion_ampliada():
    informacion = request.json
    return f'caracterizacion_ampliada\n\n{informacion}'


@app.route('/caracterizacion_ampliada_informacion_hijos', methods=['POST'])
def caracterizacion_ampliada_informacion_hijos():
    informacion = request.json
    return f'caracterizacion_ampliada_informacion_hijos\n\n{informacion}'


@app.route('/caracterizacion_ampliada_informacion_personas_a_cargo', methods=['POST'])
def caracterizacion_ampliada_informacion_personas_a_cargo():
    informacion = request.json
    return f'caracterizacion_ampliada_informacion_personas_a_cargo\n\n{informacion}'


@app.route('/diagnostico_de_perfil_productivo', methods=['POST'])
def diagnostico_de_perfil_productivo():
    informacion = request.json
    return f'diagnostico_de_perfil_productivo\n\n{informacion}'


@app.route('/diagnostico_empresarial', methods=['POST'])
def diagnostico_empresarial():
    informacion = request.json
    return f'diagnostico_empresarial\n\n{informacion}'


@app.route('/idea_de_negocio', methods=['POST'])
def idea_de_negocio():
    informacion = request.json
    return f'idea_de_negocio\n\n{informacion}'


@app.route('/informacion_general_beneficiario', methods=['POST'])
def informacion_general_beneficiario():
    informacion = request.json
    return f'informacion_general_beneficiario\n\n{informacion}'


@app.route('/monitoreo', methods=['POST'])
def monitoreo():
    informacion = request.json
    return f'monitoreo\n\n{informacion}'


@app.route('/odp_operario', methods=['POST'])
def odp_operario():
    informacion = request.json
    return f'odp_operario\n\n{informacion}'


@app.route('/odp_operario_proyectos', methods=['POST'])
def odp_operario_proyectos():
    informacion = request.json
    return f'odp_operario_proyectos\n\n{informacion}'


@app.route('/plan_de_formacion', methods=['POST'])
def plan_de_formacion():
    informacion = request.json
    return f'plan_de_formacion\n\n{informacion}'


@app.route('/plan_de_implementacion', methods=['POST'])
def plan_de_implementacion():
    informacion = request.json
    return f'plan_de_implementacion\n\n{informacion}'


@app.route('/plan_de_seguimiento', methods=['POST'])
def plan_de_seguimiento():
    informacion = request.json
    return f'plan_de_seguimiento\n\n{informacion}'


@app.route('/proyectos', methods=['POST'])
def proyectos():
    informacion = request.json
    return f'proyectos\n\n{informacion}'


@app.route('/unidad_de_negocio', methods=['POST'])
def unidad_de_negocio():
    informacion = request.json
    return f'unidad_de_negocio\n\n{informacion}'

if __name__ == "__main__":
    app.run(host= '0.0.0.0')

