import streamlit as st
import PIL as image

def app():

    col2, col3 = st.columns(2)
    

    with col2:
        st.image('Do It!.jpg')

    with col3:
        st.image('m1.jpg')
    st.markdown('-----')
    
             
    st.subheader('Riding the Wave: Trending Thoughts That Will Shape Tomorrow')
    st.markdown('----')
    st.write("Welcome to ThoughtTrends, your hub for riding the waves of the latest and greatest thoughts buzzing around the digital cosmos. In today's post, we're diving headfirst into the pool of trending thoughts, exploring the ideas that are shaping conversations, sparking debates, and ultimately, influencing the way we see the world. Buckle up and join us on this exhilarating journey through the mindscapes of the present and the promises they hold for the future.")
    st.markdown('---')
    cols1, cols2 = st.columns([2,2])
    with cols1:
        st.video("t2.mp4")
    with cols2:
        st.subheader("The Power of TikTok Trends")
        st.write("In a world of short attention spans and viral content, TikTok trends have become the heartbeat of internet culture. From dance challenges to innovative life hacks, we'll explore the power of these bite-sized trends and their impact on shaping popular opinions.")
        st.write("The power of TikTok trends lies in its ability to rapidly spread and influence a large and diverse audience. TikTok is a social media platform that allows users to create and share short-form videos, typically set to music or audio clips. Trends on TikTok can encompass a wide range of content, including dance challenges, lip-syncing, comedy sketches, educational content, and more.")
        st.write("TikTok trends have the potential to go viral very quickly. When a user creates a video that aligns with a popular trend, it can be discovered by a vast audience, leading to widespread sharing and engagement.")
        st.write("TikTok has a massive and diverse user base around the world. Trends can transcend geographical boundaries and resonate with people from different cultures and backgrounds.")
    st.markdown('---')
    st.subheader('Wellness in the Digital Age')
    st.video("vid_1.mp4")
    st.write("In the age of constant connectivity, mental health and wellness have become hot topics. From mindfulness apps to the rise of digital detox, we'll dissect the trending thoughts surrounding self-care and the quest for a balanced, healthy life in the digital age.")
    st.markdown('---')
    st.write("As we ride the wave of trending thoughts, it's clear that our collective consciousness is dynamic and ever-evolving. ThoughtTrends is here to keep you in the loop, providing insights into the pulse of contemporary thinking. Stay tuned for more updates on the trends that will continue to shape the way we perceive and interact with the world.")
    st.image("b_1.jpg")
    st.write("😊Thank you!")

  



  
    