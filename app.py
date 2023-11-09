from flask import Flask

app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
    return "<h1>Say Hi to flask</h1>"

@app.route('/about')
def about():
    return "<h1>This is a about page.</h1>"

@app.route('/contact')
def contact():
    return "<h1>This is a contact page.</h1>"

@app.route('/names/<name>')
def nameing(name):
    return f"Welcome {name.upper()}"

if __name__=='__main__':
    app.run(debug=True)
    
