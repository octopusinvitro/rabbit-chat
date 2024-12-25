from rabbitchat.parser import Parser


class TestParserToBody:
    def test_parses_a_message_into_json_including_the_username(self):
        parser = Parser('testuser')
        assert parser.to_body('hi') == '{"username": "testuser", "message": "hi"}'

    def test_supports_empty_messages(self):
        parser = Parser('user')
        assert parser.to_body('') == '{"username": "user", "message": ""}'

    def test_supports_empty_username(self):
        parser = Parser(None)
        assert parser.to_body('ghost') == '{"username": null, "message": "ghost"}'


class TestParserToMessage:
    def test_parses_encoded_bytes_to_display_text_with_user_and_message(self):
        parser = Parser('testuser')
        body = '{"username": "testuser", "message": "hi"}'.encode('utf-8')
        assert parser.to_message(body) == 'testuser: hi'

    def test_supports_empty_messages(self):
        parser = Parser('user')
        body = '{"username": "user", "message": ""}'.encode('utf-8')
        assert parser.to_message(body) == 'user: '

    def test_supports_empty_username(self):
        parser = Parser(None)
        body = '{"username": null, "message": "ghost"}'.encode('utf-8')
        assert parser.to_message(body) == ': ghost'
