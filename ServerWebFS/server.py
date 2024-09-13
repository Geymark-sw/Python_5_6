from flask import Flask, render_template, request

api = Flask(__name__)

utenti: list[list] = [["Pippo","dajeRome1","M","0"],["Pluto","dajeRoma2","F","0"],["Paperino","dajeRoma3","M","0"]]

@api.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@api.route('/pippo', methods=['GET'])
def pippo():
    return render_template('formSemplice.html')

@api.route('/reg_ok', methods=['GET'])
def reg_ok():
    return render_template('reg_ok.html')

@api.route('/reg_ko', methods=['GET'])
def reg_ko():
    return render_template('reg_ko.html')

@api.route('/registrati', methods=['GET'])
def registrati():
    nome = request.args.get("nome")

    print("Nome inserito: " + nome)

    password = request.args.get("cognome")

    if 




api.run(host = "0.0.0.0",port = 8085)

