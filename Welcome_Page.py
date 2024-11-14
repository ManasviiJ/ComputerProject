from streamlit import *

title(":rainbow[Welcome!]")
subheader(":rainbow[Build Better Habits, Build a Better Life]")
write("What would you like to do today?")

page_link("pages/Habits.py", label="Habits", icon="🌳")
page_link("pages/To_Do_List.py",label="To Do List", icon="✔")
page_link("pages/Dashboard.py",label="Dashboard", icon="🙇‍♂")

divider()
page_link("pages/About_us.py", label=":grey[About us]", icon="❤")

