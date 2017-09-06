import unittest

from talky.clients.voice.tts.pyttssay import PyTTSSayTextToSpeach
from talky.config.sections.client.voice.voice import VoiceConfiguration
from talky.config.sections.client.voice.tts.pytts import PyTTSTextToSpeechConfiguration

class PyTTSSayTests(unittest.TestCase):

    @unittest.skip("PyTTS not supported on OSX yet, needs to be installed from source")
    def test_init(self):
        config = VoiceConfiguration()
        config._tts_engine = PyTTSTextToSpeechConfiguration()
        tts = PyTTSSayTextToSpeach(config)
        self.assertIsNotNone(tts)

