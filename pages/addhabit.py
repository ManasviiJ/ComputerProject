from streamlit import *
from streamlit import segmented_control

def display_habits(key,habits):
  """Displays habits in a column with checkboxes for marking them done."""
  for val in habits:
    if checkbox(val):
      # Move habit to habits_done dictionary when checked
      time=number_input("How long did you do this activity for? (in hours)")
      session_state.habits_done[key].append([val,time])
      habits.remove(val)
 
page_link("pages/Habits.py", label="", icon="🔙")

title(':green[Add a new Habit]')

# Initialize session state for habits and habits_done dictionaries
if 'habits' not in session_state:
   session_state.habits = {"Morning": [], "Afternoon": [], "Evening": []}
if 'habits_done' not in session_state:
  session_state.habits_done = {"Morning": [], "Afternoon": [], "Evening": []}

# Entering new habits and displaying them
options = ["Morning", "Afternoon", "Evening"]
selection = segmented_control("Select a category", options, selection_mode="single")
new_habit = text_input('Enter your new habit')

if button('Add Habit'):
  session_state.habits[selection].append(new_habit)

# Display habit categories and habits with checkboxes
col1, col2, col3 = columns(3)
with col1:
  subheader('Morning')
  display_habits("Morning",session_state.habits["Morning"])
with col2:
  subheader("Afternoon")
  display_habits("Afternoon",session_state.habits["Afternoon"])
with col3:
  subheader('Evening')
  display_habits("Evening",session_state.habits["Evening"])