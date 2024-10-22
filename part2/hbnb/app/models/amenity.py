from app.models.base_model import BaseModel
import uuid

class Amenity(BaseModel):
    def __init__(self, id, name):
        super().__init__()
        self.id = id
        self.name = name

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name
        }

    def update(self, data):
        # Met à jour les attributs de l'instance avec les nouvelles données
        for key, value in data.items():
            setattr(self, key, value)
