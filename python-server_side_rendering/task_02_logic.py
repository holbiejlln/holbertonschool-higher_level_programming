from flask import Flask, render_template
import json

app = Flask(__name__)

# Route from Task 1 (Kept for completeness)
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')


# New Route for Task 2
@app.route('/items')
def items():
    # 1. Read and parse the JSON data
    try:
        with open('items.json', 'r') as f:
            data = json.load(f)
            # Ensure the structure is correct and get the list
            item_list = data.get('items', [])
    except FileNotFoundError:
        item_list = [] # Handle case where file is missing
    except json.JSONDecodeError:
        item_list = [] # Handle case where JSON is invalid

    # 2. Pass the list to the template
    return render_template('items.html', items=item_list)

if __name__ == '__main__':
    # Ensure port 5000 is used
    app.run(debug=True, port=5000)
