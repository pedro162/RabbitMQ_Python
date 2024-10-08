import pika
from pika.exchange_type import ExchangeType

host = '172.23.0.2'
connection_parameters = pika.ConnectionParameters(host)
connection = pika.BlockingConnection(connection_parameters)
channel = connection.channel()

channel.queue_declare(queue='letterbox')
message = "Hello this is my first message"
channel.basic_publish(exchange='', routing_key='letterbox', body=message)
print(f'Sent message: {message}')
connection.close()

"""docker inspect -f '{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}' ea3f922715b9
172.23.0.2"""
