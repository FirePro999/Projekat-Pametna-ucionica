light2 = 0

def on_gesture_shake():
    for index in range(2):
        music.play_melody("A E A E A E A E ", 120)
        music.rest(music.beat(BeatFraction.DOUBLE))
        music.play_melody("E A E A E A E E ", 120)
input.on_gesture(Gesture.SHAKE, on_gesture_shake)

def on_forever():
    global light2
    light2 = input.light_level()
    if light2 < 100:
        pins.digital_write_pin(DigitalPin.P1, 1)
    else:
        pins.digital_write_pin(DigitalPin.P1, 0)
    basic.show_number(light2)
basic.forever(on_forever)