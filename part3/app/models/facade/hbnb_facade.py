from app.models.sqlalchemy_repository import SQLAlchemyRepository

class HBnBFacade:
    """Façade pour gérer les opérations métier."""

    def __init__(self, repository: SQLAlchemyRepository):
        """
        Initialise la façade avec le repository.
        :param repository: Une instance de SQLAlchemyRepository.
        """
        self.repository = repository

    def create_user(self, user_data):
        """Créer un nouvel utilisateur."""
        from app.models.user import User  # Importer le modèle User
        user = User(**user_data)
        return self.repository.create(user)

    def get_user(self, user_id):
        """Récupère un utilisateur par son ID."""
        from app.models.user import User
        return self.repository.get(User, user_id)

    def get_all_users(self):
        """Récupère tous les utilisateurs."""
        from app.models.user import User
        return self.repository.all(User)

    def update_user(self, user_id, update_data):
        """Met à jour les données d'un utilisateur."""
        user = self.get_user(user_id)
        if not user:
            return None
        for key, value in update_data.items():
            setattr(user, key, value)
        return self.repository.update(user)

    def delete_user(self, user_id):
        """Supprime un utilisateur."""
        user = self.get_user(user_id)
        if user:
            self.repository.delete(user)
