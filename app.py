import os

import openai
from flask import Flask, redirect, render_template, request, url_for

app = Flask(__name__)
openai.api_key = os.getenv("OPENAI_API_KEY")


@app.route("/", methods=("GET", "POST"))
def index():
    if request.method == "POST":
        President = request.form["President"]
        response = openai.Completion.create(
            model="text-davinci-003",
            prompt=generate_prompt(President),
            temperature=0.6
        )
        return redirect(url_for("index", result=response.choices[0].text))

    result = request.args.get("result")
    return render_template("index.html", result=result)


def generate_prompt(President):
    return """Find names and year for US presidents.

President: 1
Names: George Washington, year April 30 1789 to March 4 1797
President: 2
Names: John Adams, year March 4 1797 to March 4 1801
President: {}
Names:""".format(
        President.capitalize()
    )
