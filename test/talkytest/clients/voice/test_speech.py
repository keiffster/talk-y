import unittest

from talky.clients.voice.speech import ConversationBotClient

from programytest.clients.arguments import MockArgumentParser

class ConversationBotClientTests(unittest.TestCase):

    def test_init(self):
        arguments = MockArgumentParser()
        with self.assertRaises(Exception):
            bot = ConversationBotClient(arguments)
