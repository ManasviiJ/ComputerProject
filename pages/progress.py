from streamlit import *

page_link("pages/Habits.py",label="",icon="🔙")
st.bar_chart(source, x=["Morning","Afternoon","Evening"], y="time", color="", stack=True)
