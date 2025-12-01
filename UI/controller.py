import flet as ft
from UI.view import View
from database.dao import DAO
from model.model import Model


class Controller:
    def __init__(self, view: View, model: Model):
        self._view = view
        self._model = model

    def mostra_tratte(self, e):
        """
        Funzione che controlla prima se il valore del costo inserito sia valido (es. non deve essere una stringa) e poi
        popola "self._view.lista_visualizzazione" con le seguenti info
        * Numero di Hub presenti
        * Numero di Tratte
        * Lista di Tratte che superano il costo indicato come soglia
        """
        # TODO
        try:
            threshold = float(self._view.guadagno_medio_minimo.value)
        except ValueError:
            self._view.lista_visualizzazione.append(f"ERRORE: inserire un valore valido")
        else:
            grafo = self._model.costruisci_grafo(threshold)
            num_edges = self._model.get_num_edges()
            num_nodes = self._model.get_num_nodes()
            tratte = self._model.get_all_edges()
            lista_hub_oggetti = DAO().get_hub()
            hub_name_lookup = {}
            for hub in lista_hub_oggetti:
                hub_name_lookup[hub.id] = hub.nome


            self._view.lista_visualizzazione.controls.clear()
            self._view.lista_visualizzazione.controls.append(ft.Text(f"Numero di hubs: {num_nodes}"))
            self._view.lista_visualizzazione.controls.append(ft.Text(f"Numero di tratte: {num_edges}"))
            for elemento in tratte:
                self._view.lista_visualizzazione.controls.append(ft.Text(f"{hub_name_lookup[elemento[0]]}->{hub_name_lookup[elemento[1]]}--guadagno Medio Per Spedizione:{elemento[2]['media_valore']}\n"))
            self._view.update()

