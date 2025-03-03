from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    items = [
        {'name': 'Item 1', 'description': 'Description for Item 1'},
        {'name': 'Item 2', 'description': 'Description for Item 2'},
        {'name': 'Item 3', 'description': 'Description for Item 3'},
    ]
    return render_template('macro_index.html', items=items)

if __name__ == '__main__':
    app.run(debug=True)