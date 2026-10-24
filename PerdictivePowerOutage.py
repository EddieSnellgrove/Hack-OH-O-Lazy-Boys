import streamlit as st
def run_app():
    print("testing")
    col1, col1,  = st.columns(2)
    
    header = st.empty()
    subheader = st.empty()
    
    col1, col2 = st.columns(2)
    
    buttonslot1 = col1.empty()
    buttonslot2 = col2.empty()

        
    if "step" not in st.session_state:
        st.session_state.step = 1

    if "items_to_send_to_agent" not in st.session_state:    
        st.session_state.location = 000000

    if st.session_state.step == 1:
        buttonslot2.button("Tap to begin.", on_click=go_to_next_step)  
    if st.session_state.step == 2:
        st.session_state.location = st.number_input("Insert a number")

    if st.session_state.step == 3:
        st.write("The current number is ", st.session_state.location)  

def display_input(): 
    number = st.number_input("Insert a number")
    st.write("The current number is ", number)

def go_to_next_step(user_answer = ""):
        
    st.session_state.step += 1

def submit():
    print("testing")
    
if __name__ == "__main__":
    run_app()