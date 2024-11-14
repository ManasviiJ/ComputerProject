import streamlit as st

# Initialize the session state for tasks if not already initialized
if 'tasks' not in st.session_state:
    st.session_state.tasks = []

# Title of the app
st.title("To-Do List App")

# Input field to add new tasks
task = st.text_input("New Task")

# If the user enters a task, add it to the list
if st.button("Add Task") and task:
    st.session_state.tasks.append({"task": task, "done": False})
    st.experimental_rerun()

# Display existing tasks
for idx, task_item in enumerate(st.session_state.tasks):
    # Create a checkbox for each task
    task_done = st.checkbox(
        f"{task_item['task']}",
        value=task_item['done'],
        key=f"checkbox_{idx}"
    )

    # Update the task status when checkbox is clicked
    if task_done != task_item['done']:
        st.session_state.tasks[idx]["done"] = task_done

# Display a list of tasks and their status
completed_tasks = [task['task'] for task in st.session_state.tasks if task['done']]
incomplete_tasks = [task['task'] for task in st.session_state.tasks if not task['done']]

st.write("### Completed Tasks")
st.write("\n".join(completed_tasks) if completed_tasks else "No completed tasks.")

st.write("### Incomplete Tasks")
st.write("\n".join(incomplete_tasks) if incomplete_tasks else "No incomplete tasks.")
