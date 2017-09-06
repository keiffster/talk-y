import unittest

from programy.clients.voice.stt.base import SpeechToText
from programy.config.sections.client.voice.voice import VoiceConfiguration


class SpeechToTextTests(unittest.TestCase):

    def test_init(self):
        config = VoiceConfiguration()
        stt = SpeechToText(config)
        self.assertIsNotNone(stt)
        self.assertIsNotNone(stt.configuration)
        self.assertEquals(config, stt.configuration)

        with self.assertRaises(Exception):
            stt.listen()