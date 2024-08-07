import pika
from pika.exchange_type import ExchangeType


def dlx_queue_on_message_received(ch, method, properties, body):
    print(f'DLX: received new message: {body}')

def main_queue_on_message_received(ch, method, properties, body):
    print(f'MAIN: received new message: {body}')


host = '172.24.0.4'
connection_parameters = pika.ConnectionParameters(host)

connection = pika.BlockingConnection(connection_parameters)

channel = connection.channel()

channel.exchange_declare(exchange='mainexchange', exchange_type=ExchangeType.direct)
channel.exchange_declare(exchange='dlx', exchange_type=ExchangeType.fanout)

channel.queue_declare(queue='mainexchangequeue', arguments={
    'x-dead-letter-exchange': 'dlx', 'x-message-ttl':1000
})
channel.queue_bind('mainexchangequeue', 'mainexchange', 'test')

channel.basic_consume(queue='mainexchangequeue', auto_ack=True, on_message_callback=main_queue_on_message_received)


##================

channel.queue_declare(queue='dlxqueue')
channel.queue_bind('dlxqueue', 'dlx')


channel.basic_consume(queue='dlxqueue', auto_ack=True, on_message_callback=dlx_queue_on_message_received)


print('Starting Consuming')
channel.start_consuming()