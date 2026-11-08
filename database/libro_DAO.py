from database.DB_connect import DBConnect
from model.libro_DTO import Libro

"""
    LIBRO DAO
    Gestisce le operazioni di accesso al database relative ai libri (Effettua le Query).
"""


class LibroDAO:
    def __init__(self):
        pass

    def get_all_generi(self):
        # Restituisco una lista di stringhe contenente tutti i generi distinti dei libri
        cnx = DBConnect.get_connection()
        if cnx is None:
            return []

        cursor = cnx.cursor()
        # Prendo i generi senza duplicati e li riordino alfabeticamente
        query = "SELECT DISTINCT genere FROM libro WHERE genere IS NOT NULL ORDER BY genere"
        cursor.execute(query)

        generi = []
        for row in cursor:
            # row è una tupla, prendo il primo elemento row[0]
            generi.append(row[0])

        cursor.close()
        cnx.close()
        return generi

    def get_libri_filtrati(self, id_biblioteca, genere):
        #Restituisce i libri filtrati per biblioteca e/o genere.
        #Se id_biblioteca o genere valgono None, la query COALESCE ignora quel filtro.

        cnx = DBConnect.get_connection()
        if cnx is None:
            return []

        cursor = cnx.cursor(dictionary=True)

        # Usiamo COALESCE(%s, id_biblioteca): se passiamo None (NULL), il filtro si annulla da solo!
        query = """
            SELECT * 
            FROM libro 
            WHERE id_biblioteca = COALESCE(%s, id_biblioteca)
              AND genere = COALESCE(%s, genere)
            ORDER BY titolo
        """

        cursor.execute(query, (id_biblioteca, genere))

        libri = []
        for row in cursor:
            l = Libro(
                id=row["id"],
                titolo=row["titolo"],
                autore=row["autore"],
                genere=row["genere"],
                anno_pubblicazione=row["anno_pubblicazione"],
                id_biblioteca=row["id_biblioteca"]
            )
            libri.append(l)

        cursor.close()
        cnx.close()
        return libri

