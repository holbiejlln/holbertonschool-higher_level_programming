from flask import Flask, render_template, request
import json
import csv
from io import StringIO

app = Flask(__name__)

# --- Helper Functions for Data Reading ---

def read_json_data():
    """Reads and parses data from products.json."""
    try:
        with open('products.json', 'r') as f:
            data = json.load(f)
            # Convert list of dicts to list of simple objects (or dicts)
            return [Product(**d) for d in data]
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        return []

def read_csv_data():
    """Reads and parses data from products.csv."""
    data = []
    try:
        # Use StringIO to treat string content as a file
        with open('products.csv', 'r', newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                # Convert 'id' and 'price' to appropriate types
                try:
                    product = Product(
                        id=int(row['id']),
                        name=row['name'],
                        category=row['category'],
                        price=float(row['price'])
                    )
                    data.append(product)
                except (ValueError, KeyError):
                    # Skip invalid rows
                    continue
        return data
    except FileNotFoundError:
        return []

# Simple class to make accessing data in the template cleaner (e.g., product.name)
class Product:
    def __init__(self, id, name, category, price):
        self.id = id
        self.name = name
        self.category = category
        self.price = price

# --- Main Route ---

@app.route('/products')
def products():
    # 1. Get query parameters
    source = request.args.get('source')
    product_id_str = request.args.get('id')
    
    products_data = []
    error_message = None

    # 2. Validate source and read data
    if source == 'json':
        products_data = read_json_data()
    elif source == 'csv':
        products_data = read_csv_data()
    else:
        # Handle invalid source edge case
        error_message = f"Wrong source: '{source}'. Must be 'json' or 'csv'."
        return render_template(
            'product_display.html',
            source=source,
            error=error_message,
            products=None
        )

    # 3. Implement ID Filtering
    if product_id_str:
        try:
            target_id = int(product_id_str)
            filtered_data = [p for p in products_data if p.id == target_id]

            if not filtered_data:
                # Handle product not found edge case
                error_message = f"Product with id={target_id} not found in {source} file."
                
            products_to_display = filtered_data
        
        except ValueError:
            # Handle invalid ID format
            error_message = f"Invalid ID format: '{product_id_str}'. ID must be an integer."
            products_to_display = None
            
    else:
        # Display all products if no ID is specified
        products_to_display = products_data

    # 4. Render template with data or error
    return render_template(
        'product_display.html',
        source=source,
        products=products_to_display,
        error=error_message
    )

if __name__ == '__main__':
    app.run(debug=True, port=5000)from flask import Flask, render_template, request
import json
import csv
from io import StringIO

app = Flask(__name__)

# --- Helper Functions for Data Reading ---

def read_json_data():
    """Reads and parses data from products.json."""
    try:
        with open('products.json', 'r') as f:
            data = json.load(f)
            # Convert list of dicts to list of simple objects (or dicts)
            return [Product(**d) for d in data]
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        return []

def read_csv_data():
    """Reads and parses data from products.csv."""
    data = []
    try:
        # Use StringIO to treat string content as a file
        with open('products.csv', 'r', newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                # Convert 'id' and 'price' to appropriate types
                try:
                    product = Product(
                        id=int(row['id']),
                        name=row['name'],
                        category=row['category'],
                        price=float(row['price'])
                    )
                    data.append(product)
                except (ValueError, KeyError):
                    # Skip invalid rows
                    continue
        return data
    except FileNotFoundError:
        return []

# Simple class to make accessing data in the template cleaner (e.g., product.name)
class Product:
    def __init__(self, id, name, category, price):
        self.id = id
        self.name = name
        self.category = category
        self.price = price

# --- Main Route ---

@app.route('/products')
def products():
    # 1. Get query parameters
    source = request.args.get('source')
    product_id_str = request.args.get('id')
    
    products_data = []
    error_message = None

    # 2. Validate source and read data
    if source == 'json':
        products_data = read_json_data()
    elif source == 'csv':
        products_data = read_csv_data()
    else:
        # Handle invalid source edge case
        error_message = f"Wrong source: '{source}'. Must be 'json' or 'csv'."
        return render_template(
            'product_display.html',
            source=source,
            error=error_message,
            products=None
        )

    # 3. Implement ID Filtering
    if product_id_str:
        try:
            target_id = int(product_id_str)
            filtered_data = [p for p in products_data if p.id == target_id]

            if not filtered_data:
                # Handle product not found edge case
                error_message = f"Product with id={target_id} not found in {source} file."
                
            products_to_display = filtered_data
        
        except ValueError:
            # Handle invalid ID format
            error_message = f"Invalid ID format: '{product_id_str}'. ID must be an integer."
            products_to_display = None
            
    else:
        # Display all products if no ID is specified
        products_to_display = products_data

    # 4. Render template with data or error
    return render_template(
        'product_display.html',
        source=source,
        products=products_to_display,
        error=error_message
    )

if __name__ == '__main__':
    app.run(debug=True, port=5000)
