import pyautogui as pg
import time
import webbrowser
points=0

# Question 1

answer=pg.prompt(
"""
Which would you rather do?

a) Eat donuts all day every day
b) Have a cactus as a head
c) Be a nerd
"""
    )

# Give points

if answer == "a":
    points += 1
elif answer == "b":
    points += 2
elif answer == "c":
    points += 3

# Question 2

answer=pg.prompt(
"""
Who is your arch nemesis? 

a) Bart
b) Charles Montgomery Burns
c) Slideshow Bob
"""
    )

# Give points

if answer == "a":
    points += 1
elif answer == "b":
    points += 2
elif answer == "c":
    points += 3

# Question 3

answer=pg.prompt(
"""
Where would you like to live?

a) Springfield, Oregon
b) Quahog, Ohio
c) Thunder Bay, Canada
"""
    )

# Give points

if answer == "a":
    points += 1
elif answer == "b":
    points += 2
elif answer == "c":
    points += 3


# END OF SURVEY

answer=pg.alert("You are")

# Homer
if points <8:
    pg.alert("Homer Simpson")
    webbrowser.open("https://www.youtube.com/watch?v=1T4cFcNi_nQ")
    webbrowser.open("https://www.youtube.com/watch?v=cnaeIAEp2pU")

# Marg
elif points >= 8 and points < 12:
    pg.alert ("Marg Simpson")

# Lisa
elif points >=12:
    pg.alert ("Lisa Simpson")
