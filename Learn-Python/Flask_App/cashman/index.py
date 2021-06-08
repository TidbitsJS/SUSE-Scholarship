from flask import Flask, jsonify, request

app = Flask(__name__)

incomes = [
    {'description': 'salary', 'amount': 5000}
]


@app.route("/")
def welcome():
    return "Welcome to Cashman - A Flask Restful API App"


@app.route("/incomes")
def get_incomes():
    return jsonify(incomes)


@app.route("/incomes", methods=['POST'])
def add_income():
    incomes.append(request.get_json())
    return 'Item Added!', 204
