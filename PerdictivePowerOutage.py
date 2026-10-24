import streamlit as st

def go_to_next_step():
    st.session_state.step += 1

def run_app():
    print("testing")
    
    if "step" not in st.session_state:
        st.session_state.step = 1

    if "latitude" not in st.session_state:
        st.session_state.latitude = 0.0

    if "longitude" not in st.session_state:
        st.session_state.longitude = 0.0

    col1, col2 = st.columns(2)

    if st.session_state.step == 1:
        with col1:
            if st.button("Tap to begin."):
                go_to_next_step()
                st.rerun()

    elif st.session_state.step == 2:
        with col1:
            st.session_state.latitude = st.number_input(
                "Latitude", min_value=-90.0, max_value=90.0, value=0.0, format="%.6f", key="lat_input"
            )
        
        with col2:
            st.session_state.longitude = st.number_input(
                "Longitude", min_value=-180.0, max_value=180.0, value=0.0, format="%.6f", key="lon_input"
            )
        
        if st.button("Next"):
            go_to_next_step()
            st.rerun()

    elif st.session_state.step == 3:
        st.write(f"The entered coordinates are: **Latitude:** {st.session_state.latitude}, **Longitude:** {st.session_state.longitude}")

if __name__ == "__main__":
    run_app()