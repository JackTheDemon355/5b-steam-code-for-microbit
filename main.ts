input.onButtonPressed(Button.A, function () {
    if (Time == 1) {
        // Only run this code if the intro is finished
        if (can_start) {
            // Put your game start code or first question here!
            basic.showIcon(IconNames.Yes)
        }
    }
})
input.onButtonPressed(Button.B, function () {
    if (can_start == false) {
        led.stopAnimation()
        for (let index = 0; index < 9999; index++) {
            basic.clearScreen()
        }
        Time = 1
    }
})
let can_start = false
let Time = 0
Time = 0
can_start = false
// --- Intro Sequence ---
basic.showString("Hello. Let's test your IQ in this fun game!")
basic.pause(2000)
basic.showString("5 questions per round. 4 rounds.")
basic.pause(2000)
basic.showString("OK LETS GO!")
basic.pause(2000)
basic.showString("Click A to start.")
// Enable button A actions now that intro is done
can_start = true
Time = 1
basic.forever(function () {
    if (Time == 1) {
        // Only run this code if the intro is finished
        if (can_start) {
            // Put your game start code or first question here!
            basic.showIcon(IconNames.Yes)
        }
    }
})
