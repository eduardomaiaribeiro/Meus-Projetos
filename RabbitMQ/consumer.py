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

print('[*] Aguardando mensagens. Para sair, pressione CTRL+C')

def callback(ch, method, properties, body):
    print(f"[x] Mensagem recebida: {body.decode()}")
    ch.basic_ack(delivery_tag=method.delivery_tag)

channel.basic_consume(queue=RABBITMQ_QUEUE, on_message_callback=callback)

try:
    channel.start_consuming()
except KeyboardInterrupt:
    print('\nInterrompido pelo usuário.')
    channel.stop_consuming()
finally:
    connection.close()
