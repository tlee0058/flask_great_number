
from flask import Flask, render_template, redirect, request, session
app = Flask(__name__)
app.secret_key="secret"

@app.route('/')
def index():
    import random
    session['randNum'] = random.randrange(0, 101)
    return render_template("index.html", number=session['number'])


@app.route('/guess', methods=['POST'])
def guess():

    guess = int(request.form['number'])
    rNum = session['randNum']
    
    return render_template("result.html", guess = guess, rNum = rNum)

@app.route('/playAgain', methods=['POST'])
def playAgain():
    
    return redirect('/')

app.run(debug=True)