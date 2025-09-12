import pytest
# from app import create_app
from app.models import db, Review
from factories import ReviewFactory
from app import create_app


@pytest.fixture
def client():
    app = create_app()
    app.config['TESTING'] = True
    # app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    with app.app_context():
        print("DB URL in use:", db.engine.url)

        db.drop_all()
        db.create_all()
        yield app.test_client()
        db.session.remove()
        db.drop_all()
    
def test_create_a_review(client):
    """Create a new review and test the ststuse code & name"""
    response = client.post("/reviews", json={
        "user_name": "mr ba",
        "product_id": 2,
        "rating": 4,
        "comment": "Great"
    })
    data = response.get_json()
    print(data)
    assert data['user_name'] == "mr ba"
    assert response.status_code == 201
    print(response.get_data(as_text=True))
    
    
def test_get_review(client):
    """Create new review and get it via /reviews/<id>"""
    review = ReviewFactory()
    res = client.get(f"/reviews/{review.id}")
    data = res.get_json()
    assert data['id'] == review.id
    assert data['user_name'] == review.user_name
    
def test_update_a_review(client):
    """Update a new review and test it product status code & name"""
    review = ReviewFactory()
    response = client.put(f"/reviews/{review.id}", json={
        "rating": 5
    })
    assert response.status_code == 200
    data = response.get_json()
    assert data['user_name'] == review.user_name
    assert data['rating'] == 5
    
def test_delete_review(client):
    review = ReviewFactory()
    db.session.add(review)
    db.session.commit()
    reviews_count = Review.query.count()
    assert reviews_count == 1
    res = client.delete(f"/reviews/{review.id}")
    assert res.status_code == 204
    reviews_after_count = Review.query.count()
    assert reviews_after_count == 0
    
def test_list_reviews(client):
    names = []
    for _ in range(5):
        review = ReviewFactory()
        names.append(review.user_name)
        
    db.session.commit()
    
    res = client.get("/reviews")
    data = res.get_json()
    
    assert len(data) == 5

    response_names = [p["user_name"] for p in data]
    assert set(response_names) == set(names)
    
    
            
