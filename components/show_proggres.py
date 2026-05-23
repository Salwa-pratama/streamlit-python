import streamlit as st
import time

def show_progress():
    # Show progress
    st.markdown("# Show progress")
    st.write("Starting a long computation")
    # Add a placeholder
    latest_iteration = st.empty()
    bar = st.progress(0)
    st.write("Karena pada dasarnya python dieksekusi secara berurutan dari atas ke bawah maka dari itu dia nunggu proses iterasi selesai dulu baru menampilkan elemen dibawah nya")
    for i in range(100):
        # Update the proggress bar with easch iteration
        latest_iteration.text(f'Iteration {i+1}')
        bar.progress(1+1)
        time.sleep(0.1)

    st.write("And now we're done!")



