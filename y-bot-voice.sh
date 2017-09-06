#! /bin/sh

clear

export PYTHONPATH=./src:../program-y/src:../program-y/libs/MetOffer-1.3.2:.

python3 ./src/talky/clients/voice/speech.py --config ../program-y/bots/y-bot/config.yaml --cformat yaml --logging ../program-y/bots/y-bot/logging.yaml

