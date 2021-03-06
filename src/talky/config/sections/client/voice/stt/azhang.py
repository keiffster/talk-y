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

from talky.config.sections.client.voice.engine import VoiceEngineBaseConfigurationData

class AnthonyZhangSpeechToTextConfiguration(VoiceEngineBaseConfigurationData):
    
    def __init__(self):
        VoiceEngineBaseConfigurationData.__init__(self, "azhang")
        self._ambient_adjust = 0
        self._service = None

    @property
    def ambient_adjust(self):
        return self._ambient_adjust

    @property
    def service(self):
        return self._service

    def load_additional(self, config_file, config_section, bot_root):
        self._ambient_adjust = config_file.get_int_option(config_section, "ambient_adjust", missing_value=2)
        self._service = config_file.get_option(config_section, "service")
