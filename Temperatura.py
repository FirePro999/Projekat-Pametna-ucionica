temp = 0

def on_forever():
    global temp
    temp = input.temperature()
    basic.show_number(temp)
    if temp < 27:
        pins.analog_write_pin(AnalogPin.P0, 0)
    if temp >= 27:
        pins.analog_write_pin(AnalogPin.P0, 710)
    if temp >= 29:
        pins.analog_write_pin(AnalogPin.P0, 1023)
basic.forever(on_forever)
