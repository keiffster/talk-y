import unittest

from programy.clients.voice.speech import ConversationBotClient

from test.clients.arguments import MockArgumentParser

class ConversationBotClientTests(unittest.TestCase):

    def test_init(self):
        arguments = MockArgumentParser()
        with self.assertRaises(Exception):
            bot = ConversationBotClient(arguments)
