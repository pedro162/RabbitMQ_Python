import pika
from pika.exchange_type import ExchangeType

host = '172.24.0.4'
connection_parameters = pika.ConnectionParameters(host)

connection = pika.BlockingConnection(connection_parameters)

channel = connection.channel()
channel.exchange_declare(exchange='altexchange', exchange_type=ExchangeType.fanout)
channel.exchange_declare(exchange='mainexchange', exchange_type=ExchangeType.direct, arguments={
    'alternate-exchange':'altexchange'
})

message = 'Hello this is my first message'

channel.basic_publish(exchange='mainexchange', routing_key='testaa', body=message)

print(f'Sent message: {message}')

connection.close()
