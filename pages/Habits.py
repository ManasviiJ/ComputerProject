from streamlit import *
from streamlit import segmented_control

page_link("Welcome_Page.py",label="",icon="🔙")

title(':green[Habits]')
subheader(':blue[What would you like to do today?]')

coli,coii2=columns(2)
with coli:
    page_link("pages/progress.py",label="See your progress",icon="🚨")
with colii:
    page_link("pages/addhabit.py",label="add a new habit",icon="🔥")

subheader("Your current habits are:")

col1,col2,col3=columns(3)
with col1:
    subheader('Morning')
    for k,v in session_state.habits.items():
        if k=="Morning":
            write(v[0])
with col2:
    subheader("Afternoon")
    for k,v in session_state.habits.items():
        if k=="Afternoon":
            write(v[0])
with col3:
    subheader('Evening')
    for k,v in session_state.habits.items():
        if k=="Evening":
            write(v[0])