from flask import Flask

app =  Flask(__name__)

@app.route("/")

def ola_mundo():
    return "<h1>Olá Mundo!!!!!</h1>"

app.run(debug=True)