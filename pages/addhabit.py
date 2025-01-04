from streamlit import *
from streamlit import segmented_control
import pandas as pd

def display_habits(key,habits):
  """Displays habits in a column with checkboxes for marking them done."""
  for val in habits:
    if checkbox(val[0]):
      # Move habit to habits_done dictionary when checked
      session_state.habits_done[key].append(val)
      habits.remove(val)
      
def create_habit_dataframe(habits_done):
  """Creates a DataFrame from the habits_done dictionary."""
  data = []
  for key, habits in habits_done.items():
    for habit, time in habits:
      data.append({"Time of Day": key, "Habit": habit, "Hours": time})
  return pd.DataFrame(data)
 
page_link("pages/Habits.py", label="", icon="🔙")

title(':green[Add a new Habit]')

# Initialize session state for habits and habits_done dictionaries
if 'habits' not in session_state:
   session_state.habits = {"Morning": [], "Afternoon": [], "Evening": []}
if 'habits_done' not in session_state:
  session_state.habits_done = {"Morning": [], "Afternoon": [], "Evening": []}
if 'df' not in session_state:
    session_state.df={}

# Entering new habits and displaying them
options = ["Morning", "Afternoon", "Evening"]
selection = segmented_control("Select a category", options, selection_mode="single")
new_habit = text_input('Enter your new habit')
time=number_input("How many hours will you perform this activity for?")
toast('Hello there! Dont forget to select a category! Or it might just show an error!')


if button('Add Habit'):
  session_state.habits[selection].append([new_habit,time])

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
  
  if session_state.habits_done:
    session_state.df = create_habit_dataframe(session_state.habits_done)
    