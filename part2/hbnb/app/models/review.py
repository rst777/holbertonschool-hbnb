#!/user/bin/python3

from .app.models import BaseModel
from .app.models import Place
from .app.models import User

class Review(BaseModel):
    def __init__(self, text, rating, place, user):
        super().__init__()
        self.text = text  # Contenu de l'avis
        self.rating = rating  # Note donnée (entre 1 et 5)
        self.place = place  # Lieu associé à l'avis (instance de Place)
        self.user = user  # Utilisateur qui a écrit l'avis (instance de User)
