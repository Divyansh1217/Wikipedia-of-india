import wikipedia as wiki
import streamlit as st
writ=st.text_input("What want to know about India")
sentences=3
sentences=st.text_input("Sentences you want to know")
result=wiki.summary("India "+ writ,sentences=sentences)
st.write(result)