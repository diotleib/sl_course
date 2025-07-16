import streamlit as st

st.title("Hallo Welt!")

with st.sidebar
    st.header("Über diese App")


st.header("_Streamlit_ is :blue[cool] :sunglasses:")
st.header("This is a header with a divider", divider="rainbow")   
agree = st.checkbox("I agree")

if agree:
    st.write("Great!")
