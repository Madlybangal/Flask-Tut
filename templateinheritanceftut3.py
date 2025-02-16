from flask import Flask,render_template,request,jsonify
import pickle

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('template_inheritanceindex.html')

@app.route('/about')
def about():
    return render_template('template_inheritanceabout.html')
@app.route('/profile/<string:name>')
def profile(name):
    return "Hello" +str(name)

@app.route('/profile/<int:id>')
def profile2(id):
    return "Your requested user with id " + str(id)


if __name__ == "__main__":
    app.run(debug=True)
