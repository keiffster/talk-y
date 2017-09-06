import unittest

from programy.clients.voice.tts.osxsay import OSXSayTextToSpeach
from programy.config.sections.client.voice.voice import VoiceConfiguration


class OSXSayTextToSpeachTests(unittest.TestCase):

    def test_init(self):
        config = VoiceConfiguration()
        tts = OSXSayTextToSpeach(config)
        self.assertIsNotNone(tts)
