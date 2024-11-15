from streamlit import *
from streamlit_calendar import calendar

page_link("Welcome_Page.py",label="",icon="🔙")
title(":violet[Dashboard]")
write()

col1,col2=columns(2)
with col1:
  subheader(":grey[Your existing habits:]")
  for habit,days in session_states.habits.items():
    write(habit,"for",days,"days")
with col2:
  subheader("Incomplete tasks in to do list")
  for task_not_done in session_states.tasks:
    if task_not_done['status']==False:
      write(task_not_done['task'])

calendar()

