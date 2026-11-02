input.onButtonPressed(Button.A, function () {
    // Only run this code if the intro is finished
    if (can_start) {
        // Put your game start code or first question here!
        basic.showIcon(IconNames.Yes)
    }
})
let can_start = false
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
