from streamlit import *

set_page_config(
    page_title="Trakyoduck",
    page_icon="🦆",
    layout="centered",  # Or "centered" "wide"
    initial_sidebar_state="collapsed"  # Options: "expanded", "collapsed", "auto"
)

column1,column2,column3=columns(3)

with column2:
    title(":rainbow[Trackyoduck]")
subheader(":blue[Build Better Habits, Build a Better Life]")

col1,col2=columns(2)
with col1:
    page_link("pages/Dashboard.py",label="Dashboard", icon="🐉")
    page_link("pages/Habits.py", label="Habits", icon="🌳")
with col2:
    page_link("pages/Habits_Scorecard.py",label="Habits Scorecard", icon="💯")
    page_link("pages/To_Do_List.py",label="To Do",icon="✔")

divider()

with column2:
    page_link("pages/About_us.py", label=":grey[About us]", icon="❤")

