""" Importeer de modules die je wilt gebruiken """
import RPi.GPIO as GPIO
from time import sleep

""" Kies de manier van nummering in je script """
GPIO.setmode(GPIO.BOARD)

""" Configureer pin 3 om gebruikt te worden als output """
GPIO.setup(3, GPIO.OUT)

""" Starten van een oneindige lus """
while True:
    """ We activeren GPIO pin 3 en wachten voor 1 seconde """
    GPIO.output(3, GPIO.HIGH)
    sleep(1)

    """ We desactiveren GPIO pin 3 en wachten voor 1 seconde """
    GPIO.output(3, GPIO.LOW)
    sleep(1)
