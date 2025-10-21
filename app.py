from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("Index.html")

@app.route("/add", methods=["POST"])
def add_transaction():
    description = request.form['description']
    amount = request.form['amount']

    print(f"New Transaction Received: Description={description}, Amount={amount}")

    return "<h1>Transaction added successfully!</h1><p> Go back to add another.</p>"