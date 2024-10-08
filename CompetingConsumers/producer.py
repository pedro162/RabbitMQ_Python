import pika
from pika.exchange_type import ExchangeType
import time
import random

host = '172.23.0.4'
connection_parameters = pika.ConnectionParameters(host)
connection = pika.BlockingConnection(connection_parameters)
channel = connection.channel()

channel.queue_declare(queue='letterbox')
messageI = 1
while(True):
    message = f"Sending messageID: {messageI}"
    channel.basic_publish(exchange='', routing_key='letterbox', body=message)
    print(f'Sent message: {message}')
    time.sleep(random.randint(1, 4))
    messageI +=1
    #connection.close()

"""docker inspect -f '{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}' f3040793f803
172.23.0.2
Last class: 8a
"""
