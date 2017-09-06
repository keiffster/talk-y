import unittest

from talky.clients.voice.tts.osxsay import OSXSayTextToSpeach
from talky.config.sections.client.voice.voice import VoiceConfiguration


class OSXSayTextToSpeachTests(unittest.TestCase):

    def test_init(self):
        config = VoiceConfiguration()
        tts = OSXSayTextToSpeach(config)
        self.assertIsNotNone(tts)
