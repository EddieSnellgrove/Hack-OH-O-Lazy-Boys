import streamlit as st

def go_to_next_step():
    st.session_state.step += 1

def run_app():
    print("testing")
    
    if "step" not in st.session_state:
        st.session_state.step = 1

    if "location" not in st.session_state:
        st.session_state.location = 0

    col1, col2 = st.columns(2)

    if st.session_state.step == 1:
        with col1:
            if st.button("Tap to begin."):
                go_to_next_step()
                st.rerun()

    elif st.session_state.step == 2:
        with col1:
            st.session_state.location = st.number_input("Insert a number", key="num_input", step=1)
        
        with col2:
            if st.button("Next"):
                go_to_next_step()
                st.rerun()

    elif st.session_state.step == 3:
        st.write("The current number is ", st.session_state.location)

if __name__ == "__main__":
    run_app()