plamen = 0
temp = 0
radio.set_group(99)

def on_forever():
    global temp, plamen
    temp = input.temperature()
    basic.show_number(temp)
    if temp < 27:
        pins.analog_write_pin(AnalogPin.P0, 0)
    if temp >= 27:
        pins.analog_write_pin(AnalogPin.P0, 710)
    if temp >= 29:
        pins.analog_write_pin(AnalogPin.P0, 1023)
    plamen = pins.analog_read_pin(AnalogPin.P2)
    if plamen < 150:
        radio.send_string("pozar")
        basic.show_leds("""
            # . . . .
                        # . # . .
                        # # # # .
                        # # # # .
                        # # # # #
        """)
        basic.pause(500)
        basic.show_leds("""
            . . . . #
                        . . # . #
                        . # # # #
                        . # # # #
                        # # # # #
        """)
basic.forever(on_forever)

def on_forever2():
    if plamen < 150:
        pins.digital_write_pin(DigitalPin.P1, 1)
        basic.pause(20000)
        pins.digital_write_pin(DigitalPin.P1, 0)
        basic.pause(500)
        pins.digital_write_pin(DigitalPin.P1, 1)
        basic.pause(200)
        pins.digital_write_pin(DigitalPin.P1, 0)
basic.forever(on_forever2)
