from flask import Flask, jsonify, request
from myjson import JsonDeserialize, JsonSerialize
import sys
import dbclient as db

api = Flask(__name__)

#Devo connettermi al database
cur = db.connect()
if cur is None:
	print("Errore connessione al DB")
	sys.exit()


file_path = "anagrafe.json"
cittadini = JsonDeserialize(file_path)

file_path_users = "utenti.json"
utenti = JsonDeserialize(file_path_users)


def MiaProcedura():
    print("Buongiorno a tutti")






@api.route('/login', methods=['POST'])
def GestisciLogin():
    global cur
    content_type = request.headers.get('Content-Type')
    if content_type == 'application/json':
        jsonReq = request.json
        sUsernameInseritoDalClient = jsonReq["username"]
        sPasswordInseritaDalClient = jsonReq["password"]
        
        # Query per verificare username e password
        sQuery = "SELECT privilegi FROM utenti WHERE email = %s AND password = %s;"
        cur.execute(sQuery, (sUsernameInseritoDalClient, sPasswordInseritaDalClient))
        result = cur.fetchone()

        if result:
            sPriv = result[0]  # Recupera il privilegio
            return jsonify({"Esito": "000", "Msg": "Utente registrato", "Privilegio": sPriv}), 200
        else:
            return jsonify({"Esito": "001", "Msg": "Credenziali errate"})
    else:
        return jsonify({"Esito": "002", "Msg": "Formato richiesta errato"})
 





@api.route('/add_cittadino', methods=['POST'])
def GestisciAddCittadino():
    global cur
    content_type = request.headers.get('Content-Type')
    if content_type == 'application/json':
        jsonReq = request.json

        codice_fiscale = jsonReq.get('datiCittadino').get('codFiscale')
        nome = jsonReq.get('datiCittadino').get('nome')
        cognome = jsonReq.get('datiCittadino').get('cognome')
        data_nascita = jsonReq.get('datiCittadino').get('dataNascita')
        
        sQuery = "INSERT INTO cittadini (codice_fiscale, nome, cognome, data_nascita) VALUES (%s, %s, %s, %s);"
        try:
            db.write_in_db(cur, sQuery, (codice_fiscale, nome, cognome, data_nascita))
            return jsonify({"Esito": "000", "Msg": "Cittadino aggiunto con successo"}), 200
        except Exception as e:
            if 'duplicate key' in str(e):
                return jsonify({"Esito": "001", "Msg": "Cittadino già esistente"}), 200
            else:
                return jsonify({"Esito": "002", "Msg": "Errore nel salvataggio"}), 200
    else:
        return jsonify({"Esito": "002", "Msg": "Formato richiesta non valido"})




"""
Questa funzione sta sul SERVER. Riceve il codice fiscale dal client 
e verifica se il codice e d i dati associati stanno in anagrafe.json
"""

@api.route('/read_cittadino/<codice_fiscale>/<username>/<password>', methods=['GET'])
def read_cittadino(codice_fiscale, username, password):
    sQuery = "SELECT * FROM cittadini WHERE codice_fiscale = %s;"
    cur.execute(sQuery, (codice_fiscale,))
    cittadino = cur.fetchone()
    
    if cittadino:
        dati = {
            "codFiscale": cittadino[0],
            "nome": cittadino[1],
            "cognome": cittadino[2],
            "dataNascita": cittadino[3].strftime("%d/%m/%Y")
        }
        return jsonify({"Esito": "000", "Msg": "Cittadino trovato", "Dati": dati}), 200
    else:
        return jsonify({"Esito": "001", "Msg": "Cittadino non trovato"}), 200







@api.route('/update_cittadino', methods=['PUT'])
def update_cittadino():
    content_type = request.headers.get('Content-Type')
    if content_type == 'application/json':
        jsonReq = request.json
        codice_fiscale = jsonReq.get('codFiscale')
        nome = jsonReq.get('nome')
        cognome = jsonReq.get('cognome')
        data_nascita = jsonReq.get('dataNascita')
        
        sQuery = "UPDATE cittadini SET nome = %s, cognome = %s, data_nascita = %s WHERE codice_fiscale = %s;"
        iRet = db.write_in_db(cur, sQuery, (nome, cognome, data_nascita, codice_fiscale))

        if iRet == 0:
            return jsonify({"Esito": "000", "Msg": "Cittadino aggiornato con successo"}), 200
        else:
            return jsonify({"Esito": "001", "Msg": "Cittadino non trovato"}), 200
    else:
        return jsonify({"Esito": "002", "Msg": "Formato richiesta non valido"}), 200



api.run(host="0.0.0.0", port=8080, ssl_context="adhoc")

