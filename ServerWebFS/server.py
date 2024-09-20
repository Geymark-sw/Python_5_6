from flask import Flask, render_template, request

api = Flask(__name__)

utenti: list[list] = [["Pippo","Rossi","pippo@gmail.com""dajeRoma1","M","0"],["Pluto","Verdi","pluto@gmail.com","dajeRoma2","F","0"],["Paperino","Gialli",
                        "paperino@gialli.com","dajeRoma3","M","0"]]

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

    nome: str = request.args.get("nome")
    cognome: str = request.args.get("cognome")
    email: str = request.args.get("email")
    password: str = request.args.get("password")
    sesso: str = request.args.get("sesso")

    
    for i in utenti:
        if i[0] == nome and cognome == i[1] and email == i[2] == password == i[3] and sesso == i[4]:
                
            return reg_ok()
    
    return reg_ko()




@api.route('/accedi', methods=['GET'])
def accedi():

    utente: list[str] = [request.args.get("email"),request.args.get("password")]
    


    
    for i in utenti:
        if i[2] == utente[0] and i[3] == utente[4]:

            return reg_ok()
    
    return reg_ko()
    

            


api.run(host = "0.0.0.0",port = 8085)

