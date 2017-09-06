import unittest

from programy.clients.voice.stt.azhang import AnthonyZhangSpeechToText
from programy.config.sections.client.voice.voice import VoiceConfiguration
from programy.config.sections.client.voice.stt.azhang import AnthonyZhangSpeechToTextConfiguration

class AnthonyZhangSpeechToTextTests(unittest.TestCase):

    def test_init(self):
        config = VoiceConfiguration()
        config._stt_engine = AnthonyZhangSpeechToTextConfiguration()
        stt = AnthonyZhangSpeechToText(config)
