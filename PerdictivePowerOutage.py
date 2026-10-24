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

    if st.session_state.step == 1:
        buttonslot2.button("Tap to begin.", on_click=go_to_next_step)   
    
def go_to_next_step(user_answer = ""):
    match st.session_state.step:
        case 1:
            print("testing")
    st.session_state.step += 1

def submit():
    print("testing")
    
if __name__ == "__main__":
    run_app()