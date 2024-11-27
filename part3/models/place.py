#!/usr/bin/python3
"""Place Model Module"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Integer, Float, ForeignKey, Table
from sqlalchemy.orm import relationship, backref


class Place(BaseModel, Base):
    """Place Model"""
    __tablename__ = 'places'

    city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024))
    number_rooms = Column(Integer, default=0)
    number_bathrooms = Column(Integer, default=0)
    max_guest = Column(Integer, default=0)
    price_by_night = Column(Integer, default=0)
    latitude = Column(Float)
    longitude = Column(Float)

    # Définition explicite de la table d'association
    place_amenity = Table(
        'place_amenity',
        Base.metadata,
        Column(
            'place_id',
            String(60),
            ForeignKey(
                'places.id',
                ondelete='CASCADE'),
            primary_key=True,
            nullable=False),
        Column(
            'amenity_id',
            String(60),
            ForeignKey(
                'amenities.id',
                ondelete='CASCADE'),
            primary_key=True,
            nullable=False))

    amenities = relationship(
        "Amenity",
        secondary=place_amenity,
        backref=backref("places", lazy='dynamic'),
        lazy='dynamic',
        cascade="all, delete"
    )

    reviews = relationship(
        "Review",
        backref="place",
        cascade="all, delete-orphan"
    )


@property
def reviews(self):
    """Get reviews for this place"""
    from models import storage
    all_reviews = storage.all(Review)
    return [review for review in all_reviews.values()
            if review.place_id == self.id]
