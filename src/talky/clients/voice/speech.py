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
import os

from programy.clients.client import BotClient
from talky.config.sections.client.voice.voice import VoiceConfiguration
from talky.clients.voice.tts.osxsay import OSXSayTextToSpeech
from talky.clients.voice.stt.azhang import AnthonyZhangSpeechToText
from talky.utils.wav import play_wav

class ConversationBotClient(BotClient):
    def __init__(self, argument_parser=None):
        self.clientid = "Voice"
        BotClient.__init__(self, argument_parser)

        if self.configuration.client_configuration.tts_engine_name is None:
            raise Exception("No Text To Speech Engine, exiting...")

        print("Text To Speech: " + self.configuration.client_configuration.tts_engine_name )
        if self.configuration.client_configuration.tts_engine_name == 'osx':
            self.tts = OSXSayTextToSpeech(self.configuration.client_configuration)
        elif self.configuration.client_configuration.tts_engine_name == 'pyttsx':
            self.tts = OSXSayTextToSpeech(self.configuration.client_configuration)
        else:
            raise Exception("Unknown Text To Speech Engine, exiting...")

        if self.configuration.client_configuration.stt_engine_name is None:
            raise Exception("No Speech To Text Engine, exiting...")

        print("Speech To Text: " + self.configuration.client_configuration.stt_engine_name)
        if self.configuration.client_configuration.stt_engine_name == 'azhang':
            self.stt = AnthonyZhangSpeechToText(self.configuration.client_configuration)
        else:
            raise Exception("Unknown Speech To Text Engine, exiting...")

    def set_environment(self):
        self.bot.brain.properties.add_property("env", "Conversation")

    def get_client_configuration(self):
        return VoiceConfiguration()

    def run(self):
        try:
            if self.arguments.noloop is False:
                logging.info("Entering conversation loop...")

                client_context = self.create_client_context("speechy")
                self.display_response(client_context.bot.get_version_string(client_context))

                # show and speak default response
                default_response = client_context.brain.post_process_response(client_context, client_context.bot.initial_question)
                #self.display_response(default_response)
                #self.tts.say(default_response)

            play_wav('../../resources/audio/welcome.wav')

            running = True
            while running is True:
                print("I'm listening...")
                speechRecorded = self.stt.listen()

                if speechRecorded is not None and len(speechRecorded) > 0:

                    if speechRecorded.upper() == "COMPUTER":
                        print("Waiting for command...")
                        play_wav('../../resources/audio/beep.wav')

                        try:
                            speechRecorded = self.stt.listen()
                            if speechRecorded is not None and len(speechRecorded) > 0:
                                print("Heard: [%s]"%speechRecorded)
                                if logging.getLogger().isEnabledFor(logging.DEBUG): logging.debug("Recorded [%s]"%speechRecorded)
                                response = client_context.bot.ask_question(client_context, speechRecorded)
                                if response is None:
                                    self.tts.say(self.bot.default_response)
                                    self.log_unknown_response(speechRecorded)
                                else:
                                    self.tts.say(response)
                                    self.log_response(speechRecorded, response)
                                    self.display_response(response)

                        except KeyboardInterrupt:
                            running = False
                            self.display_response(self.bot.exit_response)

                        except Exception as excep:
                            logging.exception(excep)
                            print("Oops something bad happened !")
                            print(excep)
                            self.display_response(self.bot.default_response)

        # error occured when user has no microphone
        except OSError:
            if logging.getLogger().isEnabledFor(logging.ERROR): logging.error("\nNo default input devices available.")

    def get_question(self, input_func=input):
        ask = "%s " % self.bot.prompt
        return input_func(ask)

    def display_response(self, response, output_func=print):
        output_func(response)


if __name__ == '__main__':
    def run():
        print("Loading, please wait...")
        console_app = ConversationBotClient()
        console_app.run()


    run()