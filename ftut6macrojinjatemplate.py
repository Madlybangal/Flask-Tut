from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    items = [
        {'title': 'Item 1', 'description': 'Description for item 1', 'price': 10.00},
        {'title': 'Item 2', 'description': 'Description for item 2', 'price': 20.00},
        {'title': 'Item 3', 'description': 'Description for item 3', 'price': 30.00},
    ]
    return render_template('macro_main.html', items=items)

if __name__ == '__main__':
    app.run(debug=True)