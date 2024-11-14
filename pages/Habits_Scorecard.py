from streamlit import *
import time

page_link("Welcome_Page.py",label="",icon="🔙")

title("Habits Scorecard")
entry=text_input("Make a list of your daily habits")


divider()
if button("How does this work?"):
  toast("Habit scorecard is a simple excercise you can use to become more aware of your behaviour")
  time.sleep(3)
  toast("You can create a list of your daily habits to keep track of them and review them as you cut down bad habits and replace them with good ones")

