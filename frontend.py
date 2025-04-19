import streamlit as st
import backend as bk

st.title("Gen Ai Project")
input = st.text_input("INPUT")
go = st.button("GO")

if go:
    output = bk.get_output(input)
    st.write(output)
