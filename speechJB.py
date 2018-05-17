import win32com.client as wincl
import pyautogui as pg
import webbrowser as wb

speak = wincl.Dispatch("SAPI.SpVoice")
speak.Speak("what is your name")
answer = pg.prompt("put your name")

speak.Speak("what up " + answer + "" + "Nice to meet you.")

speak.Speak("What is your animal")
animal = pg.prompt("put your favorite animal.")

if animal == "turtle":
    speak.Speak

speak.Speak("what video you want?")
video = pg.prompt("enter video here")
wb.open("https://www.youtube.com/results?search_query=" + video)
    
