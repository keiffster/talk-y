import unittest

from programy.config.file.yaml_file import YamlConfigurationFile
from talky.config.sections.client.voice.voice import VoiceConfiguration
from talky.config.sections.client.voice.stt.azhang import AnthonyZhangSpeechToTextConfiguration

class TestAnythongZhangSpeechToTextConfiguration(unittest.TestCase):

    def test_init(self):
        yaml = YamlConfigurationFile()
        self.assertIsNotNone(yaml)
        yaml.load_from_text("""
            voice:
              stt: azhang
              azhang:
                classname: talky.clients.voice.stt.azhang.AnthonyZhangSpeechToText
                ambient_adjust: 2
                service: google
        """, VoiceConfiguration(), ".")

        config = VoiceConfiguration()
        self.assertIsNotNone(config)
        config.load_config_section(yaml, ".")

        self.assertIsNotNone(config.stt_engine)
        self.assertIsInstance(config.stt_engine, AnthonyZhangSpeechToTextConfiguration)
        self.assertIsNotNone(config.stt_engine.classname)
        self.assertEqual("talky.clients.voice.stt.azhang.AnthonyZhangSpeechToText", config.stt_engine.classname)
        self.assertEqual(2, config.stt_engine.ambient_adjust)