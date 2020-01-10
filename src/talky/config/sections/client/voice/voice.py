"""
Copyright (c) 2016-17 Keith Sterling http://www.keithsterling.com

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated
documentation files (the "Software"), to deal in the Software without restriction, including without limitation
the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software,
and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO
THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT,
TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
"""

from programy.clients.config import ClientConfigurationData
from talky.config.sections.client.voice.tts.pytts import PyTTSTextToSpeechConfiguration
from talky.config.sections.client.voice.stt.azhang import AnthonyZhangSpeechToTextConfiguration

class VoiceConfiguration(ClientConfigurationData):

    def __init__(self):
        ClientConfigurationData.__init__(self, "voice")
        self._tts_engine_name = None
        self._stt_engine_name = None
        self._tts_engine = None
        self._stt_engine = None

    @property
    def tts_engine(self):
        return self._tts_engine

    @property
    def tts_engine_name(self):
        return self._tts_engine_name

    @property
    def stt_engine(self):
        return self._stt_engine

    @property
    def stt_engine_name(self):
        return self._stt_engine_name

    def load_configuration(self, configuration_file, bot_root):
        voice = configuration_file.get_section(self.section_name)
        if voice is not None:

            self._tts_engine_name = configuration_file.get_option(voice, "tts", missing_value=None)
            if self._tts_engine_name == 'pytts':
                self._tts_engine = PyTTSTextToSpeechConfiguration()
                self._tts_engine.load_config_sub_section(configuration_file, voice, bot_root)

            self._stt_engine_name = configuration_file.get_option(voice, "stt", missing_value=None)
            if self._stt_engine_name == 'azhang':
                self._stt_engine = AnthonyZhangSpeechToTextConfiguration()
                self._stt_engine.load_config_sub_section(configuration_file, voice, bot_root)

        super(VoiceConfiguration, self).load_configuration(configuration_file, voice, bot_root)
