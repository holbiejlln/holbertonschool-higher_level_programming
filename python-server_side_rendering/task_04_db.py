from flask import Flask, render_template, request
import json
import csv
import sqlite3

app = Flask(__name__)

# Task 3/4: Simple class to structure product data
class Product:
    def __init__(self, id, name, category, price):
        self.id = int(id)
        self.name = name
        self.category = category
        self.price = float(price)

# --- Task 3 Helper Functions (JSON/CSV) ---

def read_json_data():
    """Reads and parses data from products.json."""
    try:
        with open('products.json', 'r') as f:
            data = json.load(f)
            return [Product(**d) for d in data]
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def read_csv_data():
    """Reads and parses data from products.csv."""
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

# --- Task 4 Helper Function (SQLite) ---

def read_sql_data(product_id=None):
    """Fetches data from the SQLite database."""
    products = []
    try:
        conn = sqlite3.connect('products.db')
        conn.row_factory = sqlite3.Row  # Allows accessing columns by name
        cursor = conn.cursor()
        
        query = "SELECT id, name, category, price FROM Products"
        params = []
        
        if product_id is not None:
            query += " WHERE id = ?"
            params.append(product_id)
            
        cursor.execute(query, params)
        rows = cursor.fetchall()
        
        for row in rows:
            products.append(Product(
                id=row['id'],
                name=row['name'],
                category=row['category'],
                price=row['price']
            ))
        
    except sqlite3.Error as e:
        print(f"Database error: {e}")
        return products, str(e) # Return empty list and error message
    finally:
        if 'conn' in locals() and conn:
            conn.close()
            
    return products, None # Return list and no error

# --- Task 1/2 Routes (Kept for completeness) ---

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/items')
def items():
    try:
        with open('items.json', 'r') as f:
            data = json.load(f)
            item_list = data.get('items', [])
    except (FileNotFoundError, json.JSONDecodeError):
        item_list = []
        
    return render_template('items.html', items=item_list) 

# --- Task 3/4 Main Route ---

@app.route('/products')
def products():
    source = request.args.get('source')
    product_id_str = request.args.get('id')
    
    products_data = []
    error_message = None

    # Determine source and read data
    if source == 'json':
        products_data = read_json_data()
    elif source == 'csv':
        products_data = read_csv_data()
    elif source == 'sql':
        # New logic for SQL source
        sql_error = None
        target_id = None
        
        if product_id_str:
            try:
                target_id = int(product_id_str)
            except ValueError:
                # Handle invalid ID format for SQL
                error_message = f"Invalid ID format: '{product_id_str}'. ID must be an integer."
                return render_template(
                    'product_display.html', source=source, error=error_message
                )
        
        products_data, sql_error = read_sql_data(target_id)
        
        if sql_error:
            # Handle database errors
            error_message = f"Database Error: {sql_error}"
        elif product_id_str and not products_data:
            # Handle ID not found for SQL
            error_message = f"Product with id={target_id} not found in {source} file."
            
    else:
        # Handle invalid source edge case
        error_message = f"Wrong source: '{source}'. Must be 'json', 'csv', or 'sql'."
        return render_template(
            'product_display.html', source=source, error=error_message
        )

    # Filtering logic (only applies to JSON/CSV, as SQL filtering is done in read_sql_data)
    if source != 'sql' and product_id_str:
        try:
            target_id = int(product_id_str)
            filtered_data = [p for p in products_data if p.id == target_id]

            if not filtered_data:
                # Handle ID not found for JSON/CSV
                error_message = f"Product with id={target_id} not found in {source} file."
                
            products_data = filtered_data
        
        except ValueError:
            # Handle invalid ID format for JSON/CSV (already handled for SQL)
            error_message = f"Invalid ID format: '{product_id_str}'. ID must be an integer."
            products_data = [] # Clear data

    # Final rendering
    return render_template(
        'product_display.html',
        source=source,
        products=products_data,
        error=error_message
    )

if __name__ == '__main__':
    app.run(debug=True, port=5000)
