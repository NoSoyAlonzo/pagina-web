from flask import Flask, render_template, request
from singleton_db import SingletonDB

app = Flask(__name__)
db_instance = SingletonDB()

@app.route('/')
def index():
    categories = db_instance.get_all_categories()
    return render_template('index.html', categories=categories)

@app.route('/generate_names', methods=['POST'])
def generate_names():
    keyword = request.form.get('keyword')
    category_id = request.form.get('category')
    generated_names = db_instance.generate_names_by_category(keyword, category_id)
    return render_template('index.html', categories=db_instance.get_all_categories(), generated_names=generated_names)

if __name__ == '__main__':
    app.run(debug=True)
