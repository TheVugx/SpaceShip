import firebase_admin

from firebase_admin import credentials, firestore

class Fireb():
    def __init__(self):
        if not firebase_admin._apps:
            cred = credentials.Certificate('src/credentials.json')
            firebase_admin.initialize_app(cred)

        self.db = firestore.client()

    def guardar_puntuacion(self, nombre: str, puntuacion: int):

        jugador_ref = self.db.collection('spaceshiphighscores').where('nombre_jugador', '==', nombre).get()
        if jugador_ref:
            for doc in jugador_ref:
                if doc.to_dict()['puntuacion'] < puntuacion:
                    doc.reference.update({'puntuacion': puntuacion})
                    return
                
        else:
            doc_ref = self.db.collection('spaceshiphighscores').add({
                'nombre_jugador':nombre,
                'puntuacion':puntuacion})

    def obtener_leaderboard(self):
        leaderboard = self.db.collection('spaceshiphighscores').order_by('puntuacion', direction=firestore.Query.DESCENDING).limit(10).stream()

        for doc in leaderboard:
            print(f'{doc.to_dict()["nombre_jugador"]}: {doc.to_dict()["puntuacion"]}')

