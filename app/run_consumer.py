from rabbit_consumers.rabbitmq import setup_channel
from rabbit_consumers.product_events import handle_delete_product

def main():
    connection, channel = setup_channel()

    # Queue אחת, callback אחד
    channel.basic_consume(queue='delete_product_reviews', on_message_callback=handle_delete_product)

    print("Waiting for messages. To exit press CTRL+C")
    try:
        channel.start_consuming()
    except KeyboardInterrupt:
        channel.stop_consuming()
    finally:
        connection.close()

if __name__ == "__main__":
    main()