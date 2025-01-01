from streamlit import *

def display_habits(habits):
  """Displays habits in a column with checkboxes for marking them done."""
  for val in habits:
    if checkbox(val):
      # Move habit to habits_done dictionary when checked
      session_state.habits_done[val] = True
      habits.remove(val)
      rerun()  # Refresh the app to update the habit lists

if __name__ == "__main__":
  page_link("pages/Habits.py", label="", icon="🔙")

  title(':green[Add a new Habit]')

  # Initialize session state for habits and habits_done dictionaries
  if 'habits' not in session_state:
    session_state.habits = {"Morning": [], "Afternoon": [], "Evening": []}
  if 'habits_done' not in session_state:
    session_state.habits_done = {}

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
    display_habits(session_state.habits["Morning"])
  with col2:
    subheader("Afternoon")
    display_habits(session_state.habits["Afternoon"])
  with col3:
    subheader('Evening')
    display_habits(session_state.habits["Evening"])

  # Display completed habits (if any)
  if session_state.habits_done:
    write("Completed Habits:")
    for habit, done in session_state.habits_done.items():
      if done:
        write(f"- {habit}")