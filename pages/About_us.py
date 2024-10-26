from streamlit import *

page_link("Welcome_Page.py",label="",icon="🔙")

title(":red[About us]")
markdown('''Welcome to your personal pocket cheerleader! 🌟 Whether you're forming new habits or chasing your dreams, we're here to help you stay on track. With every step forward, big or small, you're building a better you—one day at a time. Let's grow together and make everyday wins feel extra special! 💪✨''')
caption('Your feedback is really important to us!')
if feedback('stars'):
    write("Thank you for choosing us!")

