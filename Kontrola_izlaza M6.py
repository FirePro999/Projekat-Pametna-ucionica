from microbit import *
import radio

radio.on()

display.scroll("Za privremeni izlazak pritisni taster B")
display.scroll("a za napustanje prostorije taster A")

while True:
    if button_a.was_pressed():
        display.scroll("Vidimo se sutra!")
        radio.send("izlaz")
    if button_b.was_pressed():
        display.scroll("Privremeni izlazak")
        radio.send("izlaz-ulaz")
    sleep(1000)
