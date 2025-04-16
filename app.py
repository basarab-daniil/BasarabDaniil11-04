from flask import Flask, render_template, redirect, url_for, request
import pandas as pd

# inizializza l'app Flask
app = Flask(__name__)
lista=[]

# rotta principale
@app.route('/')
def home():
    return render_template('index.html', lista=lista)

@app.route("/modifica", methods=["GET", "POST"])
def modifica():
    if request.method == "POST":
        valore=request.form["valore"]
        lista.append(valore)
    return redirect(url_for('home')) 

# avvio dell'app Flask
if __name__ == '__main__':
    app.run(debug=True)