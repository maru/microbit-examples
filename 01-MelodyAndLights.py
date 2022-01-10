"""
First example!

micro:bit plays a melody when button A is pressed.
Melody stops when button B is pressed.

The mic is on, so a heart is displayed or the screen is cleared when a sound is
heard.
"""


def on_button_pressed_a():
    while musicOn:
        music.play_melody("A F E F D G E F ", 418)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_sound_loud():
    global lightsOn
    lightsOn = not (lightsOn)
    if lightsOn:
        basic.show_leds("""
            . # . # .
            # # # # #
            # # # # #
            . # # # .
            . . # . .
        """)
    else:
        basic.clear_screen()
input.on_sound(DetectedSound.LOUD, on_sound_loud)

def on_button_pressed_b():
    global musicOn
    musicOn = not (musicOn)
input.on_button_pressed(Button.B, on_button_pressed_b)

lightsOn = False
musicOn = False
input.set_sound_threshold(SoundThreshold.LOUD, 35)
