import pika


class ChannelFactory:
    @classmethod
    def create(cls, hostname):
        connection = pika.BlockingConnection(pika.ConnectionParameters(hostname))
        return connection.channel()
