
def on_button_pressed_a():
    if Time == 1:
        # Only run this code if the intro is finished
        if can_start:
            # Put your game start code or first question here!
            basic.show_icon(IconNames.YES)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    global Time
    if can_start == False:
        led.stop_animation()
        for index in range(9999):
            basic.clear_screen()
        Time = 1
input.on_button_pressed(Button.B, on_button_pressed_b)

can_start = False
Time = 0
Time = 0
can_start = False
# --- Intro Sequence ---
basic.show_string("Hello. Let's test your IQ in this fun game!")
basic.pause(2000)
basic.show_string("5 questions per round. 4 rounds.")
basic.pause(2000)
basic.show_string("OK LETS GO!")
basic.pause(2000)
basic.show_string("Click A to start.")
# Enable button A actions now that intro is done
can_start = True
Time = 1

def on_forever():
    if Time == 1:
        # Only run this code if the intro is finished
        if can_start:
            # Put your game start code or first question here!
            basic.show_icon(IconNames.YES)
basic.forever(on_forever)
