import streamlit as st
import os
# Check for query parameters
#query_params = st.experimental_get_query_params()
#page = query_params.get("page", [""])[0]  # Default to an empty string if no "page" parameter
def run():
    st.title("Vacuum Chamber Project")
    st.write("This page shows details about the Vacuum Chamber project.")

    # First Container
    with st.container():
        st.write("----")
        st.header("My Vacuum Chamber Project")
        st.write("##")
        st.write("I am making a Vacuum Chamber to mimic the environment at 30kft.")

    with st.container():
        st.header("My Vacuum Chamber")
        
        # Test if the file exists
        st.write("Does the file exist?", os.path.exists("PICS/Vacuum2.jpg"))
        
        # Display the image
        st.image("pages/vac/vac_pic/Vacuum2.jpg", caption="This is a picture of the lid of the vacuum chamber.", use_column_width=True)
