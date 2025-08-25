"""

Note: The variable "black_line" is used as a reference for the micro:bot to determine what it is driving on.

"""

def on_button_pressed_a():
    global black_line
    black_line = pins.analog_read_pin(AnalogReadWritePin.P1)
    serial.write_string("black_line_(i.e._Baseline_Value_of_Line_Following_Sensor_on_P1)=")
    serial.write_line("" + str((black_line)))
input.on_button_pressed(Button.A, on_button_pressed_a)

current_surface_reading = 0
black_line = 0
serial.redirect_to_usb()
motobit.invert(Motor.LEFT, True)
motobit.invert(Motor.RIGHT, True)
black_line = pins.analog_read_pin(AnalogReadWritePin.P1)
serial.write_string("black_line_(i.e._Baseline_Value_of_Line_Following_Sensor_on_P1)=")
serial.write_line("" + str((black_line)))
"""

Note: If the line following sensor connected to P1 sees a black line, move backward and pivot to the left. We'll need to take a few more steps back to make sure that we do not get stuck in the same place. The reading can vary depending on the material that you are using for a black line. For black electrical tape, this is about ~800.

It takes a few more seconds for the micro:bit to react when using the LED array and sending serial data. We'll want short delays so that there is enough time for the micro:bot to read the surface.

"""
"""

Note: This part of the code drives the micro:bot forward slowly if we do not see a black line.

"""

def on_forever():
    global current_surface_reading
    current_surface_reading = pins.analog_read_pin(AnalogReadWritePin.P1)
    serial.write_line("" + str((current_surface_reading)))
    #if encounter color set
    if current_surface_reading < black_line - 70 or current_surface_reading > black_line + 70:
        motobit.enable(MotorPower.ON)
        motobit.set_motor_speed(Motor.LEFT, MotorDirection.REVERSE, 40)
        motobit.set_motor_speed(Motor.RIGHT, MotorDirection.REVERSE, 40)
        basic.show_leds("""
            . # . # .
            . # # # .
            # # # # #
            . # # # .
            . . # . .
            """)
        basic.pause(10)
        motobit.set_motor_speed(Motor.LEFT, MotorDirection.REVERSE, 30)
        motobit.set_motor_speed(Motor.RIGHT, MotorDirection.FORWARD, 40)
        basic.show_leds("""
            # # # . .
            # # . . .
            # . # . .
            . . # . .
            . . # . .
            """)
        basic.pause(5)
        motobit.enable(MotorPower.OFF)
    else:
        motobit.enable(MotorPower.ON)
        motobit.set_motor_speed(Motor.LEFT, MotorDirection.FORWARD, 40)
        motobit.set_motor_speed(Motor.RIGHT, MotorDirection.FORWARD, 40)
        basic.show_leds("""
            . . # . .
            . # # # .
            # . # . #
            . . # . .
            . . # . .
            """)
        basic.pause(5)
        motobit.enable(MotorPower.OFF)
basic.forever(on_forever)
