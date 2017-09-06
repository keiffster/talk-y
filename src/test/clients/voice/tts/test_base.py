import unittest

from programy.clients.voice.tts.base import TextToSpeech
from programy.config.sections.client.voice.voice import VoiceConfiguration

class TextToSpeechTests(unittest.TestCase):

    def test_init(self):
        config = VoiceConfiguration()
        tts = TextToSpeech(config)
        self.assertIsNotNone(tts)
        self.assertIsNotNone(tts.configuration)
        self.assertEquals(config, tts.configuration)

        with self.assertRaises(Exception):
            tts.say()