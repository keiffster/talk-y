
First we need XCode Command Line Tool, with the following command

xcode-select --install

If not installed then you will be run through the XCode install, alternatively if you have already installed them,
then you will be informed to use 'Software Updates' which means opening XCode and following the instructions that
pop up about installing additional components


Next we need to install OSX dependencies. I use Homebrew for dependency management, other package managers exist.

brew install portaudio
brew install swig

Finally we can install the required Python 3 packages

pip3 install pyttsx3
pip3 install pyAudio
pip3 install SpeechRecognition
pip3 install pocketsphinx 

And that should be it,