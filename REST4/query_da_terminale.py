from configparser import ConfigParser
import psycopg2
import dbclient as db  # Assumendo che il modulo `dbclient` fornisca le funzioni di connessione e esecuzione query.

def main():
    # Connessione al database
    cur = db.connect()
    if cur is None:
        print("Errore connessione al database.")
        return
    
    while True:
        # Menu interattivo per l'utente
        print("\nScegli cosa vuoi fare:")
        print("1. Query di scrittura")
        print("2. Query di lettura")
        print("3. Esci")
        
        choice = input("Inserisci la tua scelta (1, 2 o 3): ")
        
        if choice == "1":
            # Inserisci query di scrittura
            query = input("Inserisci la query di scrittura: ")
            ret = db.write_in_db(cur, query)
            
            if ret == 0:
                print("Query di scrittura eseguita correttamente.")
            elif ret == -2:
                print("Errore: chiave duplicata.")
            else:
                print("Errore nell'esecuzione della query di scrittura.")
                
        elif choice == "2":
            # Inserisci query di lettura
            query = input("Inserisci la query di lettura: ")
            num_rows = db.read_in_db(cur, query)
            
            if num_rows >= 0:
                print(f"Numero di righe restituite: {num_rows}")
                # Stampa ogni riga restituita dalla query
                for _ in range(num_rows):
                    row = db.read_next_row(cur)
                    if row[0] == 0:  # Se la lettura è andata a buon fine
                        print(row[1])  # Stampa la riga letta
                    else:
                        print("Errore nella lettura delle righe.")
            else:
                print("Errore nell'esecuzione della query di lettura.")
                
        elif choice == "3":
            print("Chiusura del programma.")
            break
        else:
            print("Scelta non valida. Riprova.")
    
    # Chiudi la connessione al database
    db.close(cur)

if __name__ == '__main__':
    main()
