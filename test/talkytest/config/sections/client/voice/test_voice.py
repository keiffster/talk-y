import unittest

from programy.config.file.yaml_file import YamlConfigurationFile
from talky.config.sections.client.voice.voice import VoiceConfiguration
from talky.config.sections.client.voice.stt.azhang import AnthonyZhangSpeechToTextConfiguration
from talky.config.sections.client.voice.tts.pytts import PyTTSTextToSpeechConfiguration


class TestAnthonyZangSpeechToTextConfiguration(unittest.TestCase):

    def test_init(self):
        yaml = YamlConfigurationFile()
        self.assertIsNotNone(yaml)
        yaml.load_from_text("""
            voice:
              tts: pytts
              stt: azhang
              pytts:
                classname: talky.clients.voice.tts.pyttssay.PyTTSSayTextToSpeach
                rate_adjust: 50
              azhang:
                classname: talky.clients.voice.stt.azhang.AnthonyZangWebServiceSpeechToText
                ambient_adjust: 2
        """, VoiceConfiguration(), ".")

        config = VoiceConfiguration()
        self.assertIsNotNone(config)
        config.load_config_section(yaml, ".")

        self.assertIsNotNone(config.stt_engine)
        self.assertIsInstance(config.stt_engine, AnthonyZhangSpeechToTextConfiguration)
        self.assertIsNotNone(config.stt_engine.classname)
        self.assertEqual("talky.clients.voice.stt.azhang.AnthonyZangWebServiceSpeechToText", config.stt_engine.classname)
        self.assertEqual(2, config.stt_engine.ambient_adjust)

        self.assertIsNotNone(config.tts_engine)
        self.assertIsInstance(config.tts_engine, PyTTSTextToSpeechConfiguration)
        self.assertIsNotNone(config.tts_engine.classname)
        self.assertEqual("talky.clients.voice.tts.pyttssay.PyTTSSayTextToSpeach", config.tts_engine.classname)
        self.assertEqual(50, config.tts_engine.rate_adjust)