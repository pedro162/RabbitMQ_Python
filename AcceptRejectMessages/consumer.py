import pika
from pika.exchange_type import ExchangeType


def on_queue_on_message_received(ch, method, properties, body):
    if(method.delivery_tag % 5 == 0):
        #ch.basic_ack(delivery_tag=method.delivery_tag, multiple=True)
        #ch.basic_nack(delivery_tag=method.delivery_tag, requeue=True, multiple=True)
        ch.basic_nack(delivery_tag=method.delivery_tag, requeue=False, multiple=True)
    print(f'received new message: {body}')



host = '172.23.0.3'
connection_parameters = pika.ConnectionParameters(host)

connection = pika.BlockingConnection(connection_parameters)

channel = connection.channel()

channel.exchange_declare(exchange='acceptrejectexchange', exchange_type=ExchangeType.fanout)
channel.queue_declare(queue='letterbox')
channel.queue_bind('letterbox', 'acceptrejectexchange', 'test')

channel.basic_consume(queue='letterbox', on_message_callback=on_queue_on_message_received)


print('Starting Consuming')
channel.start_consuming()