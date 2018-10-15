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

import os
import logging

from talky.clients.voice.tts.base import TextToSpeech

class OSXSayTextToSpeech(TextToSpeech):

    def __init__(self, configuration):
        TextToSpeech.__init__(self, configuration)
        if logging.getLogger().isEnabledFor(logging.DEBUG): logging.debug("Initialising OSX Native Text To Speech Engine...")

    def say(self, text):
        if text is not None and len(text) > 0:
            if logging.getLogger().isEnabledFor(logging.DEBUG): logging.debug("Saying [%s]" % text)
            try:
                os.system('say "%s"'%text)
            except Exception as e:
                logging.exception(e)
