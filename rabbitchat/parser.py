import json


class Parser:
    def __init__(self, username):
        self._username = username

    def to_body(self, message):
        return json.dumps({
            'username': self._username,
            'message': message
        })

    def to_message(self, body):
        data = json.loads(body.decode('utf-8'))
        username = data.get('username') or ''
        message = data.get('message') or ''

        return f'{username}: {message}'
