from streamlit import *
from streamlit import segmented_control

page_link("pages/Habits.py",label="",icon="🔙")

title(':green[Add a new Habit]')

#Initializing session state to store habits as a dictionary
if 'habits' not in session_state:
    session_state.habits={}
   
#Entering new habits and displaying them
new_habit=text_input('Enter you new habit', label_visibility='collapsed')

options = ["Morning", "Afternoon", "Evening"]
selection =segmented_control("Select a category", options, selection_mode="single")

if button('Add Habit'):
    session_state.habits[selection]=[new_habit]

col1,col2,col3=columns(3)
with col1:
    subheader('Morning')
    for k,v in session_state.habits.items():
        if k=="Morning":
            if checkbox(v[0]):
                session_state.habits[k]=None
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

