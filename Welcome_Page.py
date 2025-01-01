from streamlit import *

set_page_config(
    page_title="TrackyoDuck",
    page_icon="🦆",
    layout="wide",  # Or "centered" "wide"
    initial_sidebar_state="collapsed"  # Options: "expanded", "collapsed", "auto"
)
title(":rainbow[TrackyoDuck]")
subheader(":blue[Build Better Habits, Build a Better Life]")

col1,col2=columns(2)
with col1:
    page_link("pages/Dashboard.py",label="Dashboard", icon="🐉")
    page_link("pages/Habits.py", label="Habits", icon="🌳")
with col2:
    page_link("pages/Motivation.py", label="Motivation", icon="🗻")
    page_link("pages/To_Do_List.py",label="To Do",icon="✔")

divider()
page_link("pages/About_us.py", label=":grey[About us]", icon="❤")


