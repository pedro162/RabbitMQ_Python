import pika
from pika.exchange_type import ExchangeType

host = '172.23.0.3'
connection_parameters = pika.ConnectionParameters(host)

connection = pika.BlockingConnection(connection_parameters)

channel = connection.channel()

channel.exchange_declare(exchange='acceptrejectexchange', exchange_type=ExchangeType.fanout)
message = 'Lets send this'

while True:
    channel.basic_publish(exchange='acceptrejectexchange', routing_key='test', body=message)
    print(f'Sent message: {message}')
    input('Press any key to continue..')
    
    
#connection.close()