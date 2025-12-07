from flask import Flask, render_template, request
import json
import csv

app = Flask(__name__)

# Task 3: Verilənləri təmiz saxlamaq üçün sadə sinif
class Product:
    def __init__(self, id, name, category, price):
        self.id = int(id)
        self.name = name
        self.category = category
        self.price = float(price)

# Task 3: JSON oxuma funksiyası
def read_json_data():
    try:
        with open('products.json', 'r') as f:
            data = json.load(f)
            # Sözlükləri Product obyektlərinə çevirir
            return [Product(**d) for d in data]
    except (FileNotFoundError, json.JSONDecodeError):
        return []

# Task 3: CSV oxuma funksiyası
def read_csv_data():
    data = []
    try:
        with open('products.csv', 'r', newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                try:
                    data.append(Product(**row))
                except (ValueError, KeyError):
                    continue
        return data
    except FileNotFoundError:
        return []

# --- Task 1 Routes ---
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

# --- Task 2 Route ---
@app.route('/items')
def items():
    try:
        with open('items.json', 'r') as f:
            data = json.load(f)
            item_list = data.get('items', [])
    except (FileNotFoundError, json.JSONDecodeError):
        item_list = []
        
    # 'items.html' yoxdursa, onu da yaratmalısınız!
    return render_template('items.html', items=item_list) 

# --- Task 3 Route ---
@app.route('/products')
def products():
    source = request.args.get('source')
    product_id_str = request.args.get('id')
    
    products_data = []
    error_message = None

    # Mənbəni yoxlamaq
    if source == 'json':
        products_data = read_json_data()
    elif source == 'csv':
        products_data = read_csv_data()
    else:
        # Hata 1: Yanlış mənbə
        error_message = f"Wrong source: '{source}'. Must be 'json' or 'csv'."
        return render_template(
            'product_display.html',
            source=source,
            error=error_message,
            products=None
        )

    products_to_display = products_data

    # ID ilə filterləmə
    if product_id_str:
        try:
            target_id = int(product_id_str)
            filtered_data = [p for p in products_data if p.id == target_id]

            if not filtered_data:
                # Hata 2: ID tapılmadı
                error_message = f"Product with id={target_id} not found in {source} file."
                products_to_display = None
            else:
                products_to_display = filtered_data
        
        except ValueError:
            # Hata 3: ID formatı səhvdir
            error_message = f"Invalid ID format: '{product_id_str}'. ID must be an integer."
            products_to_display = None
            
    # Şablonu render etmək
    return render_template(
        'product_display.html',
        source=source,
        products=products_to_display,
        error=error_message
    )

if __name__ == '__main__':
    app.run(debug=True, port=5000)
