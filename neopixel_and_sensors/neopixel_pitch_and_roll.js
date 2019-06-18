// Need to import Neopixel extension first
function get_pitch () {
    pitch = Math.map(input.rotation(Rotation.Pitch), 0, 360, 0, 120)
}
function get_roll () {
    roll = Math.map(input.rotation(Rotation.Roll), 0, 360, 0, 120)
}
let roll = 0
let pitch = 0
let strip = neopixel.create(DigitalPin.P0, 1, NeoPixelMode.RGB)
basic.forever(function () {
    get_pitch()
    get_roll()
    strip.showColor(neopixel.rgb(pitch, 0, roll))
    strip.show()
    basic.pause(100)
})
