from microbit import pin0, sleep
import neopixel

np = neopixel.NeoPixel(pin0, 25)

colours = [
    (100, 0, 0),
    (50, 50, 0),
    (0, 100, 0),
    (0, 50, 50),
    (0, 0, 100),
    (50, 0, 50),
]

while True:
    for colour in colours:
        for row in range(5):
            for col in range(5):
                index = col * 5 + row
                np[index] = colour
                np.show()
                sleep(100)
        np.clear()
    
