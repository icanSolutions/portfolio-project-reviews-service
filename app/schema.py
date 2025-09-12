from marshmallow_sqlalchemy import SQLAlchemySchema, auto_field
from app.models import Review

class ReviewSchema(SQLAlchemySchema):
    class Meta:
        model = Review
        load_instance = True  # Deserialize into SQLAlchemy model
        include_fk = True     # If using foreign keys

    id = auto_field(dump_only=True)
    user_name = auto_field(required=True)
    product_id = auto_field(required=True)
    rating = auto_field(required=True)
    comment = auto_field()
    created_at = auto_field()
    
    
    