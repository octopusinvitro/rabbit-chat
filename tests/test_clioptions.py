import pytest

from rabbitchat.clioptions import CLIOptions


class TestCLIOptions:
    def test_accepts_valid_username_and_optional_hostname(self):
        options = CLIOptions(['-u', 'testuser', '-o', 'testhost'])
        assert options.username == 'testuser'
        assert options.hostname == 'testhost'

    def test_accepts_valid_username_and_no_hostname(self):
        options = CLIOptions(['-u', 'testuser'])
        assert options.username == 'testuser'
        assert options.hostname == CLIOptions.DEFAULT_HOSTNAME

    def test_detects_missing_required_username(self):
        with pytest.raises(SystemExit):
            CLIOptions(['-o', 'testhost'])

    def test_detects_missing_all_arguments(self):
        with pytest.raises(SystemExit):
            CLIOptions([])

    def test_detects_invalid_flag(self):
        with pytest.raises(SystemExit):
            CLIOptions(['--invalid', 'value'])
