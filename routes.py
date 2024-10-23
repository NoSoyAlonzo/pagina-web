from flask import Blueprint, render_template, request
from singleton_db import SingletonDB

# Instancia de Flask Blueprint
routes = Blueprint('routes', __name__)

# Ruta para mostrar las categorías
@routes.route('/')
def index():
    db = SingletonDB('mysql+pymysql://root:Alonso181437@localhost:3306/generador_nombres')
    categories = db.get_all_categories()
    return render_template('index.html', categories=categories)

# Ruta para generar nombres basados en la categoría seleccionada
@routes.route('/generate', methods=['POST'])
def generate_name():
    db = SingletonDB('mysql+pymysql://user:password@localhost/nombre_db')
    category_id = request.form.get('category_id')
    keyword = request.form.get('keyword')
    
    prefixes = db.get_prefixes_by_category_id(category_id)
    suffixes = db.get_suffixes_by_category_id(category_id)
    
    # Lógica para generar nombres basados en prefijos, sufijos y palabra clave
    generated_names = []
    for prefix in prefixes:
        for suffix in suffixes:
            name = f"{prefix.prefix}{keyword}{suffix.suffix}"
            generated_names.append(name)
    
    return render_template('results.html', names=generated_names)
