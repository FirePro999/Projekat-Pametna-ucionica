procena = 0
concentration = 0
ratio = 0
lowpulseoccupancy = 0
duration = pins.pulse_in(DigitalPin.P0, PulseValue.LOW)
sampletime_ms = 10000
startime = control.millis()
serial.set_baud_rate(BaudRate.BAUD_RATE9600)

def on_forever():
    global duration, lowpulseoccupancy, ratio, concentration, startime, procena
    duration = pins.pulse_in(DigitalPin.P0, PulseValue.LOW)
    lowpulseoccupancy = lowpulseoccupancy + duration
    if control.millis() - startime > sampletime_ms:
        ratio = lowpulseoccupancy / (sampletime_ms * 10)
        concentration = 1.1 * ratio ** 3 - 3.8 * ratio ** 2 + 520 * ratio + 0.62
        lowpulseoccupancy = 0
        startime = control.millis()
        procena = Math.floor(concentration)
        if procena <= 2500:
            basic.show_number(procena)
            basic.show_icon(IconNames.YES)
        elif procena > 2500 and procena <= 18000:
            basic.show_number(procena)
            basic.show_icon(IconNames.ASLEEP)
        else:
            basic.show_number(procena)
            basic.show_icon(IconNames.SKULL)
basic.forever(on_forever)
