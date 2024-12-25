from .types import ExchangeTypes


class Connection:
    EXCHANGE = 'chatroom'
    TYPE = ExchangeTypes.FANOUT

    def __init__(self, channel, parser, callback):
        self._channel = channel
        self._parser = parser
        self._callback = callback

    def setup(self):
        self._channel.exchange_declare(exchange=self.EXCHANGE, exchange_type=self.TYPE)
        self._queue = self._channel.queue_declare(queue='', exclusive=True).method.queue
        self._channel.queue_bind(exchange=self.EXCHANGE, queue=self._queue)

    def send(self, message):
        body = self._parser.to_body(message)
        self._channel.basic_publish(exchange=self.EXCHANGE, routing_key=self._queue, body=body)

    def receive(self, channel, method, properties, body):
        message = self._parser.to_message(body)
        self._callback(message)

    def wait_for_messages(self):
        self._channel.basic_consume(
            queue=self._queue, on_message_callback=self.receive, auto_ack=True
        )
        self._channel.start_consuming()
