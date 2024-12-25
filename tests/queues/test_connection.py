from pika.adapters.blocking_connection import BlockingChannel

from unittest import mock, TestCase

from rabbitchat.queues.connection import Connection
from rabbitchat.parser import Parser


class TestConnection(TestCase):
    def setUp(self):
        self.channel_spy = mock.create_autospec(BlockingChannel, instance=True)
        self.callback_spy = mock.MagicMock()
        self.connection = Connection(self.channel_spy, Parser('testuser'), self.callback_spy)

        self.connection.setup()

    def test_sends_correctly_formatted_messages(self):
        self.connection.send('Hello')
        self.channel_spy.basic_publish.assert_called_once_with(
            exchange=Connection.EXCHANGE,
            routing_key=mock.ANY,
            body='{"username": "testuser", "message": "Hello"}'
        )

    def test_runs_custom_callback_when_it_receives_a_message(self):
        body = b'{"username": "testuser", "message": "bye"}'
        self.connection.receive(None, None, None, body)
        self.callback_spy.assert_called_once_with('testuser: bye')

    def test_sets_up_for_consuming_with_receive_method_as_callback(self):
        self.connection.wait_for_messages()
        self.channel_spy.basic_consume.assert_called_once_with(
            queue=mock.ANY,
            on_message_callback=self.connection.receive,
            auto_ack=mock.ANY
        )
