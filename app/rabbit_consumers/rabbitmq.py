import pika
import json

RABBIT_HOST = 'rabbitmq'

def get_connection():
    return pika.BlockingConnection(pika.ConnectionParameters(host=RABBIT_HOST))

def setup_channel():
    connection = get_connection()
    channel = connection.channel()

    # Set an exchange
    channel.exchange_declare(exchange='products_exchange', exchange_type='direct', durable=True)

    # Queues & bind setting to each action
    channel.queue_declare(queue='delete_product_reviews', durable=True)
    channel.queue_bind(exchange='products_exchange', queue='delete_product_reviews', routing_key='product.deleted')

    
    return connection, channel