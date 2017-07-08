from flask import Flask, render_template, request, redirect, session
import random
import time

app = Flask(__name__)
app.secret_key = ('ThisIsMyKey')

@app.route('/')
def main():
    if 'gold' not in session:
        session['gold'] = 0
    else:
        session['gold'] += 0
    if 'place' not in session:
        session['place'] = ''
    else:
        session['place'] += ''
    return render_template('index.html', currentGold = session['gold'], outcome = session['place'])

@app.route('/process_money', methods =['POST'])
def process():
    giveOrTake = random.randint(0, 1)
    if request.form['building'] == 'farm':
        farm = random.randint(10, 20)
        session['place'] = 'Earned ' + str(farm) + ' golds from the farm! ' + '(' + time.ctime() + ')'
        session['gold'] += farm
    elif request.form['building'] == 'cave':
        farm = random.randint(5, 10)
        session['place'] = 'Earned ' + str(farm) + ' golds from the cave! ' + '(' + time.ctime() + ')'
        session['gold'] += farm
    elif request.form['building'] == 'house':
        farm = random.randint(2, 5)
        session['place'] = 'Earned ' + str(farm) + ' golds from the house! ' + '(' + time.ctime() + ')'
        session['gold'] += farm
    elif request.form['building'] == 'casino':
        if giveOrTake == 0:
            farm = random.randint(0, 50)
            session['place'] = 'Entered a casino and lost ' + str(farm) + ' golds...Ouch.. ' + '(' + time.ctime() + ')'
            session['gold'] -= farm
        else:
            farm = random.randint(0, 50)
            session['place'] = 'Entered a casino and won ' + str(farm) + ' golds! ' + '(' + time.ctime() + ')'
            session['gold'] += farm
    return redirect('/')
app.run(debug = True)
