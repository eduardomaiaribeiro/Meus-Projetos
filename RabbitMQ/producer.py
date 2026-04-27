import pika
import os
from dotenv import load_dotenv

# Carrega variáveis de ambiente do arquivo .env
load_dotenv()

RABBITMQ_USER = os.getenv('RABBITMQ_USER')
RABBITMQ_PASSWORD = os.getenv('RABBITMQ_PASSWORD')
RABBITMQ_HOST = os.getenv('RABBITMQ_HOST', 'localhost')
RABBITMQ_QUEUE = os.getenv('RABBITMQ_QUEUE', 'fila_exemplo')

if not RABBITMQ_USER or not RABBITMQ_PASSWORD:
    raise Exception('Credenciais do RabbitMQ não definidas nas variáveis de ambiente.')

credentials = pika.PlainCredentials(RABBITMQ_USER, RABBITMQ_PASSWORD)
parameters = pika.ConnectionParameters(host=RABBITMQ_HOST, credentials=credentials)

connection = pika.BlockingConnection(parameters)
channel = connection.channel()

channel.queue_declare(queue=RABBITMQ_QUEUE, durable=True)

mensagem = 'Olá, RabbitMQ!'
channel.basic_publish(
    exchange='',
    routing_key=RABBITMQ_QUEUE,
    body=mensagem,
    properties=pika.BasicProperties(delivery_mode=2)  # Mensagem persistente
)
print(f"[x] Mensagem enviada: {mensagem}")

connection.close()
