from flask import Flask, render_template, request, redirect, session, flash
import re

app = Flask(__name__)
app.secret_key = 'ThisIsAKeyBoy'

@app.route('/')
def main():
    return render_template('index.html')

@app.route('/result', methods=['POST'])
def submit():
    if len(request.form['name']) < 1:
        for key in session.keys():
            session.pop[key]
        flash('Name cannot be empty!')
        return render_template('index.html')
    if len(request.form['comment']) < 1:
        for key in session.keys():
            session.pop[key]
        flash('Comment section cannot be empty!')
        return render_template('index.html')
    if len(request.form['comment']) > 120:
        for key in session.keys():
            session.pop[key]
        flash('Comment section cannot be more than 120 characters!')
        return render_template('index.html')
    else:
        return render_template('result.html', name = request.form['name'], location = request.form['location'], language = request.form['language'], comment = request.form['comment'])

@app.route('/back')
def back():
    return render_template('index.html')

app.run(debug = True)