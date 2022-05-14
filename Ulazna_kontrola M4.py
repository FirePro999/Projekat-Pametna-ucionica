from microbit import *
import radio

radio.on()

display.scroll("Za prvi ulazak pritisni taster A")
display.scroll("a ako se vracas u prostoriju pritisni taster B")

while True:
    if button_a.was_pressed():
        display.scroll("Zdravo - dobro dosao!")
        radio.send("ulaz")

    if button_b.was_pressed():
        display.scroll("Povratak")
        radio.send("izlaz-ulaz")
    sleep(1000)
