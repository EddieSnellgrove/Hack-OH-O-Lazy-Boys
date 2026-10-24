import streamlit as st
def run_app():
    s = st.text_input()
    st.button(on_click=submit(s))

def submit(s):
    print(s)
    
    
if __name__ == "__main__":
    run_app()