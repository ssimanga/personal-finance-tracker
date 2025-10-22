from flask import Flask, render_template, request, redirect, url_for
import csv

app = Flask(__name__)

CSV_FILE = 'transactions.csv'

def load_transactions():
    """Loads transactions from CSV file"""
    try:
        with open(CSV_FILE, mode="r", newline='') as file:
            reader = csv.DictReader(file)
            return list(reader)
    except FileNotFoundError:
        return []
    
def save_transaction(description, amount):
    """Saves a single transaction to the CSV file"""
    with open(CSV_FILE, mode='a', newline='') as file:
        fieldnames = ['description', 'amount']
        writer = csv.DictWriter(file, fieldnames=fieldnames)

        file.seek(0,2)
        if file.tell() == 0:
            writer.writeheader()
        writer.writerow({'description': description, 'amount': amount})

@app.route("/")
def index():
    transactions = load_transactions()
    return render_template("Index.html", transactions=transactions)

@app.route("/add", methods=["POST"])
def add_transaction():
    description = request.form['description']
    amount = request.form['amount']

    save_transaction(description, amount)

    return redirect(url_for('index'))