def on_received_string(receivedString):
    for index in range(2):
        music.play_melody("A E A E A E A E ", 120)
        music.rest(music.beat(BeatFraction.DOUBLE))
        music.play_melody("E A E A E A E E ", 120)
radio.on_received_string(on_received_string)

def on_gesture_shake():
    for index2 in range(2):
        music.play_melody("A E A E A E A E ", 120)
        music.rest(music.beat(BeatFraction.DOUBLE))
        music.play_melody("E A E A E A E E ", 120)
input.on_gesture(Gesture.SHAKE, on_gesture_shake)

svetlo2 = 0
radio.set_group(99)

def on_forever():
    global svetlo2
    svetlo2 = input.light_level()
    if svetlo2 < 100:
        pins.digital_write_pin(DigitalPin.P1, 1)
    else:
        pins.digital_write_pin(DigitalPin.P1, 0)
    basic.show_number(svetlo2)
basic.forever(on_forever)
