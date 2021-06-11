import requests

from flask import Flask, jsonify, render_template, request

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/convert", methods=["POST"])
def convert():

    # Query for currency exchange rate
    currency = request.form.get("currency")
    #print ( f"currency: {currency}" )
    res = requests.get("https://open.exchangerate-api.com/v6/latest")
    #print (f"request: {res}")

    # Make sure request succeeded
    if res.status_code != 200:
        return jsonify({"success": False})

    # Make sure currency is in response
    data = res.json()
    #print (f"data: {data}")
    #print (f'data[rates]: {data["rates"]}')
    if currency not in data["rates"]:
        return jsonify({"success": False})

    return jsonify({"success": True, "rate": data["rates"][currency]})
