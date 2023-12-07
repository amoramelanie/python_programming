import streamlit as st
from streamlit_option_menu import option_menu
import plotly.express as pix
import base64
import home, trending,  your_posts, about
st.set_page_config(
        page_title="Mel Blog",
)


@st.cache_data
def get_img_as_base64(file):
        with open(file, "rb") as f:
            data = f.read()
        return base64.b64encode(data).decode()


img = get_img_as_base64("b_0.jpg")
img1 = get_img_as_base64("b_2.jpg")


page_bg_img = f"""
<style>
[data-testid="stAppViewContainer"] > .main {{
background-image: url("data:image/png;base64,{img1}");
background-position: left; 
background-repeat: repeat;
background-size: 100%;
background-attachment: local;
}}
[data-testid="stSidebar"] > div:first-child {{
background-image: url("data:image/png;base64,{img}");
background-position: left; 
background-repeat: repeat;
background-size: 180%;
background-attachment: local;
}}

[data-testid="stHeader"] {{
background: rgba(0,0,0,0);
}}

[data-testid="stToolbar"] {{
    right: 2rem;
    }}
    </style>
    """

st.markdown(page_bg_img, unsafe_allow_html=True)


class MultiApp:

    def __init__(self):
        self.apps = []

    def add_app(self, title, func):

        self.apps.append({
            "title": title,
            "function": func
        })

    def run():
        # app = st.sidebar(
        with st.sidebar:        
            app = option_menu(
                menu_title='Mel Blog ',
                options=['Home','Trending','Your Posts','about'],
                icons=['house-fill','trophy-fill','chat-fill','info-circle-fill'],
                menu_icon='chat-text-fill',
                default_index=0 ,
                styles={
                    "container": {"padding": "5!important","background-color":'orange'},
        "icon": {"color": "white", "font-size": "23px"}, 
        "nav-link": {"color":"w","font-size": "20px", "text-align": "left", "margin":"0px", "--hover-color": "blue"},
        "nav-link-selected": {"background-color": "#0000FF"},}
                
                )
            
            
            

        
        if app == "Home":
            home.app()
    
        if app == "Trending":
            trending.app()        
        if app == 'Your Posts':
            your_posts.app()
        if app == 'about':
            about.app()    
             

             
          
             
    run()     

