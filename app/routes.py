from flask import Blueprint, request, jsonify
from .models import Review, db
from .schema import ReviewSchema
from utils.db_helpers import get_or_404, get_list_or_404  # Handle product not found 404

review_schema = ReviewSchema(session=db.session)
reviews_schema = ReviewSchema(many=True, session=db.session)
bp = Blueprint("routes", __name__)

# Example route: Health check
@bp.route('/health', methods=['GET'])
def health_check():
    return jsonify({'status': 'reviews-service is healthy'}), 200


@bp.route("/reviews", methods=["POST"])
def create():
    data = request.json
    review = review_schema.load(data)
    db.session.add(review)
    db.session.commit()
    return jsonify(review_schema.dump(review)), 201


@bp.route("/reviews/<int:review_id>", methods=["GET"])
def get(review_id):
    filters = {key: value for key, value in request.args.items() if value is not None}
    review = get_or_404(Review, review_id, filters) if filters else get_or_404(Review, review_id)
    return jsonify(review_schema.dump(review)), 200


@bp.route("/reviews", methods=["GET"])
def get_all():
    try:
        reviews = get_list_or_404(Review)
        return jsonify(reviews_schema.dump(reviews)), 200
    except Exception as e:
        print("Error fetching reviews:", e)
        return jsonify({"error": str(e)}), 404

@bp.route('/reviews/<int:rating>', methods=['GET'])
def get_by_rating(rating):
    reviews = get_list_or_404(Review, 'rating', rating)
    return jsonify(reviews_schema.dump(reviews)), 200


@bp.route('/reviews/<int:review_id>', methods=['PUT'])
def update(review_id):
    review = get_or_404(Review, review_id) 
    data = request.get_json()
    updated_review = review_schema.load(data, instance=review, partial=True)
    db.session.commit()
    return jsonify(review_schema.dump(updated_review)), 200


@bp.route('/reviews/<int:review_id>', methods=['DELETE'])
def delete(review_id):
    review = get_or_404(Review, review_id)
    db.session.delete(review)
    db.session.commit()
    return jsonify({'message': 'Review deleted successfully'}), 204