import os

from flask import Flask, jsonify, render_template, request
from flask_wtf import FlaskForm
from wtforms import SubmitField, TextAreaField

# Typically in a production setting, this file would be divided up into multiple files
# I kept it as one file to demonstrate how different things work together for simplicity


app = Flask(__name__)
# SECRET_KEY is required for generation of wtforms CSRF tokens
app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY") or "your secret key"


class TextForm(FlaskForm):
    text = TextAreaField("Text Area Field")
    submit = SubmitField("Submit Text")


@app.route("/", methods=["GET", "POST"])
def index():
    form = TextForm()
    if request.method == "POST":
        if form.validate_on_submit():
            return jsonify(data={"you typed": form.text.data})
        else:
            return jsonify(data=form.errors)
    return render_template("index4.html", form=form)


app.run(host="127.0.0.1", port=5000)