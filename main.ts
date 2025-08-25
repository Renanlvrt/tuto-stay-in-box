/** Note: The variable "black_line" is used as a reference for the micro:bot to determine what it is driving on. */
input.onButtonPressed(Button.A, function on_button_pressed_a() {
    
    black_line = pins.analogReadPin(AnalogReadWritePin.P1)
    serial.writeString("black_line_(i.e._Baseline_Value_of_Line_Following_Sensor_on_P1)=")
    serial.writeLine("" + ("" + black_line))
})
let current_surface_reading = 0
let black_line = 0
serial.redirectToUSB()
motobit.invert(Motor.Left, false)
motobit.invert(Motor.Right, false)
black_line = pins.analogReadPin(AnalogReadWritePin.P1)
serial.writeString("black_line_(i.e._Baseline_Value_of_Line_Following_Sensor_on_P1)=")
serial.writeLine("" + ("" + black_line))
/** 

Note: If the line following sensor connected to P1 sees a black line, move backward and pivot to the left. We'll need to take a few more steps back to make sure that we do not get stuck in the same place. The reading can vary depending on the material that you are using for a black line. For black electrical tape, this is about ~800.

It takes a few more seconds for the micro:bit to react when using the LED array and sending serial data. We'll want short delays so that there is enough time for the micro:bot to read the surface.


 */
/** Note: This part of the code drives the micro:bot forward slowly if we do not see a black line. */
// motobit.enable(MotorPower.OFF)
basic.forever(function on_forever() {
    
    current_surface_reading = pins.analogReadPin(AnalogReadWritePin.P1)
    serial.writeLine("" + ("" + current_surface_reading))
    // if encounter color set (now not white)
    // if current_surface_reading < black_line - 100 or current_surface_reading > black_line + 100:
    if (current_surface_reading < 100 || current_surface_reading > 530) {
        motobit.enable(MotorPower.On)
        motobit.setMotorSpeed(Motor.Left, MotorDirection.Reverse, 60)
        motobit.setMotorSpeed(Motor.Right, MotorDirection.Reverse, 60)
        basic.showLeds(`
            . # . # .
            . # # # .
            # # # # #
            . # # # .
            . . # . .
            `)
        basic.pause(15)
        motobit.setMotorSpeed(Motor.Left, MotorDirection.Reverse, 30)
        motobit.setMotorSpeed(Motor.Right, MotorDirection.Forward, 40)
        basic.showLeds(`
            # # # . .
            # # . . .
            # . # . .
            . . # . .
            . . # . .
            `)
        basic.pause(5)
    } else {
        // motobit.enable(MotorPower.OFF)
        motobit.enable(MotorPower.On)
        motobit.setMotorSpeed(Motor.Left, MotorDirection.Forward, 70)
        motobit.setMotorSpeed(Motor.Right, MotorDirection.Forward, 70)
        basic.showLeds(`
            . . # . .
            . # # # .
            # . # . #
            . . # . .
            . . # . .
            `)
        basic.pause(5)
    }
    
})
