import requests
import streamlit as st
import time

# Set up web page.
st.set_page_config(layout="wide")
empty_col1, col1, empty_col2 = st.columns([0.5, 2.0, 0.5])

# Define api_key and URL
api_key_nasa = "7KBBGutXsyswaaAb7dKYXd57NYO3pgOMyjOK7b7e"
url = f"https://api.nasa.gov/planetary/apod?api_key={api_key_nasa}"

# Get data through API.
response = requests.get(url)
content = response.json()

# Parse explanation and image URL
title = content["title"]
explanation = content["explanation"]
image_url = content["url"]

# Parse image file extension.
file_extension = image_url.split(".")[3]

# Get image file through API
image_response = requests.get(image_url)
image_binary = image_response.content

with open(f"today_image.{file_extension}", "wb") as today_image:
	today_image.write(image_binary)

# Create web page per prefered layout and contents.
with col1:		
	st.header(content["title"])
	st.image("today_image.jpg")
	st.write(explanation)
