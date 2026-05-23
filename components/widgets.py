import streamlit as st


def widgets_display():
    st.write("widget slider")
    x = st.slider("x")  # widget
    st.write(x, "squared is", x * x)

    st.write("Input element")
    st.write("Input your name here : ")
    st.text_input("Your name", key="name")

    if st.session_state.name:

        st.write(f"Hello {st.session_state.name}")
    else:
        st.write(f"Put yourname")

