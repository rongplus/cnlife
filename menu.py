import streamlit as st 
   
def menu():  
    st.sidebar.page_link("streamlit_app.py", label="首页")  
    st.sidebar.page_link("pages/fi.py", label="降雨")  
    st.sidebar.page_link("pages/life.py", label="天气")  

