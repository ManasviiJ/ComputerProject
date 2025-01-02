from streamlit import *

page_link("Welcome_Page.py",label="",icon="🔙")
title(":violet[Dashboard]")
write()

if 'habits' not in session_state or 'tasks' not in session_state:
  toast('Hello there! Try adding some habits and tasks in the habits and tasks page to see your dashboard')

col1,col2=columns(2)
with col1:
  subheader("Your existing habits:")
  for habit_time in session_state.habits.values():
    write(habit_time)
with col2:
  subheader("Incomplete tasks in to do list")
  for task_not_done in session_state.tasks:
    if task_not_done['status']==False:
      write(task_not_done['task'])



