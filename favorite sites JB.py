import pyautogui as pg
import webbrowser

videos = ["https://www.youtube.com/watch?v=1T4cFcNi_nQ","https://www.youtube.com/watch?v=cnaeIAEp2pU"]

music = 


answer = pg.prompt(
"""
Which would you rather do?
a) Watch videos
b) Listen to music

"""
    )
if answer == "a":
    for i in videos:
        webbbrowser.open(i)

elif answer == "b":
    for i in music:
        webbrowser.open(i)
