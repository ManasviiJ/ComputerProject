from streamlit import *
import pandas as pd

def display_habits(key, habits):
    """Displays habits in a column with checkboxes for marking them done and recording duration."""
    for val in habits:
        if checkbox(val):
            time = number_input(f"How long did you do '{val}' for? (in hours)", min_value=0.0, step=0.5)  # Add min_value and step for better user experience
            session_state.habits_done[key].append([val, time])
            habits.remove(val)
            rerun()  # Refresh the app to update habit lists

def create_habit_dataframe(habits_done):
    """Creates a DataFrame from the habits_done dictionary."""
    data = []
    for key, habit_list in habits_done.items():
        for habit, time in habit_list:
            data.append({"Time of Day": key, "Habit": habit, "Hours": time})
    return pd.DataFrame(data)

if __name__ == "__main__":
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
        display_habits("Morning", session_state.habits["Morning"])
    with col2:
        subheader("Afternoon")
        display_habits("Afternoon", session_state.habits["Afternoon"])
    with col3:
        subheader('Evening')
        display_habits("Evening", session_state.habits["Evening"])

    # Create and display the DataFrame if habits_done has data
    if session_state.habits_done:
        habit_df = create_habit_dataframe(session_state.habits_done)
        st.write("Habit Summary:")
        st.dataframe(habit_df)