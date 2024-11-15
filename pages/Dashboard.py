from streamlit import *

page_link("Welcome_Page.py",label="",icon="🔙")

col1, col2, col3=columns(3)
with col2:
  title(":violet[Dashboard]")
with col1:
  subheader(":grey[Your existing habits:]")
  for habit,days in session_state.habits.items():
    write(habit,"for",days,"days")

divider()
with col3:
  subheader("Your To-DO List for the day")
