import requests
import streamlit as st
from streamlit_lottie import st_lottie

st.set_page_config(page_title="Sergio's Portfolio", page_icon="🤖", layout="wide")

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# ----- LOAD ASSET ----- #
lottie_coding = load_lottieurl("https://lottie.host/7b088768-a16f-4c43-9b69-63cb5ab2b9fe/cvyV1R4tUl.json")

# ----- HEADER SECTION ----- #
with st.container():
    st.subheader("Hello, I'm Sergio 🧔‍♂️")
    st.title("A Dominican Data Scientist")
    st.write("I'm a data scientist who turns raw data into clear, actionable insights using machine learning and sharp analysis.")
    st.write("##")
    st.link_button(label="Github", url="https://github.com/sergioacast/Portfolio")

# ----- WHAT I DO ----- #
with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("What I Do")
        st.write(
            """
            My work focuses on solving real-world problems by digging into complex datasets, building models, and delivering results that make a difference. 
            Whether it's predicting trends, optimizing processes, or uncovering hidden patterns, 
            I'm driven by a mix of technical know-how and practical curiosity. 
            Here's a breakdown of what I bring to the table:
            
            - Data Analysis & Exploration: I dive deep into datasets to spot trends, outliers, and opportunities, using tools like Python or SQL to get the job done.
            - Machine Learning: I design and deploy models—think regression, classification, or clustering—to predict outcomes and solve problems, tailoring solutions to the data at hand.
            - Data Visualization: I create clean, intuitive visuals with tools like PowerBI or Matplotlib, making complex findings easy to grasp for anyone.
            - Problem-Solving: From business challenges to research questions, I break down big issues into manageable parts and deliver answers that work.
            - End-to-End Projects: I handle the full pipeline—cleaning messy data, building models, testing results, and presenting insights—so you get a complete solution.   
            """)
    with right_column:
        st.write("#")
        st_lottie(lottie_coding, height=400, key="coding")
        
        
# ----- PROJECTS ----- #
with st.container():
    st.write("---")
    st.header("Projects")
    st.write("##")
    image_column, text_column = st.columns((1, 2))

    with text_column:
        st.subheader("Exploratory Data Analysis Tool")
        st.write("Upload your dataset and explore it with automated stats and visuals.")
        st.markdown("[View Code on GitHub](https://github.com/sergioacast/eda-tool)")
        st.markdown("[Try it Live](https://exploreit.streamlit.app/)")    
          
