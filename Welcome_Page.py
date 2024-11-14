from streamlit import *

title(":rainbow[Welcome!]")
subheader(":red[Build Better Habits, Build a Better Life]")
write("What would you like to do today?")

page_link("pages/Dashboard.py",label="Dashboard", icon="🐉")
page_link("pages/Habits.py", label="Habits", icon="🌳")
page_link("pages/Habits_Scorecard.py",label="Habits Scorecard", icon="💯")
page_link("pages/To_Do_List.py",label="To Do",icon="✔")

divider()
page_link("pages/About_us.py", label=":grey[About us]", icon="❤")

