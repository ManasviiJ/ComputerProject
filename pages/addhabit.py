from streamlit import *
from streamlit import segmented_control

page_link("pages/Habits.py",label="",icon="🔙")

title(':green[Add a new Habit]')

#Initializing session state to store habits as a dictionary
if 'habits' not in session_state:
    session_state.habits={}
   
#Entering new habits and displaying them
new_habit=text_input('Enter you new habit', label_visibility='collapsed')
days_to_follow=select_slider('How  many ***days*** do you wish to follow your new habit?', options=range(31))

write('Select a category')
options = ["Morning", "Afternoon", "Evening"]
selection =segmented_control("Directions", options, selection_mode="multi")
markdown(f"Your selected options: {selection}.")

if button('Add habit'):
    session_state.habits[new_habit]=days_to_follow
  
subheader('Your new habits:')
for habit, days in session_state.habits.items():
    checkbox(f"{habit} for {days} days")
