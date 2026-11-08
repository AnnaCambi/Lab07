from database.DB_connect import DBConnect
from model.biblioteca_DTO import Biblioteca

"""
    Biblioteca DAO
    Gestisce le operazioni di accesso al database relative alle biblioteche (Effettua le Query).
"""

class BibliotecaDAO:
    def __init__(self):
        pass

    def get_all_biblioteche(self):
        # Leggo tutte le biblioteche dal database e restituisco una lista di oggetti 'Biblioteca'

        # Chiedo la connessione al database tramite il pool
        cnx = DBConnect.get_connection()
        if cnx is None:
            print("Errore di connessione al database")
            return []

        cursor = cnx.cursor(dictionary=True)
        # Query SQL per prendere tutte le biblioteche ordinate per nome
        query = "SELECT * FROM biblioteca ORDER BY nome"
        cursor.execute(query)

        risultato = []
        for row in cursor:
            # Creo l'oggetto Biblioteca usando i campi presi dal DB
            b = Biblioteca(
                id=row["id"],
                nome=row["nome"],
                indirizzo=row["indirizzo"]
            )
            risultato.append(b)

        cursor.close()
        cnx.close()
        return risultato

