from streamlit import *

st.set_page_config(
    page_title="Trakyoduck",
    page_icon="🦆",
    layout="wide",  # Or "centered"
    initial_sidebar_state="collapsed"  # Options: "expanded", "collapsed", "auto"
)

title(":rainbow[Trackyoduck]")
subheader(":blue[Build Better Habits, Build a Better Life]")

page_link("pages/Dashboard.py",label="Dashboard", icon="🐉")
page_link("pages/Habits.py", label="Habits", icon="🌳")
page_link("pages/Habits_Scorecard.py",label="Habits Scorecard", icon="💯")
page_link("pages/To_Do_List.py",label="To Do",icon="✔")

divider()
page_link("pages/About_us.py", label=":grey[About us]", icon="❤")

