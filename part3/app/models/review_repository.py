from sqlalchemy.orm import Session
from models.review import Review

class ReviewRepository:
    """Repository pour gérer les entités Review."""

    def __init__(self, session: Session):
        self.session = session

    def create_review(self, review_data):
        review = Review(**review_data)
        self.session.add(review)
        self.session.commit()
        return review

    def get_review_by_id(self, review_id):
        return self.session.query(Review).get(review_id)

    def update_review(self, review):
        self.session.merge(review)
        self.session.commit()
        return review

    def delete_review(self, review):
        self.session.delete(review)
        self.session.commit()
