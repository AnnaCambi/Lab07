from database.biblioteca_DAO import BibliotecaDAO
from database.libro_DAO import LibroDAO

'''
    MODELLO:
    - Rappresenta la struttura dati
    - Si occupa di gestire lo stato dell'applicazione
    - Si occupa di interrogare il DAO (chiama i metodi di BibliotecaDAO e LibroDAO)
'''

class Model:
    def __init__(self):
        self._biblioteca_dao = BibliotecaDAO()
        self._libro_dao = LibroDAO()

    # --- LIBRI ---
    def get_libri_filtrati(self, id_biblioteca, genere):
        """ Restituisce la lista di tutti i libri filtrati per biblioteca e/o genere """
        # Richiama il DAO passando i due filtri
        return self._libro_dao.get_libri_filtrati(id_biblioteca, genere)

    def get_generi(self):
        """ Restituisce la lista di tutti i generi disponibili """
        return self._libro_dao.get_all_generi()

    # --- BIBLIOTECHE ---
    def get_biblioteche(self):
        """ Restituisce la lista di tutte le biblioteche """
        return self._biblioteca_dao.get_all_biblioteche()
