from microbit import *
import radio

radio.on()

KAPACITET_PROSTORIJE = 10
br_mesta = KAPACITET_PROSTORIJE
pin0.set_analog_period(10)  # za upravljanje pinom 0 – elektricna brava

while True:
    if br_mesta > 0:
        display.show(str(br_mesta))
    else:
        display.scroll("Puna prostorija!")

    poruka = radio.receive()
    if poruka == "ulaz":
        if br_mesta > 0:
            pin0.write_analog(150)  # otkljucaj bravu
            sleep(5000)
            pin0.write_analog(60)  # zakljucaj bravu
            br_mesta -= 1
    elif poruka == "izlaz":
        if br_mesta < KAPACITET_PROSTORIJE:
            pin0.write_analog(150)  # otkljucaj bravu
            sleep(5000)
            pin0.write_analog(60)  # zakljucaj bravu
            br_mesta += 1
    elif poruka == "izlaz-ulaz":
        pin0.write_analog(150)  # otkljucaj bravu
        sleep(5000)
        pin0.write_analog(60)  # zakljucaj bravu
    sleep(500)
