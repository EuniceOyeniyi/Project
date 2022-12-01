from flask import Flask, render_template


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

@app.route("/demo")
def demo():
    return("Welcome\n Now")
    

if __name__ == "__main__":
    app.run(debug=True)
