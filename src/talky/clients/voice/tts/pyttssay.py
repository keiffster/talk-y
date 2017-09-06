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

import pyttsx3
import os
import logging

from talky.clients.voice.tts.base import TextToSpeech

class PyTTSSayTextToSpeach(TextToSpeech):

    def __init__(self, configuration):
        TextToSpeech.__init__(self, configuration)
        if logging.getLogger().isEnabledFor(logging.DEBUG): logging.debug("Initialising PyTTS Text To Speech Engine...")
        self.engine = pyttsx3.init()
        if os.name == 'nt':
            voices = self.engine.getProperty('voices')
            self.engine.setProperty('voice', voices[1].id)
        rate = self.engine.getProperty('rate')
        self.engine.setProperty('rate', rate - 50)

    def say(self, text):
        if logging.getLogger().isEnabledFor(logging.DEBUG): logging.debug("Saying [%s]"%text)
        self.engine.say(text)
        self.engine.runAndWait()
