import pika

def on_message_received(ch, method, properties, body):
    print(f'received new message: {body}')

host = '172.23.0.2'
connection_parameters = pika.ConnectionParameters(host=host)
connection = pika.BlockingConnection(connection_parameters)
channel = connection.channel()

channel.queue_declare(queue='letterbox')

channel.basic_consume(queue='letterbox', auto_ack=True, on_message_callback=on_message_received)
print('Starting Consuming')
channel.start_consuming()