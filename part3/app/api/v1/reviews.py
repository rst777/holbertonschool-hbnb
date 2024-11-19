from flask_restx import Namespace, Resource, fields
from app.services.facade import facade
from flask import request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
review_db =[]
place_db =[]

api = Namespace('reviews', description='Review operations')

review_model = api.model('Review', {
    'id': fields.String(readonly=True, description='Unique identifier'),
    'text': fields.String(required=True, description='Review text'),
    'rating': fields.Integer(required=True, min=1, max=5, description='Rating (1-5)'),
    'user_id': fields.String(required=True, description='ID of the reviewer'),
    'place_id': fields.String(required=True, description='ID of the reviewed place'),
    'created_at': fields.DateTime(readonly=True),
    'updated_at': fields.DateTime(readonly=True)
})

@api.route('/')
class ReviewList(Resource):
    @api.doc('list_reviews')
    @api.marshal_list_with(review_model)
    def get(self):
        """List all reviews"""
        return facade.get_all_reviews()

    @api.doc('create_review')
    @api.expect(review_model)
    @api.marshal_with(review_model, code=201)
    @api.response(400, 'Validation Error')
    def post(self):
        """Create a new review"""
        try:
            return facade.create_review(api.payload), 201
        except ValueError as e:
            api.abort(400, str(e))

@api.route('/<string:review_id>')
@api.param('review_id', 'The review identifier')
@api.response(404, 'Review not found')

@jwt_required()
def post(self):
    """Create a review (user cannot review their own places)."""
    user = get_jwt_identity()
    data = request.get_json()
    place_id = data.get('place_id')

    # Trouver le lieu
    place = next((p for p in place_db if p['id'] == place_id), None)
    if not place:
        return {"error": "Place not found."}, 404

    # Vérifier que l'utilisateur ne révise pas son propre lieu
    if place['owner_id'] == user['id']:
        return {"error": "You cannot review your own place."}, 403

    # Vérifier que l'utilisateur n'a pas déjà évalué ce lieu
    existing_review = next(
        (r for r in review_db if r['place_id'] == place_id and r['reviewer_id'] == user['id']), None)
    if existing_review:
        return {"error": "You cannot review a place more than once."}, 400

    # Créer une nouvelle revue
    new_review = {
        "id": len(review_db) + 1,
        "place_id": place_id,
        "reviewer_id": user['id'],
        "content": data['content']
    }
    review_db.append(new_review)
    return new_review, 201


class ReviewResource(Resource):
    @api.doc('get_review')
    @api.marshal_with(review_model)
    def get(self, review_id):
        """Get a review by ID"""
        review = facade.get_review(review_id)
        if not review:
            api.abort(404, "Review not found")
        return review

    @api.doc('update_review')
    @api.expect(review_model)
    @api.marshal_with(review_model)
    def put(self, review_id):
        """Update a review"""
        try:
            review = facade.update_review(review_id, api.payload)
            if not review:
                api.abort(404, "Review not found")
            return review
        except ValueError as e:
            api.abort(400, str(e))

    @api.doc('delete_review')
    @api.response(200, 'Review deleted')
    def delete(self, review_id):
        """Delete a review"""
        try:
            facade.delete_review(review_id)
            return {'message': 'Review deleted successfully'}
        except ValueError as e:
            api.abort(404, str(e))

@api.route('/places/<string:place_id>/reviews')
@api.param('place_id', 'The place identifier')
class PlaceReviewList(Resource):
    @api.doc('list_reviews_for_place')
    @api.marshal_list_with(review_model)
    def get(self, place_id):
        """List all reviews for a place"""
        try:
            # Vérifie d'abord si le place existe
            place = facade.get_place(place_id)
            if not place:
                api.abort(404, f"Place {place_id} not found")
                
            # Récupère les reviews pour ce place
            reviews = facade.get_reviews_by_place(place_id)
            return reviews
        except ValueError as e:
            api.abort(400, str(e))

@api.route('/places/<string:place_id>/reviews')
class PlaceReviews(Resource):
    @api.marshal_list_with(review_model)
    def get(self, place_id):
        """Get all reviews for a place"""
        try:
            return facade.get_reviews_by_place(place_id)
        except ValueError as e:
            api.abort(404, str(e))
