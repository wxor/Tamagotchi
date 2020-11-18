def egg():
    basic.show_leds("""
        . . . . .
        . # # # .
        # . . . #
        # . . . #
        . # # # .
        """)
        
    basic.show_leds("""
        . # # # .
        # . . . #
        # . . . #
        . # # # .
        . . . . .
        """)
    eventcheck()

def stage1():
    basic.show_leds("""
        . . . . .
        . # # . .
        # # # # .
        # . . # .
        . . . . .
        """)
        
    basic.show_leds("""
        . . . . .
        . . # # .
        . # # # #
        . # . . #
        . . . . .
        """)
    eventcheck()

def stage2():
    basic.show_leds("""
        # # # # .
        # # # # .
        # . . # .
        # # # # .
        # . . # .
        """)
        
    basic.show_leds("""
        . # # # #
        . # # # #
        . # . . #
        . # # # #
        . # . . #
        """)
    eventcheck()

def death():
    basic.show_leds("""
        . # # # .
        # # . # #
        # . . . #
        . # # # .
        . # # # .
        """)

def select():

    basic.show_leds("""
        # # # # #
        # . . . #
        # . . . #
        # . . . #
        # # # # #
        """)
    basic.show_leds("""
        . . . . .
        . # # # .
        . # . # .
        . # # # .
        . . . . .
        """)
    basic.show_leds("""
        . . . . .
        . . . . .
        . . # . .
        . . . . .
        . . . . .
        """)

def on_button_pressed_a():
    global status
    global hunger
    global state
    if state == 3:
        basic.show_leds("""
            # . . . #
            . # . # .
            . . # . .
            . # . # .
            # . . . #
            """)
    elif state == 0:
        basic.show_leds("""
            # . . . #
            . # . # .
            . . # . .
            . # . # .
            # . . . #
            """)
    else:
        basic.show_leds("""
            . # . . .
            # # . . .
            . . # # #
            . . # # #
            . . # # #
            """)
        if hunger < 100:
            select()
            hunger = hunger + 10
            status = status - 10
        else:
            basic.show_leds("""
            # . . . #
            . # . # .
            . . # . .
            . # . # .
            # . . . #
            """)
    basic.show_string(" H:")
    basic.show_number(hunger)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    global status
    global state
    if state == 3:
        basic.show_leds("""
            # . . . #
            . # . # .
            . . # . .
            . # . # .
            # . . . #
            """)
    elif state == 0:
        basic.show_leds("""
            # . . . #
            . # . # .
            . . # . .
            . # . # .
            # . . . #
            """)
    else:
        basic.show_leds("""
            . # . # .
            # # # # #
            # # # # #
            . # # # .
            . . # . .
            """)
        select()
        status = status - 1
input.on_button_pressed(Button.B, on_button_pressed_b)

def on_gesture_shake():
    happiness = status / 100
    basic.show_number(100 - happiness)
    basic.show_string("%")
input.on_gesture(Gesture.SHAKE, on_gesture_shake)

def eventcheck():
    global state
    global status
    global hunger
    if state == 0:
        if 1 == randint(0, 100):
            state = state + 1
    elif hunger < 0:
        state = state + 2
    elif state == 2:
        hunger = hunger - .01
    elif 1 == randint(0, status):
        state = state + 1
        status = 10000

state = 0
status = 10000
hunger = 50

def main():
    global state
    global hunger 
    hunger = hunger - .01
    if state == 0:
        egg()
    elif state == 1:
        stage1()
    elif state == 2:
        stage2()
    else:
        state = 3
        death()
basic.forever(main)

#def on_button_pressed_ab():
#    global status
#    status = 10
#input.on_button_pressed(Button.AB, on_button_pressed_ab)
