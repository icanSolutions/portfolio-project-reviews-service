import factory
from app.models import Review
from app import db

class ReviewFactory(factory.alchemy.SQLAlchemyModelFactory):
    class Meta:
        model = Review
        sqlalchemy_session = db.session
        sqlalchemy_session_persistence = "flush"

    product_id = factory.Faker("random_int", min=1, max=1000)
    user_name = factory.Faker("name")
    rating = factory.Faker("random_int", min=1, max=5)
    comment = factory.Faker("sentence")
