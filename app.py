from flask import Flask, render_template, request

app = Flask(__name__)

carros = []
catalogo_carros = []

@app.route("/")
def principal():
    return render_template("index.html")

@app.route("/catalogo", methods=["GET", "POST"])
def catalogo():
    if request.method =="POST":
        if request.form.get("carro"):
            carros.append(request.form.get("carro"))
    return render_template("catalogo.html", carros=carros)

@app.route("/catalogo_completo", methods=["GET", "POST"])
def catalogo_completo():
    if request.method == "POST":
        if request.form.get("carro") and request.form.get("modelo") and request.form.get("ano"):
            catalogo_carros.append({"carro":request.form.get("carro"),"modelo":request.form.get("modelo"), "ano":request.form.get("ano"),})
    return render_template("catalogo_completo.html", catalogo_carros=catalogo_carros)

@app.route("/contatos", methods=["GET", "POST"])
def contatos():
    if request.method =="POST":
        if request.form.get("carro") and request.form.get("modelo") and request.form.get("ano"):
            catalogo_carros.append({"carro":request.form.get("carro"),"modelo":request.form.get("modelo"), "ano":request.form.get("ano"),})
    return render_template("contatos.html", catalogo_carros=catalogo_carros)

if __name__ == "__main__":
    app.run(debug=True)