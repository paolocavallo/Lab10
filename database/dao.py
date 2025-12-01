from database.DB_connect import DBConnect
from model.compagnia import Compagnia
from model.hub import Hub
from model.spedizione import Spedizione


class DAO:
    """
    Implementare tutte le funzioni necessarie a interrogare il database.
    """
    # TODO

    def get_compagnia(self):
        conn = DBConnect.get_connection()
        result = []
        cursor = conn.cursor(dictionary=True)
        query = """SELECT * FROM compagnia"""
        cursor.execute(query)
        for row in cursor:
            compagnia = Compagnia(row["id"], row["codice"], row["nome"])
            result.append(compagnia)
        conn.close()
        cursor.close()
        return result

    def get_spedizione(self):
        conn = DBConnect.get_connection()
        result = []
        cursor = conn.cursor(dictionary=True)
        query = """SELECT * FROM spedizione"""
        cursor.execute(query)
        for row in cursor:
            spedizione = Spedizione(row["id"], row["id_compagnia"], row["numero_tracking"],
                                    row["id_hub_origine"], row["id_hub_destinazione"],
                                    row["data_ritiro_programmata"], row["distanza"],
                                    row["data_consegna"], row["valore_merce"])
            result.append(spedizione)
        conn.close()
        cursor.close()
        return result

    def get_hub(self):
        conn = DBConnect.get_connection()
        result = []
        cursor = conn.cursor(dictionary=True)
        query = """SELECT * FROM hub"""
        cursor.execute(query)
        for row in cursor:
            hub = Hub(row["id"], row["codice"], row["nome"], row["citta"], row["stato"],
                      row["latitudine"], row["longitudine"])
            result.append(hub)
        conn.close()
        cursor.close()
        return result

    def get_id_hub(self, threshold):
        conn = DBConnect.get_connection()
        cursor = conn.cursor(dictionary=True)
        result = []
        query = """SELECT LEAST(id_hub_origine, id_hub_destinazione) AS Hub_A, GREATEST(id_hub_origine, id_hub_destinazione) AS Hub_B, SUM(valore_merce) AS ValoreTotaleMerce, COUNT(*) AS NumeroSpedizioni, AVG(valore_merce) AS media_valore
                    FROM spedizione
                    GROUP BY Hub_A, Hub_B
                    HAVING AVG(valore_merce) >= %s"""
        cursor.execute(query, (threshold,))
        for row in cursor:
            result.append(row)
        cursor.close()
        conn.close()
        return result


