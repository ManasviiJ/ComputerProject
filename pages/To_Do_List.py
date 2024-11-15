from streamlit import *
page_link("Welcome_Page.py",label="",icon="🔙")

title("To Do List")

if 'tasks' not in session_state:
  session_state.tasks=[]
  
task=text_input("Enter new task")
if task and button('add task'):
  session_state.tasks.append({'task':task,'status':False})

subheader('Your tasks:')
for task_status in session_state.tasks:
  task_status['status']=checkbox(label=task_status['task'],key=session_state.tasks.index(task_status),help=None)
   
col1,col2=columns(2)
with col2: 
  subheader(':green[Tasks Completed]')
  for task_done in session_state.tasks:
    if task_done['status']:
      write(task_done['task'])

with col1:
  subheader(':red[Tasks Inomplete]')
  for task_not_done in session_state.tasks:
    if task_not_done['status']==False:
      write(task_not_done['task'])

