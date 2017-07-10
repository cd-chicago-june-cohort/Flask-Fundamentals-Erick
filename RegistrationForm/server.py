from flask import Flask, render_template, request, redirect, session, flash
import re


EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

app = Flask(__name__)
app.secret_key = ('ThisIsMyKey')

@app.route('/')
def main():
    return render_template('index.html')

@app.route('/process', methods = ['POST'])
def process():
    if len(request.form['email']) < 1:
        flash('Please enter an email!')
        return redirect('/')
    elif not EMAIL_REGEX.match(request.form['email']):
        flash("Please enter a valid email!")
        return redirect('/')
    if request.form['firstName'].isalpha() == False:
        flash('Please enter a valid first name!')
        return redirect('/')
    if len(request.form['lastName']) < 1:
        flash('Please enter a last name!')
        return redirect('/')
    if len(request.form['password']) < 1:
        flash('Please enter a password!')
        return redirect('/')
    elif len(request.form['password']) < 8:
        flash('Please enter a password with more than 8 characters')
        return redirect('/')
    if len(request.form['confirmPassword']) < 1:
        flash('Please confirm the password!')
        return redirect('/')
    if request.form['password'] != request.form['confirmPassword']:
        flash('Please make sure that both passwords match!')
        return redirect('/')
    else:
        flash("Form successfuly submitted!")
        return redirect('/')
app.run(debug = True)