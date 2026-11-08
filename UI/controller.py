import flet as ft
from UI.view import View
from model.model import Model

'''
    CONTROLLER:
    - Funziona da intermediario tra MODELLO e VIEW
    - Gestisce la logica del flusso dell'applicazione
'''

class Controller:
    def __init__(self, view: View, model: Model):
        self._model = model
        self._view = view

        # Variabili per memorizzare le selezioni correnti
        self.biblioteca_selezionata = None
        self.genere_selezionato = None

    # POPOLA DROPDOWN
        def popola_dropdown_biblioteche(self):
        """ Legge le biblioteche dal model e aggiunge le opzioni al Dropdown """
        # Aggiungo l'opzione "Nessun filtro" come richiesto
        self._view.dd_biblioteca.options.append(
            ft.dropdown.Option(key="NONE", text="Nessun filtro")
        )

        # Recupero tutte le biblioteche
        biblioteche = self._model.get_biblioteche()
        for b in biblioteche:
            # Usiamo l'ID come chiave (key) per ritrovarlo facilmente nelle query
            self._view.dd_biblioteca.options.append(
                ft.dropdown.Option(key=str(b.id), text=b.nome)
            )

    def popola_dropdown_generi(self):
        """ Legge i generi dal model e aggiunge le opzioni al Dropdown """
        # Aggiungo l'opzione "Nessun filtro"
        self._view.dd_genere.options.append(
            ft.dropdown.Option(key="NONE", text="Nessun filtro")
        )

        generi = self._model.get_generi()
        for g in generi:
            self._view.dd_genere.options.append(
                ft.dropdown.Option(key=g, text=g)
            )

    # CALLBACKS DROPDOWN
    def handler_biblioteca_selezionata(self, e):
        """ Salva l'ID della biblioteca selezionata """
        valore = self._view.dd_biblioteca.value
        if valore == "NONE" or valore is None:
            self.biblioteca_selezionata = None
        else:
            self.biblioteca_selezionata = int(valore)

    def handler_genere_selezionato(self, e):
        """ Salva il genere selezionato """
        valore = self._view.dd_genere.value
        if valore == "NONE" or valore is None:
            self.genere_selezionato = None
        else:
            self.genere_selezionato = valore

    # AZIONE: MOSTRA LIBRI
    def handle_mostra_libri(self, e):
        """ Recupera i libri filtrati dal modello e aggiorna la View """
        # Chiedo i libri filtrati al modello
        libri = self._model.get_libri_filtrati(self.biblioteca_selezionata, self.genere_selezionato)

        # Svuoto la lista grafica precedente
        self._view.lv_risultati.controls.clear()

        # Se non trovo nessun libro, mostro un alert informativo
        if not libri:
            self._view.show_alert("Nessun libro trovato con i filtri selezionati!")
        else:
            # Aggiungo ogni libro alla ListView grafica
            for l in libri:
                self._view.lv_risultati.controls.append(
                    ft.Text(str(l))
                )

        # Aggiorno l'interfaccia utente
        self._view.update()
