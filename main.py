import streamlit as st

st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:
    st.image("pictures/my_photo.png")

with col2:
    st.title("Juan Tomás Gómez")
    content = """
    Tech-driven venture strategist with experience in entrepreneurship, core consulting, and
    corporate venture building. Tech entrepreneur with a successful exit in the LATAM 
    e-commerce space. Currently a Senior Venture Architect for BCG X, focusing primarily on 
    enterprise AI and B2B SaaS ventures.
    """
    st.info(content)

info_content = """
Below, you will find an overview of the apps I have built in my python journey.
"""
st.write(info_content)