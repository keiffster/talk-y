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

import logging
import speech_recognition as sr

from talky.clients.voice.stt.base import SpeechToText

class AnthonyZhangSpeechToText(SpeechToText):

    def __init__(self, configuration):
        SpeechToText.__init__(self, configuration)
        print("Initialising Google Speech To Text Engine...")
        self.record = sr.Recognizer()

        print('Calibrating microphone...')
        with sr.Microphone() as source:
            self.record.adjust_for_ambient_noise(source, self.configuration.stt_engine.ambient_adjust)

        print(("Listening using: [%s]" % self.configuration.stt_engine.service))

    def listen(self):
        with sr.Microphone() as source:
            try:
                if logging.getLogger().isEnabledFor(logging.DEBUG): logging.debug("Listening using: [%s]"%self.configuration.stt_engine.service)
                audio = self.record.listen(source)
                if self.configuration.stt_engine.service == 'sphinx':
                    recordedSpeech =  self.record.recognize_sphinx(audio, language='en-US')
                elif self.configuration.stt_engine.service == 'google':
                    recordedSpeech = self.record.recognize_google(audio, language='en-US')
                elif self.configuration.stt_engine.service == 'google_cloud':
                    recordedSpeech = self.record.recognize_google_cloud(audio)
                elif self.configuration.stt_engine.service == 'wit':
                    recordedSpeech = self.record.recognize_wit(audio, key='XXX')
                elif self.configuration.stt_engine.service == 'bing':
                    recordedSpeech = self.stt_enginerecord.recognize_bing(audio)
                elif self.configuration.stt_engine.service == 'houndify':
                    recordedSpeech = self.record.recognize_houndify(audio)
                elif self.configuration.stt_engine.service == 'ibm':
                    recordedSpeech = self.record.recognize_ibm(audio, username='xxx', password='xxx')
                else:
                    if logging.getLogger().isEnabledFor(logging.ERROR): logging.error("Unknown sst service [%s]" % self.configuration.stt_engine.service)
                    recordedSpeech = ""
                if logging.getLogger().isEnabledFor(logging.DEBUG): logging.debug ("Heard [%s]"%recordedSpeech)
                return recordedSpeech
            except LookupError as e:
                logging.exception(e)
            except sr.UnknownValueError:
                if logging.getLogger().isEnabledFor(logging.ERROR): logging.error("Google Speech Recognition could not understand audio")
            except sr.RequestError as e:
                if logging.getLogger().isEnabledFor(logging.ERROR): logging.error("Could not request results from Speech Recognition service; {0}".format(e))
        return None
