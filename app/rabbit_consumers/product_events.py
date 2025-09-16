from app.models import Review, db

def handle_delete_product(ch, method, properties, body):
    """
    Handle Reviews deleting on product delete
    """
    import json
    data = json.loads(body)
    product_id = data.get("product_id")
    if not product_id:
        print("No product_id in message")
        ch.basic_ack(delivery_tag=method.delivery_tag)
        return

    reviews = Review.query.filter_by(product_id=product_id).all()
    for review in reviews:
        db.session.delete(review)
    db.session.commit()

    print(f"Deleted {len(reviews)} reviews for product {product_id}")
    ch.basic_ack(delivery_tag=method.delivery_tag)