from streamlit import *
from streamlit import segmented_control

page_link("pages/Habits.py",label="",icon="🔙")

title(':green[Add a new Habit]')

#Initializing session state to store habits as a dictionary
if 'habits' not in session_state:
    session_state.habits={}
if 'habits_done' not in session_state:
    session_state.habits_done={'Morning':[],'Afternoon':[],'Evening':[]}
   
#Entering new habits and displaying them
options = ["Morning", "Afternoon", "Evening"]
selection =segmented_control("Select a category", options, selection_mode="single")
new_habit=text_input('Enter you new habit')

if button('Add Habit'):
    session_state.habits[selection].append(new_habit)

'''def get_number_input():
  """Displays a popup and gets a number input from the user."""
  with sidebar:
    title("Enter a Number")
    number = number_input("Enter a number:")
  return number'''

col1,col2,col3=columns(3)
with col1:
    subheader('Morning')
    for k,v in session_state.habits.items():
        if k=="Morning":
            if checkbox(v):
                '''number = get_number_input()
                write("You entered:", number)'''
                session_state.habits.pop(k)
                rerun()
with col2:
    subheader("Afternoon")
    for k,v in session_state.habits.items():
        if k=="Afternoon":
            if checkbox(v):
                session_state.habits.pop(k)
                rerun()
with col3:
    subheader('Evening')
    for k,v in session_state.habits.items():
        if k=="Evening":
            if checkbox(v):
                session_state.habits.pop(k)
                rerun()
write(session_state.habits_done)

