def on_received_string(receivedString):
    global p
    p += 1
    if p <= 1:
        basic.show_string("Dron aktiviran!")
        kitronik_smart_greenhouse.control_high_power_pin(kitronik_smart_greenhouse.HighPowerPins.PIN13,
            kitronik_smart_greenhouse.on_off(True),
            45)
        basic.pause(2100)
        kitronik_smart_greenhouse.control_high_power_pin(kitronik_smart_greenhouse.HighPowerPins.PIN13,
            kitronik_smart_greenhouse.on_off(False))
    else:
        basic.show_string("Akcija u toku!")
radio.on_received_string(on_received_string)

p = 0
radio.set_group(99)
p = 0
svetla = neopixel.create(DigitalPin.P0, 24, NeoPixelMode.RGB)
svetla.show_rainbow(1, 360)

def on_forever():
    if p == 0:
        svetla.set_brightness(10)
        svetla.show()
        basic.pause(200)
        svetla.rotate(1)
        pins.analog_write_pin(AnalogPin.P2, 404)
    else:
        svetla.set_brightness(100)
        svetla.show()
        svetla.rotate(4)
        pins.analog_write_pin(AnalogPin.P2, randint(200, 1000))
basic.forever(on_forever)
