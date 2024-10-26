from streamlit import *

title(":rainbow[Welcome!]")
subheader(":rainbow[Build Better Habits, Build a Better Life]")
write("What would you like to do today?")

page_link("pages/Habits.py", label="Habits", icon="🌳")

divider()
page_link("pages/About_us.py", label=":grey[About us]", icon="❤")

