from microbit import *
from random import randint

state = 0
status = 10000
hunger = 50

def egg():
    egg0 = Image("00000:09990:90009:90009:09990")
    egg1 = Image("09990:90009:90009:09990:00000")
    egg_animation = [egg0, egg1]
    display.show(egg_animation)
    eventcheck()


def stage1():

    evol0 = Image("00000:09900:99990:90090:00000")
    evol1 = Image("00000:00990:09999:09009:00000")
    evol_animation = [evol0, evol1]
    display.show(evol_animation)
    eventcheck()

def stage2():

    evol0 = Image("99990:99990:90090:99990:90090")
    evol1 = Image("09999:09999:09009:09999:09009")
    evol_animation = [evol0, evol1]
    display.show(evol_animation)
    eventcheck()

def death():
    death = Image("09990:99099:90009:09990:09990")
    death_animation = [death]
    display.show(death_animation)
    eventcheck()

def select():

    sel0 = Image("99999:90009:90009:90009:99999")
    sel1 = Image("00000:09990:09090:09990:00000")
    sel2 = Image("00000:00000:00900:00000:00000")
    sel_animation = [sel0, sel1, sel2]
    display.show(sel_animation)

def cross():
    img0 = Image("90009:09090:00900:09090:90009")
    cross_img = [img0]
    display.show(cross_img)

def evolve():
    evo0 = Image("09990:99999:99999:99999:09990")
    evo1 = Image("00000:00000:00000:00000:00000")
    evo_animation = [evo0, evo1]

    i = 0
    while i is not 2:
        i += 1
        display.show(evo_animation)

def on_button_pressed_a():
    global status
    global hunger
    global state
    if state == 3:
        cross()
    elif state == 0:
        cross()
    else:
        fish1 = Image("09000:99000:00999:00999:00999")
        fish_animation = [fish1]
        display.show(fish_animation)

        if hunger < 100:
            select()
            hunger = hunger + 10
            #test
            status = status - 1000
        else:
            cross()
    #display.show(round(hunger,2))

def on_button_pressed_b():
    global status
    global state
    if state == 3:
        cross()
    elif state == 0:
        cross()
    else:
        heart = Image("09090:99999:99999:09990:00900")
        heart_animation = [heart]
        display.show(heart_animation)
        select()
        status = status - 1

def on_button_pressed_ab():
    happy_animation = [Image.HAPPY]
    display.show(happy_animation)
    h1 = status / 100
    h2 = 100 - h1
    display.scroll(round(h2, 2))
    display.scroll("%")

def hidden():
    while True:
        hidden0 = Image("09990:90909:99999:99999:90909")
        hidden_animation = [hidden0]
        checkinput()

        i = -6

        if accelerometer.current_gesture() == 'face up':
            display.show(hidden_animation)

        if accelerometer.current_gesture() == 'right':
            while i < 6:
                hidden_animation = [hidden0.shift_right(i)]
                display.show(hidden_animation)
                checkinput()
                i += 1

        if accelerometer.current_gesture() == 'left':
            while i < 6:
                hidden_animation = [hidden0.shift_left(i)]
                display.show(hidden_animation)
                checkinput()
                i += 1

        if accelerometer.current_gesture() == 'down':
            while i < 6:
                hidden_animation = [hidden0.shift_up(i)]
                display.show(hidden_animation)
                checkinput()
                i += 1

        if accelerometer.current_gesture() == 'up':
            while i < 6:
                hidden_animation = [hidden0.shift_down(i)]
                display.show(hidden_animation)
                checkinput()
                i += 1

def eventcheck():
    global state
    global status
    global hunger

    if state == 0:
        if 1 == randint(0, 10):
            evolve()
            state = state + 1
    elif hunger < 0:
        state = state + 2
    elif state == 2:
        hunger = hunger - .01
    elif 1 == randint(0, status):
        evolve()
        state = state + 1
        status = 10000

def checkinput():
    gesture = accelerometer.current_gesture()

    if button_a.is_pressed() and button_b.is_pressed():
        on_button_pressed_ab()
    elif button_a.is_pressed():
        on_button_pressed_a()
    elif button_b.is_pressed():
        on_button_pressed_b()

    while gesture == "face down":
        gesture = accelerometer.current_gesture()
        display.clear()

def main():
    global state
    global hunger

    hunger = hunger - .01

    #test
    day = 1000*60

    if running_time() > day * 3:
        hidden()
    elif state == 0:
        egg()
    elif state == 1:
        stage1()
    elif state == 2:
        stage2()
    else:
        state = 3
        death()

    checkinput()

while True:
    main()
