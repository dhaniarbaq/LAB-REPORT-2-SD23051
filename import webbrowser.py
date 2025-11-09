# streamlit_app.py
import streamlit as st
import webbrowser

# App title
st.title("🎵 Rickroll Time! 🎵")
st.subheader("Never Gonna Give You Up - Rick Astley")

# Short teaser of the lyrics
teaser = """
We're no strangers to love  
You know the rules and so do I  
A full commitment's what I'm thinkin' of  
(lyrics continue...)
"""
st.text(teaser)

# YouTube link
youtube_link = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"

# Button to open YouTube
if st.button("🎶 Play Full Song on YouTube"):
    webbrowser.open(youtube_link)
    st.success("Opening the full song on YouTube!")
