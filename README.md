# RabbitMQ_Python

This project demonstrates the implementation of various types of exchanges and queues using RabbitMQ in Python. It covers publishing and consuming messages through different exchange types, showcasing how to efficiently handle messaging patterns in distributed systems.

## Table of Contents

- [Project Overview](#project-overview)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
  - [Exchange Types](#exchange-types)
  - [Queue Types](#queue-types)
  - [Publishing Messages](#publishing-messages)
  - [Consuming Messages](#consuming-messages)
- [Screenshots](#screenshots)
- [Contributing](#contributing)
- [License](#license)

## Project Overview

The "RabbitMQ_Python" project provides a comprehensive guide to working with RabbitMQ in Python, covering the following concepts:

1. **Exchanges:** Direct, Topic, Fanout, and Headers exchanges.
2. **Queues:** Durable, Non-Durable, Exclusive, and Auto-Delete queues.
3. **Message Publishing:** Techniques for sending messages to different exchange types.
4. **Message Consumption:** Techniques for consuming messages from various queues.

This project is intended to help developers understand and implement robust messaging solutions using RabbitMQ.

## Requirements

To run this application, you will need the following:

- Python 3.6 or higher
- pika (Python client for RabbitMQ)
- RabbitMQ Server

You can install the required packages using the following command:

```bash
pip install pika
```

Ensure RabbitMQ server is installed and running on your machine. You can download and install RabbitMQ from [here](https://www.rabbitmq.com/download.html).

## Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/pedro162/RabbitMQ_Python.git
   cd RabbitMQ_Python
   ```

2. **Install the required dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

## Usage

### Exchange Types

- **Direct Exchange:** Routes messages to queues based on an exact match between the routing key and the queue binding key.
- **Topic Exchange:** Routes messages to queues based on a pattern matching between the routing key and the queue binding key.
- **Fanout Exchange:** Broadcasts messages to all queues bound to it, regardless of routing key.
- **Headers Exchange:** Routes messages based on message header values instead of the routing key.

### Queue Types

- **Durable Queue:** Survives a RabbitMQ server restart.
- **Non-Durable Queue:** Does not survive a RabbitMQ server restart.
- **Exclusive Queue:** Used by only one connection and deleted when that connection closes.
- **Auto-Delete Queue:** Automatically deleted when the last consumer unsubscribes.

### Publishing Messages

To publish messages to a specific exchange:

```python
import pika

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

channel.exchange_declare(exchange='direct_logs', exchange_type='direct')

channel.basic_publish(exchange='direct_logs', routing_key='info', body='Hello RabbitMQ!')
connection.close()
```

### Consuming Messages

To consume messages from a queue:

```python
import pika

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

channel.queue_declare(queue='hello')

def callback(ch, method, properties, body):
    print(f" [x] Received {body}")

channel.basic_consume(queue='hello', on_message_callback=callback, auto_ack=True)
channel.start_consuming()
```

## Screenshots

### Direct Exchange Example

![Direct Exchange](screenshots/direct_exchange.png)

### Topic Exchange Example

![Topic Exchange](screenshots/topic_exchange.png)

## Contributing

Contributions are welcome! If you have suggestions for improvements or new features, feel free to submit a pull request or open an issue.

## License

This project is licensed under the MIT License.
