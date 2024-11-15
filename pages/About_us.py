from streamlit import *

page_link("Welcome_Page.py",label="",icon="🔙")

title(":red[Why choose us?]")
write_stream("TrackYourDuck is more than just a name; it's a playful reminder to keep paddling, no matter how challenging it may seem.")
markdown('''*Description:*

Trackyoduck is a simple, yet powerful habit tracker app inspired by the principles of "Atomic Habits". Our app helps you create lasting changes by  by focusing on small incremental improvements
That's correct!

Daniel Kahneman, Nir Eyal, and Aubrey Marcus are indeed notable figures who have drawn inspiration from "Atomic Habits" by James Clear.

*Daniel Kahneman*: Nobel Prize-winning economist and author of "Thinking, Fast and Slow". Kahneman's work on behavioral economics and cognitive biases laid the groundwork for Clear's habits-based approach.

*Nir Eyal*: Author of "Hooked: How to Build Habit-Forming Products" and behavioral designer. Eyal's work focuses on designing engaging products that create lasting habits.

*Aubrey Marcus*: Founder of Onnit, author, and podcaster. Marcus has integrated Atomic Habits principles into Onnit's wellness and self-improvement programs.
 Habits"  and motivational 

These thought leaders recognize the value of "Atomic Habits" in providing actionable strategies for personal growth, self-improvement, and behavioral change.''')
caption('Your feedback is really important to us!')
if feedback('stars'):
    write("Thank you for choosing us!")

