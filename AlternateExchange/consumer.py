import pika
from pika.exchange_type import ExchangeType

def alt_queue_on_message_received(ch, method, properties, body):
    print(f'Alt: received new message: {body}')

def main_queue_on_message_received(ch, method, properties, body):
    print(f'Main: received new message: {body}')

host = '172.24.0.2'
connection_parameters = pika.ConnectionParameters(host)

connection = pika.BlockingConnection(connection_parameters)

channel = connection.channel()

channel.exchange_declare(exchange='altexchange', exchange_type=ExchangeType.fanout)
channel.exchange_declare(exchange='mainexchange', exchange_type=ExchangeType.direct, arguments={
    'alternative-exchange':'altexchange'
})
channel.queue_declare(queue='altexchangequeue')
channel.queue_bind('altexchangequeue', 'altexchange')
channel.basic_consume(queue='altexchangequeue', auto_ack=True, on_message_callback=alt_queue_on_message_received)

#===========================


channel.queue_declare(queue='mainexchangequeue')
channel.queue_bind('mainexchangequeue', 'mainexchange', 'test')
channel.basic_consume(queue='mainexchangequeue', auto_ack=True, on_message_callback=main_queue_on_message_received)



print('Starting Consuming')
channel.start_consuming()