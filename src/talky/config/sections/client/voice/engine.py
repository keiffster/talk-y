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

from programy.config.base import BaseConfigurationData

class VoiceEngineBaseConfigurationData(BaseConfigurationData):

    def __init__(self, name):
        BaseConfigurationData.__init__(self, name)
        self._classname = None

    @property
    def classname(self):
        return self._classname

    def load_config_sub_section(self, config_file, parent_section, bot_root):
        voice = config_file.get_section(self.section_name, parent_section)
        if voice is not None:
            self._classname = config_file.get_option(voice, "classname", missing_value=None)
            self.load_additional(config_file, voice, bot_root)

    def load_additional(self, config_file, config_section, bot_root):
        # Nothing to see here
        return