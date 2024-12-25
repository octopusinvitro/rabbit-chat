[![Python version](https://badgen.net/badge/python/3.10/yellow)](Pipfile)
[![License](https://img.shields.io/github/license/octopusinvitro/rabbit-chat)](https://github.com/octopusinvitro/rabbit-chat/blob/main/LICENSE.md)
[![Maintainability](https://api.codeclimate.com/v1/badges/cfd6bc8641452a4ac793/maintainability)](https://codeclimate.com/github/octopusinvitro/rabbit-chat/maintainability)


# README

This is a simple chat application that sets up a messaging system where multiple users can send and receive messages in real-time.


## Dependencies

* `pipenv` for dependency management,
* `pytest` as a testing framework,
* `tika` as the RabbitMQ client library for Python,
* `tkinter` for creating the chat interface, `tkinter` is included with Python

The bin folder has scripts for basic commands.


## To test

```sh
. bin/test                    # all tests
. bin/test tests/test_file.py # single test
```


## To lint

```sh
. bin/lint
```
