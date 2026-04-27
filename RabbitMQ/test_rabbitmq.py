import unittest
from unittest.mock import patch, MagicMock
import producer
import consumer

class TestProducer(unittest.TestCase):
    @patch('producer.pika.BlockingConnection')
    @patch('producer.pika.ConnectionParameters')
    @patch('producer.pika.PlainCredentials')
    def test_producer_env_vars(self, mock_creds, mock_params, mock_conn):
        with patch.dict('os.environ', {
            'RABBITMQ_USER': 'user',
            'RABBITMQ_PASSWORD': 'pass',
            'RABBITMQ_HOST': 'localhost',
            'RABBITMQ_QUEUE': 'fila_exemplo',
        }):
            # Simula conexão e canal
            mock_channel = MagicMock()
            mock_conn.return_value.channel.return_value = mock_channel
            # Executa o producer
            import importlib
            importlib.reload(producer)
            # Verifica se a mensagem foi enviada
            mock_channel.basic_publish.assert_called()

class TestConsumer(unittest.TestCase):
    @patch('consumer.pika.BlockingConnection')
    @patch('consumer.pika.ConnectionParameters')
    @patch('consumer.pika.PlainCredentials')
    def test_consumer_env_vars(self, mock_creds, mock_params, mock_conn):
        with patch.dict('os.environ', {
            'RABBITMQ_USER': 'user',
            'RABBITMQ_PASSWORD': 'pass',
            'RABBITMQ_HOST': 'localhost',
            'RABBITMQ_QUEUE': 'fila_exemplo',
        }):
            # Simula conexão e canal
            mock_channel = MagicMock()
            mock_conn.return_value.channel.return_value = mock_channel
            # Simula start_consuming
            mock_channel.start_consuming.side_effect = KeyboardInterrupt
            import importlib
            importlib.reload(consumer)
            mock_channel.basic_consume.assert_called()

if __name__ == '__main__':
    unittest.main()
