"""
Using a Kitronik ZIP Halo HD

Display a rainbow: 
light colors rotate and change brightness.
"""

haloDisplay = kitronik_halo_hd.create_zip_halo_display(60)
haloDisplay.show_rainbow(1, 360)
brightness = 255
brightnessDirection = -1
MAX_BRIGHTNESS = 180
MIN_BRIGHTNESS = 10
BRIGHTNESS_STEPS = 10
COLOR_STEPS = 5

def on_forever():
    global brightness, brightnessDirection
    haloDisplay.rotate(COLOR_STEPS)
    haloDisplay.show()
    basic.pause(100)
    if brightnessDirection == -1:
        brightness += -1 * BRIGHTNESS_STEPS
    else:
        brightness += 1 * BRIGHTNESS_STEPS
    if brightness < MIN_BRIGHTNESS:
        brightness = MIN_BRIGHTNESS
        brightnessDirection = 1
    elif brightness > MAX_BRIGHTNESS:
        brightness = MAX_BRIGHTNESS
        brightnessDirection = -1
    haloDisplay.set_brightness(brightness)
basic.forever(on_forever)

