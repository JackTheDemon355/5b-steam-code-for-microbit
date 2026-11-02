def on_button_pressed_a():
    # Only run this code if the intro is finished
    if can_start:
        # Put your game start code or first question here!
        basic.show_icon(IconNames.YES)
input.on_button_pressed(Button.A, on_button_pressed_a)

can_start = False
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