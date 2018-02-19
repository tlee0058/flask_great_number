
from flask import Flask, render_template, redirect, request, session
app = Flask(__name__)
app.secret_key="secret"

@app.route('/')
def index():
    return render_template("index.html")


@app.route('/guess', methods=['POST'])
def guess():
    import random
    session['randNum'] = random.randrange(0, 101)

    guess = int(request.form['number'])
    rNum = session['randNum']

    return redirect ('/result')            
    
@app.route('/result')
def result():
    return render_template("result.html", guess = int(request.form['number']), rNum = session['randNum'])

app.run(debug=True)