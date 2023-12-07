import streamlit as st
from PIL import Image


def app():
    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown('#')
    with col2:
        st.image('melanie pic.jpg')
    with col3:
        st.markdown('#')
    # find more emojis here: https://www.webfx.com/tools/emoji-cheat-sheet/
    img = 'melanie pic.jpg'
    # ----HEADER SECTION----
    st.subheader("Hi I am Melanie D. Amora :wave:")
    st.title("Computer Engineering student of Surigao del Norte State University (SNSU)_BSCpE-1B")
    st.write(" I am learning how to code and program. Let's go and explore the world of programming.")

    st.markdown("---")
    st.markdown("<h1 style='text-align: center;'> Unravelling the Code: A Journey into the World of Programming </h1>", unsafe_allow_html=True)
    
    
    st.markdown('---')
    # ----Learn more----
    st.subheader("Interesting part to learn, explore, and develop your own website. Here on computer programming. ")
    st.write("[Learn More >](https://pythonandvba.com)")
    
