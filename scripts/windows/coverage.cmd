@echo off

SUBST Y: /D
SUBST Y: Z:\Development\Python\Projects\AIML\program-y
SUBST X: /D
SUBST X: Z:\Development\Python\Projects\AIML\talk-y

SET PYTHONPATH=X:\src;Y:\src;Y:\libs\MetOffer-1.3.2;Y:\bots\y-bot

nosetests --with-coverage --cover-erase --with-xunit --cover-branches --cover-package=talky

coverage html -d cover
