import streamlit as st
import os
import sys

# Append paths to dynamically load pages
# This allows you to load modules or files from the "pages/vac" directory dynamically.
sys.path.append(os.path.join(os.path.dirname(__file__), "pages/Vac"))
sys.path.append(os.path.join(os.path.dirname(__file__), "pages/Ebike"))
sys.path.append(os.path.join(os.path.dirname(__file__), "pages/IRLED"))
sys.path.append(os.path.join(os.path.dirname(__file__), "pages/Clockdistribution"))
sys.path.append(os.path.join(os.path.dirname(__file__), "pages/Easyeats"))
sys.path.append(os.path.join(os.path.dirname(__file__), "pages/Resumeproject"))




# Configure the Streamlit app
# Set the title, icon, and layout of the Streamlit app.
st.set_page_config(page_title="Jason Wong", page_icon=":tada:", layout="wide")

# Callback function to handle navigation
# This function updates the session state to store the current page. 
# It accepts a parameter `page_name`, which sets the page to navigate to.
def navigate_to(page_name):
    st.session_state["page"] = page_name

# Initialize the query parameter `page` in session_state if not already set
# If "page" is not already in `st.session_state`, it is initialized to an empty string.
# This ensures a default value for the page variable.
if "page" not in st.session_state:
    st.session_state["page"] = ""

# Get the current page from session_state
# This retrieves the current page name from `st.session_state`.
page = st.session_state["page"]

# Render content dynamically based on the current page
if page == "vacuum-chamber":
    # Display the Vacuum Chamber page
    import Vacuum_chamber  # Import the Vacuumchamber module
    Vacuum_chamber.run()
    # Add a button to navigate back to the home page
    # Clicking this button calls `navigate_to("")`, which sets the page to the home page.
    st.button("Back to Home", on_click=navigate_to, args=("",))
elif page =="E-bike":
    import E_bike
    E_bike.run()
    st.button("Back to Home", on_click=navigate_to, args=("",))
elif page =="IR-LED":
    import IR_LED
    IR_LED.run()
    st.button("Back to Home", on_click=navigate_to, args=("",))
elif page == "Clock-distribution":
    import clock_distribution
    clock_distribution.run()
    st.button("Back to Home", on_click=navigate_to, args=("",))
elif page == "easy-eats":
    import easy_eats
    easy_eats.run()
    st.button("Back to Home", on_click=navigate_to, args=("",))
elif page == "resume-project":
    import Resume_project
    Resume_project.run()
    st.button("Back to Home", on_click=navigate_to, args=("",))



else:
    # Default home page
    # Content displayed when no specific page is selected (i.e., page is "").
    st.subheader("Hello, I am Jason!")  # Adds a subheader to introduce the webpage
    st.title("Welcome to My Webpage!")  # Main title of the home page
    st.write("This webpage showcases all the projects I have been working on for the last few years.")  # Brief description of the webpage
    st.write("Each project title is a hyperlink that will direct you to a different page with specific details about the project.")  # Instruction for users
    
    # Navigation link to the Vacuum Chamber page
    # Clicking this button calls `navigate_to("vacuum_chamber")`, which sets the page to "vacuum_chamber".
    st.button("Go to Vacuum Chamber", on_click=navigate_to, args=("vacuum-chamber",))
    st.button("Go to E-bike", on_click=navigate_to, args=("E-bike",))
    st.button("Go to IR LED",on_click=navigate_to, args=("IR-LED",))
    st.button("Go to Clock Distribution ",on_click=navigate_to, args=("Clock-distribution",))
    st.button("Go to Easy Eats ",on_click=navigate_to, args=("easy-eats",))
    st.button("Go to Resume Project ",on_click=navigate_to, args=("resume-project",))
    contact_form = """
    <form action="https://formsubmit.co/jasonwong38927@gmail.com" method="POST">
        <input type="hidden" name="_captcha" value="false">
        <input type="text" name="name" placeholder="Your Name" required>
        <input type="email" name="email" placeholder="Your email" required>
        <textarea name="message" placeholder="Your message here" required></textarea>
        <button type="submit">Send</button>
    </form>
    """
    st.write("---")
    st.header("Get in touch with me!")
    st.write("##")
    left_column, right_column = st.columns(2)
    with left_column:
        st.markdown(contact_form, unsafe_allow_html=True)
    with right_column:
        st.empty()

