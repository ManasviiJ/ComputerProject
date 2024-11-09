from streamlit import *

page_link("Welcome_Page.py",label="",icon="🔙")

title(':green[Habits]')
    
#Initializing session state to store habits as a dictionary
if 'habits' not in session_state:
    session_state.habits={}
   
#Entering new habits and displaying them
new_habit=text_input('Enter you new habit', label_visibility='collapsed')
days_to_follow=select_slider('How  many ***days*** do you wish to follow your new habit?', options=range(31))
  
if  button('Add habit'):
    session_state.habits[new_habit]=days_to_follow
  
subheader('Your new habits:')
for habit, days in session_state.habits.items():
    write(f"{habit} for {days} days")

balloons()
