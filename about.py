import streamlit as st

def app():
    st.markdown('---')
  
    col2, col3 = st.columns(2)
    
       
    with col2:
        st.image('Software Engineering.jpg')
    with col3:
        st.markdown('#')
    with col3:
        st.image('img.1.jpg')
    st.subheader('Welcome to our Coding Haven!')
    st.write('In this blog, we will embark on a journey through the intricate and fascinating realm of programming.')
    st.write('Come and let us explore the latest trends, share helpful tips, and demystify the wonders of coding.')

    #----HEADER SECTION----
    with st.container():
         st.subheader("1.The Art of Debugging: Navigating the Maze")
         st.write('Drive into the art of debugging as we unravel common coding challenges. Learn effective strategies to troubleshoot and conquer bugs that may lurk in your code.')
         st.subheader("2.Mastering the Basics: A Guide for Beginners ")
         st.write("Discover fundametal concepts and step-by-step tutorials to kickstart your coding journey. From variables to loops, let us break down the basics with clarity.")
         st.subheader("3.Beyond Hello World: Building your first project")
         st.write("Ready to move beyond the standard Hello World! program? No worries will guide you through the process of building your first real-world project, offering practical insights and hands-on examples.")
         st.subheader("4.The Power of Verson Control Git and GitHub")
         st.write("Unlock the potential of version control with Git and GitHub. Learn how to track changes, collaborate seamlessly with others, and ensure the integrity of your codebase.")
         st.subheader("5.Web Development Wonders: From HTML to JavaScript")
         st.write("Take a deep dive into web development essentials. Explore the building blocks of the web- HTML, CSS, and JavaScript-and discover how they come together to create interactive and visually appealing websites.")
         st.subheader("6.Exploring Python:A Versatile Programming Language ")  
         st.write("Python's versatility makes it a favorite among developers. Delve into the language's features, explore its diverse applications, and uncover why python is a go-to choice for many coding enthusiasts.")
         st.image('pic.1.jpg') 
         st.markdown('#')   
         st.subheader('Thank you!')
    st.markdown('Created by: [Melanie Amora](https://github.com/Ashwani132003)')
    st.markdown('Contact via mail: [35melanieamora@gmail.com]')
    