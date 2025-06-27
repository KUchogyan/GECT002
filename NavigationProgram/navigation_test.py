import playsound3 as p3

status = 'Turn-Left'

if status == 'school_zone':
    p3.playsound('In a moment.mp3')
    p3.playsound('Child protection.mp3')
    p3.playsound("It is.mp3")
    p3.playsound("On speeding.mp3")
    p3.playsound("Please be careful.mp3")
elif status == "Bus-only lane":
    p3.playsound("Bus-only lane.mp3")
    p3.playsound("It is.mp3")
    p3.playsound("Please be careful.mp3")
elif status == "Turn-Left":
    p3.playsound("In a moment.mp3")
    p3.playsound("Turn left.mp3")
    p3.playsound("It is.mp3")
elif status == "Turn-Right":
    p3.playsound("In a moment.mp3")
    p3.playsound("Turn right.mp3")
    p3.playsound("It is.mp3")