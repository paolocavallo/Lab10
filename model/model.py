from database.DB_connect import DBConnect
from database.dao import DAO
import networkx as nx

class Model:
    def __init__(self):
        self._nodes = None
        self._edges = None
        self.G = nx.Graph()

    def costruisci_grafo(self, threshold):
        """
        Costruisce il grafo (self.G) inserendo tutti gli Hub (i nodi) presenti e filtrando le Tratte con
        guadagno medio per spedizione >= threshold (euro)
        """
        # TODO
        self.G.clear()
        lista_hub_oggetti = DAO().get_hub()
        nodi_da_aggiungere = [hub.id for hub in lista_hub_oggetti]
        self.G.add_nodes_from(nodi_da_aggiungere)
        lista_conn = DAO().get_id_hub(threshold)
        for conn in lista_conn:
            hub_sorgente = conn["Hub_A"]
            hub_destinazione = conn["Hub_B"]
            guadagno_medio = conn["ValoreTotaleMerce"]
            peso = conn["NumeroSpedizioni"]
            media_valore = round(conn["media_valore"], 1)
            if guadagno_medio >= threshold:
                self.G.add_edge(
                    hub_sorgente,
                    hub_destinazione,
                    weight=peso,
                    guadagno_medio=guadagno_medio,
                    media_valore=media_valore
                )
    def get_num_edges(self):
        """
        Restituisce il numero di Tratte (edges) del grafo
        :return: numero di edges del grafo
        """
        # TODO
        return self.G.number_of_edges()


    def get_num_nodes(self):
        """
        Restituisce il numero di Hub (nodi) del grafo
        :return: numero di nodi del grafo
        """
        # TODO
        return self.G.number_of_nodes()

    def get_all_edges(self):
        """
        Restituisce tutte le Tratte (gli edges) con i corrispondenti pesi
        :return: gli edges del grafo con gli attributi (il weight)
        """
        # TODO
        return list(self.G.edges(data=True))

