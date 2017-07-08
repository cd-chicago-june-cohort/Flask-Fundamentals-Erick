from flask import Flask, render_template, request, redirect, session
import random

app = Flask(__name__)
app.secret_key = ('ThisIsARandomKey')


@app.route('/')
def main():
    session['randomNum'] = random.randrange(1, 101)
    return render_template('index.html')

@app.route('/guess', methods=['POST'])
def guess():
    session['guess'] = int(request.form['guess'])
    print session['guess']
    print session['randomNum']
    if(session['guess'] == session['randomNum']):
        return render_template('newGame.html', guessNum = str(session['randomNum']) + ' was the number!')
    elif(session['guess'] < session['randomNum']):
        return render_template('guess.html', guessNum = 'Too low!')
    elif(session['guess'] > session['randomNum']):
        return render_template('guess.html', guessNum = 'Too high!')
@app.route('/winner')
def winner():
    return redirect('/')
app.run(debug = True)

