import time
from flask import Flask, render_template, request
from musicapp import *


app = Flask(__name__)

@app.route("/")
def index():
    return render_template('home.html')

@app.route("/about")
def about():
    return render_template('about.html')

@app.route("/project")
def projects():
    return render_template('projects.html')

@app.route("/demo", methods=['GET', 'POST'])
def demo():
    if request.method == 'POST':
        
        control.get_commands()
        return render_template('demo.html')
    else:        
        return render_template('demo.html')
    
    
    

if __name__ == "__main__":
    app.run(debug=True)
