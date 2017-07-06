from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def helloWord():
    return render_template('helloWorld.html')

app.run(debug = True)
