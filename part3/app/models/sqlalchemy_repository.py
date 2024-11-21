from sqlalchemy.orm import Session
from sqlalchemy.exc import NoResultFound

class SQLAlchemyRepository:
    """Repository utilisant SQLAlchemy pour la persistance."""

    def __init__(self, session: Session):
        """
        Initialise le repository avec une session SQLAlchemy.
        :param session: Instance de session SQLAlchemy.
        """
        self.session = session

    def create(self, instance):
        """
        Ajoute une nouvelle instance à la base de données.
        :param instance: L'instance du modèle à ajouter.
        """
        self.session.add(instance)
        self.session.commit()
        return instance

    def get(self, model, id):
        """
        Récupère une instance par ID.
        :param model: Le modèle SQLAlchemy.
        :param id: L'ID de l'instance.
        """
        try:
            return self.session.query(model).filter_by(id=id).one()
        except NoResultFound:
            return None

    def all(self, model):
        """
        Récupère toutes les instances d'un modèle.
        :param model: Le modèle SQLAlchemy.
        """
        return self.session.query(model).all()

    def update(self, instance):
        """
        Met à jour une instance existante.
        :param instance: L'instance mise à jour.
        """
        self.session.merge(instance)
        self.session.commit()
        return instance

    def delete(self, instance):
        """
        Supprime une instance de la base de données.
        :param instance: L'instance à supprimer.
        """
        self.session.delete(instance)
        self.session.commit()
