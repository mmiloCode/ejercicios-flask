from flask import Flask, render_template, url_for, request

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/tablas-multiplicar", methods = ['GET', 'POST'])
def tablasMultiplicar():

    number = 0
    tabla = list(range(1, 11))

    if request.method == 'POST' :
        number = int(request.form['number'])

    return render_template("tablas-multiplicar.html",
                           number = number,
                           tabla = tabla)



