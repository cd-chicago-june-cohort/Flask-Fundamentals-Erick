from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = "ThisAIsKey"

@app.route('/')
def main():
    if 'counter' not in session:
        session['counter'] = 1
    else:
        session['counter'] += 1
    return render_template('index.html', counter=session['counter'])

@app.route('/reload')
def reload():
    session['counter'] += 1
    return redirect('/')

@app.route('/reset')
def reset():
    session['counter'] = 0
    return redirect('/')

app.run(debug = True)