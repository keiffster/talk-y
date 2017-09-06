#!/usr/bin/env bash

clear

export PYTHONPATH=./src:../program-y/src:../program-y/test/:../program-y/libs/MetOffer-1.3.2:.

nosetests --with-coverage --cover-erase --with-xunit --cover-branches --cover-package=talky

coverage html -d cover
