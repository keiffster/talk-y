@echo off

CLS

ECHO This Bot has additional dependencies on Python libraries
ECHO Have you run pip install -r requirements.txt ?

python -m talky.clients.voice.speech --config ..\..\config\windows\config.yaml --cformat yaml --logging ..\..\config\windows\logging.yaml
