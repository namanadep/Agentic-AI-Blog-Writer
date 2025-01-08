import streamlit as st
from crew import crew

st.title("Blog Content Generator")

# User input for the topic
topic = st.text_input("Enter the topic for the blog:")

if st.button("Generate Blog"):
    if topic:
        st.write("Generating blog content for the topic:", topic)
        result = crew.kickoff(inputs={'topic': topic})
        st.write("Blog Content:")
        st.write(result)
    else:
        st.write("Please enter a topic.")