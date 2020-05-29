
import json
from flask import Flask, render_template, request, flash

app = Flask(__name__)

#below line is secret key for flash
app.secret_key = 'some_secret'

@app.route("/")
def index():
    data = []
    with open("data/list.json","r") as list_json_data:
        data = json.load(list_json_data)
    return render_template("index.html",first = data)


@app.route("/about")
def about():
    data = []
    with open("data/cont.json", "r") as json_data:
        data = json.load(json_data)
    return render_template("about.html",cont = data)

@app.route("/about/<item_name>")
def about_item(item_name):
    page = {}

    with open("data/cont.json", "r") as json_data:
        data = json.load(json_data)
        for obj in data:
            if obj["name"] == item_name:
                page = obj
    return render_template("new-page.html", page=page)


@app.route("/sale")
def sale():
    data = []
    with open ("data/list.json", "r") as json_data:
        data = json.load(json_data)

    return render_template("sale.html",ab = data)


@app.route("/contact", methods=['GET','POST'])
def contact():
    if request.method == "POST":
        flash("Thanks {}, we recived your message".format(request.form["name"]))

    return render_template("contact.html")


@app.route("/detail1")
def detail1():
    return render_template("detail1.html")

@app.route("/detail2")
def detail2():
    return render_template("detail2.html")

@app.route("/detail3")
def detail3():
    return render_template("detail3.html")
