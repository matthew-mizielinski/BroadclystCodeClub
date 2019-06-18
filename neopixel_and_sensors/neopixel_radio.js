// Need to import Neopixel extension first.
function get_pitch () {
    pitch = Math.map(input.rotation(Rotation.Pitch), 0, 360, 0, 120)
}
function get_roll () {
    roll = Math.map(input.rotation(Rotation.Roll), 0, 360, 0, 120)
}
radio.onReceivedValue(function (name, value) {
    if (name == "pitch") {
        received_pitch = value
    } else if (name == "roll") {
        received_roll = value
    }
})
let received_roll = 0
let received_pitch = 0
let roll = 0
let pitch = 0
radio.setGroup(1)
let strip = neopixel.create(DigitalPin.P0, 1, NeoPixelMode.RGB)
basic.forever(function () {
    get_pitch()
    radio.sendValue("pitch", pitch)
    get_roll()
    radio.sendValue("roll", roll)
    basic.pause(100)
    strip.showColor(neopixel.rgb(received_pitch, 0, received_roll))
    strip.show()
})
